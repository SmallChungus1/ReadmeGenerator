import os
import sys
import shutil
import subprocess
import argparse
import requests
import json
import fnmatch
from datetime import datetime
import tempfile
import io

try:
    import tiktoken
except ImportError:
    tiktoken = None

# --- Constants ---

DEFAULT_IGNORE_DIRS = {
    ".git", "node_modules", "dist", "build", "target", ".venv", "venv", "__pycache__", ".idea", ".vscode"
}
DEFAULT_IGNORE_PATTERNS = {
    "*.min.js", "*.min.css", "*.png", "*.jpg", "*.jpeg", "*.gif", "*.pdf", "*.zip", "*.jar", "*.class",
    "*.xcf", "*.exe", "*.dll", "*.so", "*.dylib", "*.o", "*.obj", "*.pyc", "*.pyo", "*.db", "*.sqlite",
    "*.svg", "*.ico", "*.woff", "*.woff2", "*.ttf", "*.eot", "*.mp3", "*.mp4", "*.wav", "*.avi", "*.mov",
    "*.md"
}
LOCKFILE_NAMES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock"
}
CONFIG_FILES = {
    "pom.xml", "package.json", "pyproject.toml", "Dockerfile", "docker-compose.yml", "Makefile",
    ".env", ".env.example", ".gitignore", ".dockerignore"
}

# --- Helpers ---

def count_tokens(text):
    """
    Counts the number of tokens in the given text using tiktoken (cl100k_base).
    Returns -1 if tiktoken is not installed.
    """
    if not tiktoken:
        return -1
    try:
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))
    except Exception:
        return -1

def get_repo_id(repo_str):
    """
    Parses a repo identifier like apache/commons-cli (optionally branch/tag/commit).
    Returns (user/repo, ref)
    """
    parts = repo_str.split('/')
    if len(parts) < 2:
        raise ValueError("Invalid repo identifier. Expected 'user/repo'.")
    
    user_repo = f"{parts[0]}/{parts[1]}"
    ref = parts[2] if len(parts) > 2 else None
    return user_repo, ref

def clone_repo(user_repo, ref, temp_dir):
    """
    Attempts to clone the repo using git.
    Returns the commit SHA if successful.
    """
    try:
        repo_url = f"https://github.com/{user_repo}.git"
        cmd = ["git", "clone", "--depth", "1", repo_url, temp_dir]
        if ref:
            cmd.extend(["-b", ref])
        
        subprocess.run(cmd, check=True, capture_output=True)
        
        # Get SHA
        result = subprocess.run(["git", "-C", temp_dir, "rev-parse", "HEAD"], 
                               check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Git clone failed: {e}. Falling back to zip download.")
        return None

def download_zip(user_repo, ref, temp_dir):
    """
    Downloads the repo as a ZIP archive and extracts it.
    Returns the 'ref' used or 'HEAD'.
    """
    ref = ref or "HEAD"
    url = f"https://github.com/{user_repo}/archive/{ref}.zip"
    response = requests.get(url)
    response.raise_for_status()
    
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall(temp_dir)
    
    # Github zips are nested inside a folder like repo-ref
    nested_dir = os.listdir(temp_dir)[0]
    extracted_path = os.path.join(temp_dir, nested_dir)
    
    # Move everything up
    for item in os.listdir(extracted_path):
        shutil.move(os.path.join(extracted_path, item), temp_dir)
    
    os.rmdir(extracted_path)
    return ref # Or we could try to find the SHA if possible... but zip doesn't provide it easily.

def is_ignored(path, root_dir):
    filename = os.path.basename(path)

    # Always include config files regardless of other rules
    if filename in CONFIG_FILES:
        return False

    rel_path = os.path.relpath(path, root_dir)
    parts = rel_path.split(os.sep)
    
    # Check ignored dirs
    if any(p in DEFAULT_IGNORE_DIRS for p in parts):
        return True
    
    # Check ignore patterns on filename
    if any(fnmatch.fnmatch(filename, pat) for pat in DEFAULT_IGNORE_PATTERNS):
        return True
    
    # Binary check: look for null bytes
    try:
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                chunk = f.read(1024)
                if b'\0' in chunk:
                    return True
    except Exception:
        return True # If we can't read it, ignore it
    
    return False

def get_repo_structure(root_dir):
    """
    Generates a tree-like string representing the directory structure,
    excluding ignored files/directories.
    """
    lines = []
    
    def _build_tree(current_dir, prefix=""):
        try:
            items = sorted(os.listdir(current_dir))
        except Exception:
            return
            
        # Filter items
        valid_items = []
        for item in items:
            item_path = os.path.join(current_dir, item)
            if not is_ignored(item_path, root_dir):
                valid_items.append(item)
                
        for i, item in enumerate(valid_items):
            item_path = os.path.join(current_dir, item)
            is_last = (i == len(valid_items) - 1)
            connector = "└── " if is_last else "├── "
            
            lines.append(f"{prefix}{connector}{item}")
            
            if os.path.isdir(item_path):
                new_prefix = prefix + ("    " if is_last else "│   ")
                _build_tree(item_path, new_prefix)

    lines.append(".")
    _build_tree(root_dir)
    return "\n".join(lines)

# --- Core Logic ---

def run_ingest(args):
    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)
    
    for repo_str in args.repo:
        user_repo, ref = get_repo_id(repo_str)
        print(f"--- Processing {user_repo} ---")
        
        # Determine prefix
        if args.prefix:
            prefix = args.prefix
        else:
            # Default prefix: sanitize user/repo to user_repo_
            prefix = user_repo.replace('/', '_') + "_"
            
        with tempfile.TemporaryDirectory() as temp_dir:
            sha = clone_repo(user_repo, ref, temp_dir)
            if not sha:
                sha = download_zip(user_repo, ref, temp_dir)
                
            # Analysis
            stats = {
                "total_scanned": 0,
                "included": 0,
                "skipped_rule": 0,
                "skipped_size": 0,
                "languages": {},
                "top_files": [] # list of (size, path)
            }
            
            readme_content = ""
            output_data = [] # List of strings to be joined
            
            # Root README
            readme_name = f"{prefix}README.md"
            parsed_name = f"{prefix}parsed_code.txt"

            for f in os.listdir(temp_dir):
                if f.lower().startswith("readme") and os.path.isfile(os.path.join(temp_dir, f)):
                    with open(os.path.join(temp_dir, f), 'r', encoding='utf-8', errors='ignore') as rf:
                        readme_content = rf.read()
                    break
            
            if not readme_content:
                readme_content = " (No README.md found in repository) "
                
            with open(os.path.join(out_dir, readme_name), 'w', encoding='utf-8') as f:
                f.write(readme_content)
                
            # Walk
            for root, dirs, files in os.walk(temp_dir):
                # Prune dirs
                dirs[:] = [d for d in dirs if d not in DEFAULT_IGNORE_DIRS]
                
                for file in files:
                    stats["total_scanned"] += 1
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, temp_dir)
                    
                    if is_ignored(full_path, temp_dir):
                        stats["skipped_rule"] += 1
                        continue
                    
                    size = os.path.getsize(full_path)
                    
                    # Check caps
                    is_config = file in CONFIG_FILES
                    mb_cap = args.max_bytes if not is_config else args.max_bytes * 5 # Config files get 5x cap
                    
                    if size > mb_cap:
                        stats["skipped_size"] += 1
                        continue
                    
                    try:
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                            lines = f.readlines()
                            
                        if len(lines) > args.max_lines and not is_config:
                            stats["skipped_size"] += 1
                            continue
                            
                        # Handle lockfiles
                        if file in LOCKFILE_NAMES:
                            lines = lines[:80] + ["... (truncated)"]
                            
                        content = "".join(lines)
                        
                        # Language detection (very basic)
                        ext = os.path.splitext(file)[1].lower() or "no_ext"
                        stats["languages"][ext] = stats["languages"].get(ext, 0) + 1
                        
                        stats["included"] += 1
                        stats["top_files"].append((size, rel_path))
                        
                        # Store block
                        output_data.append(f"---\nFile: {rel_path}\nSize: {size} bytes\nLines: {len(lines)}\n---\n{content}\n")
                        
                    except Exception:
                        stats["skipped_rule"] += 1 # Binary or unreadable
                        
            # Sort top files
            stats["top_files"].sort(key=lambda x: x[0], reverse=True)
            stats["top_files"] = stats["top_files"][:15]
            
            # Header
            header = [
                f"Repo: {user_repo}",
                f"Commit: {sha}",
                f"Timestamp: {datetime.now().isoformat()}",
                "",
                "--- Repository Structure ---",
                get_repo_structure(temp_dir),
                "",
                "--- Summary Report ---",
                f"Total files scanned: {stats['total_scanned']}",
                f"Files included: {stats['included']}",
                f"Files skipped by rule: {stats['skipped_rule']}",
                f"Files skipped by size: {stats['skipped_size']}",
                f"Detected languages count: {len(stats['languages'])}",
                "Top 15 largest included files:"
            ]
            for s, p in stats["top_files"]:
                header.append(f"  {s} bytes - {p}")
            header.append("-----------------------")
            
            # Token count
            full_content = "\n".join(header) + "\n\n" + "\n".join(output_data)
            tokens = count_tokens(full_content)
            
            token_line = f"Tokens: {tokens if tokens >= 0 else 'N/A (tiktoken not installed)'}"
            final_output = f"{token_line}\n{full_content}"

            with open(os.path.join(out_dir, parsed_name), 'w', encoding='utf-8') as f:
                f.write(final_output)
            
            print(f"Ingest complete for {user_repo}. Output: {parsed_name} ({tokens} tokens)")

def run_chunk(args):
    input_file = os.path.abspath(args.input)
    out_file = os.path.abspath(args.out)
    chunk_tokens = args.chunk_tokens
    overlap = args.overlap
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
        
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Split by blocks using the specific header pattern
    # The pattern is: ---\nFile: [path]\nSize: [size]\nLines: [lines]\n---
    blocks = content.split("\n---\nFile: ")
    if len(blocks) < 2:
        print("No files found in the input file or format is invalid.")
        return

    # First block is the summary header
    summary_header = blocks[0]
    file_blocks = blocks[1:]
    
    chunks = []
    
    for block in file_blocks:
        # Re-add "File: " because it was consumed by split
        full_block = "File: " + block
        
        # Parse the header lines
        try:
            header_lines = full_block.split('\n', 4)
            if len(header_lines) < 5: continue
            
            file_path = header_lines[0].replace("File: ", "").strip()
            # header_lines[1] is Size
            # header_lines[2] is Lines
            # header_lines[3] is "---"
            file_content = header_lines[4]
            
            # Simple chunking logic (character based approximation)
            chunk_size_chars = chunk_tokens * 4
            overlap_chars = overlap * 4
            
            if len(file_content) <= chunk_size_chars:
                chunks.append({
                    "file": file_path,
                    "chunk": file_content.strip(),
                    "chunk_id": 0
                })
            else:
                start = 0
                chunk_id = 0
                while start < len(file_content):
                    end = start + chunk_size_chars
                    chunk_text = file_content[start:end]
                    
                    chunks.append({
                        "file": file_path,
                        "chunk": chunk_text.strip(),
                        "chunk_id": chunk_id
                    })
                    
                    if end >= len(file_content):
                        break
                    start = end - overlap_chars
                    chunk_id += 1
        except Exception as e:
            print(f"Error parsing block: {e}")
            continue
            
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        for c in chunks:
            f.write(json.dumps(c) + "\n")
            
    print(f"Chunking complete. {len(chunks)} chunks written to {out_file}")

def main():
    parser = argparse.ArgumentParser(description="Repo Ingest CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Ingest
    ingest_parser = subparsers.add_parser("ingest", help="Ingest one or more repositories")
    ingest_parser.add_argument("repo", nargs='+', help="GitHub repo(s) (user/repo[/branch or commit])")
    ingest_parser.add_argument("--out", default="./out", help="Output directory")
    ingest_parser.add_argument("--prefix", default="", help="Override default prefix (sanitized_repo_name_)")
    ingest_parser.add_argument("--max-lines", type=int, default=3000, help="Max lines per file")
    ingest_parser.add_argument("--max-bytes", type=int, default=2000000, help="Max bytes per file")
    
    # Chunk
    chunk_parser = subparsers.add_parser("chunk", help="Chunk the parsed code")
    chunk_parser.add_argument("input", help="Path to parsed_code.txt")
    chunk_parser.add_argument("--out", default="./out/chunks.jsonl", help="Output JSONL file")
    chunk_parser.add_argument("--chunk-tokens", type=int, default=800, help="Approximate tokens per chunk")
    chunk_parser.add_argument("--overlap", type=int, default=80, help="Approximate overlap tokens")
    
    args = parser.parse_args()
    
    if args.command == "ingest":
        run_ingest(args)
    elif args.command == "chunk":
        run_chunk(args)

if __name__ == "__main__":
    main()
