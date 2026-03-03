# ReadmeGenerator

A tool for ingesting Entire GitHub repositories into a single, LLM-friendly text file with built-in token counting and chunking capabilities.

## Features

- **Repo Ingest**: Clones or downloads GitHub repositories and aggregates all relevant code into one file.
- **Token Counting**: Automatically calculates OpenAI-compatible tokens (cl100k_base) for the output.
- **Smart Filtering**: Ignores binary files, common build directories (`node_modules`, `venv`, etc.), and large files by default.
- **Config Awareness**: Always includes essential config files (e.g., `package.json`, `Dockerfile`, `.env`) even if they match ignore patterns.
- **Chunking**: Splits large ingested files into JSONL chunks for easier processing by RAG systems or LLMs.

## Installation

```powershell
# Create a virtual environment
python -m venv venv

# Activate and install dependencies
.\venv\Scripts\activate
pip install requests tiktoken
```

## Usage

### 1. Ingest Repositories

The `ingest` command pulls code from GitHub and creates a parsed summary.

```powershell
python repo_ingest.py ingest <user/repo> [repo2...] [options]
```

**Options:**
- `--out`: Output directory (default: `./out`)
- `--max-lines`: Maximum lines per file (default: 3000)
- `--max-bytes`: Maximum bytes per file (default: 2,000,000)
- `--prefix`: Custom prefix for output files.

**Example:**
```powershell
python repo_ingest.py ingest pallets/click --out ./my_repos
```

### 2. Chunk Parsed Data

The `chunk` command splits the generated `.txt` into smaller, overlapping chunks.

```powershell
python repo_ingest.py chunk <input_file> [options]
```

**Options:**
- `--out`: Path to output `.jsonl` file.
- `--chunk-tokens`: Approximate tokens per chunk (default: 800).
- `--overlap`: Token overlap between chunks (default: 80).

## Output Format

The `ingest` command generates two files per repository:
1. `[prefix]README.md`: The original repository's README content.
2. `[prefix]parsed_code.txt`: A single file containing:
   - Total Token Count at the top.
   - Repository Structure.
   - Summary Report (Stats).
   - All file contents separated by headers.
