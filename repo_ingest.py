import os
import sys
import ast
import re
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

# ---------------------------------------------------------------------------
# Optional: tree-sitter (>= 0.21 new-style API)
# Install: pip install tree-sitter tree-sitter-python tree-sitter-javascript
#          tree-sitter-typescript
# ---------------------------------------------------------------------------
_TS_PARSERS: dict = {}   # ext -> (parser, lang_name)

def _init_tree_sitter() -> None:
    """Populate _TS_PARSERS if tree-sitter and any grammar packages are available."""
    try:
        from tree_sitter import Language, Parser  # type: ignore[import-untyped]  # noqa: F401
    except ImportError:
        return  # tree-sitter not installed, skip silently

    def _try_register(exts, module_name, lang_factory):
        try:
            mod = __import__(module_name)
            lang = Language(lang_factory(mod))  # type: ignore[name-defined]
            p = Parser(lang)  # type: ignore[name-defined]
            for ext in exts:
                _TS_PARSERS[ext] = (p, module_name)
        except Exception:
            pass

    _try_register([".py"],               "tree_sitter_python",     lambda m: m.language())
    _try_register([".js", ".jsx", ".mjs"], "tree_sitter_javascript", lambda m: m.language())
    _try_register([".ts"],               "tree_sitter_typescript",  lambda m: m.language_typescript())
    _try_register([".tsx"],              "tree_sitter_typescript",  lambda m: m.language_tsx())

_init_tree_sitter()


# ---------------------------------------------------------------------------
# Optional: universal-ctags (--output-format=json support required)
# ---------------------------------------------------------------------------
_CTAGS_BIN: str | None = None
_CTAGS_CHECKED: bool = False

def _check_ctags() -> str | None:
    """Return path to universal-ctags binary with JSON support, or None. Result cached."""
    global _CTAGS_BIN, _CTAGS_CHECKED
    if _CTAGS_CHECKED:
        return _CTAGS_BIN
    _CTAGS_CHECKED = True
    path = shutil.which("ctags")
    if not path:
        return None
    try:
        result = subprocess.run([path, "--version"], capture_output=True, text=True, timeout=5)
        if "universal ctags" not in (result.stdout + result.stderr).lower():
            return None   # macOS BSD / Exuberant ctags — no JSON support
    except Exception:
        return None
    _CTAGS_BIN = path
    return _CTAGS_BIN


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_IGNORE_DIRS = frozenset({
    # VCS / IDE
    ".git", ".hg", ".svn", ".idea", ".vscode",
    # Dependencies
    "node_modules", "bower_components", "vendor",
    # Build outputs
    "dist", "build", "target", "out", "output", ".output",
    "buck-out", ".buck", "DerivedData", "Pods",
    ".next", ".nuxt",
    # Python
    ".venv", "venv", "__pycache__", ".eggs", ".tox",
    "site-packages", "dist-packages",
    # Caches
    "cache", ".cache", ".pytest_cache", ".nyc_output",
    ".gradle", ".m2",
    # Coverage / reports
    "coverage", "htmlcov", "lcov-report",
    # Temp / logs
    "tmp", "temp", ".tmp", ".temp", "logs",
    # Generated code
    "generated", "__generated__",
    # Tests — noise for README generation
    "tests", "test", "spec", "specs", "__tests__", "__mocks__", "fixtures",
    # CI/CD config — not useful for understanding how to use the code
    ".github", ".circleci", ".travis",
})

DEFAULT_IGNORE_PATTERNS = frozenset({
    # Images / media
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.svg", "*.ico",
    "*.xcf", "*.webp", "*.bmp",
    "*.mp3", "*.mp4", "*.wav", "*.avi", "*.mov",
    # Fonts
    "*.woff", "*.woff2", "*.ttf", "*.eot",
    # Archives / binaries
    "*.zip", "*.tar", "*.gz", "*.bz2", "*.xz", "*.rar",
    "*.jar", "*.war", "*.ear",
    "*.exe", "*.dll", "*.so", "*.dylib",
    "*.o", "*.obj", "*.a", "*.lib",
    # Compiled / bytecode
    "*.class", "*.pyc", "*.pyo", "*.pyd",
    # DB / certs
    "*.db", "*.sqlite", "*.sqlite3",
    "*.pem", "*.p12", "*.pfx",
    # Minified / bundled assets
    "*.min.js", "*.min.css",
    "*.bundle.js", "*.chunk.js",
    # Source maps
    "*.map",
    # PDF / Office docs
    "*.pdf", "*.doc", "*.docx", "*.xls", "*.xlsx", "*.ppt",
    # Protobuf / generated stubs
    "*.pb.go", "*.pb.cc", "*.pb.h",
    "*.g.dart", "*.freezed.dart",
    # Diagram / binary-ish data files
    "*.gliffy", "*.drawio", "*.excalidraw",
    # README / docs (excluded from model input; captured separately)
    "*.md", "*.rst",
})

LOCKFILE_NAMES = frozenset({
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "poetry.lock", "Gemfile.lock", "Cargo.lock",
    "uv.lock", "composer.lock", "Pipfile.lock", "mix.lock",
})

# Stems (case-insensitive) that are legal/project-management boilerplate —
# zero signal for README generation.
BOILERPLATE_STEMS = frozenset({
    "license", "licence", "notice", "copying", "patents",
    "changelog", "changes", "history", "news", "releases",
    "authors", "contributors", "maintainers",
    "code_of_conduct", "contributing", "security",
})

# How many files sharing the same basename (e.g. "Dockerfile") are kept
# before the rest are deduplicated.  Prevents repos that repeat the same
# manifest across many version subdirectories from blowing the budget.
MAX_COPIES_PER_BASENAME = 2

# Tier-0: build/dependency manifests + run/deploy configs.  Always included.
PRIORITY_MANIFESTS = frozenset({
    # Package managers / build tools
    "package.json", "pom.xml",
    "build.gradle", "settings.gradle",
    "build.gradle.kts", "settings.gradle.kts",
    "pyproject.toml", "requirements.txt", "setup.py", "setup.cfg",
    "MANIFEST.in",
    "Cargo.toml", "go.mod", "go.sum",
    "Gemfile", "composer.json",
    "build.sbt", "mix.exs", "CMakeLists.txt",
    # Run / deploy
    "Dockerfile", "docker-compose.yml", "docker-compose.yaml",
    "Makefile", ".env.example", "Procfile",
})

# Files that bypass the per-file size cap (5x headroom)
CONFIG_FILES = PRIORITY_MANIFESTS | {".env", ".gitignore", ".dockerignore"}

# Filenames (stem only, lower-cased) treated as likely entrypoints
ENTRYPOINT_STEMS = frozenset({
    "main", "app", "server", "index", "cli", "__main__",
    "wsgi", "asgi", "run", "start", "manage", "application",
    "entrypoint", "entry", "launcher",
})

# Extensions for which structural extraction is attempted
STRUCTURAL_EXTENSIONS = frozenset({
    ".py", ".js", ".ts", ".jsx", ".tsx", ".mjs",
    ".java", ".go", ".rs", ".kt",
})

# Extensions where ctags fallback applies (languages not covered by existing extractors)
CTAGS_EXTENSIONS = frozenset({
    ".c", ".h", ".cpp", ".cc", ".cxx", ".hh", ".hpp", ".hxx",
    ".rb", ".php", ".swift", ".scala", ".lua",
    ".sh", ".bash", ".cs", ".pl", ".pm",
    ".ex", ".exs", ".erl", ".hs", ".ml", ".mli",
    ".r", ".R", ".m", ".d", ".nim",
})

# Files with more lines than this threshold get structural extraction
AST_THRESHOLD_LINES = 80

# Default total-output token budget
DEFAULT_BUDGET_TOKENS = 80_000


# ---------------------------------------------------------------------------
# Token counting
# ---------------------------------------------------------------------------

def count_tokens(text: str) -> int:
    """Returns token count via tiktoken, or -1 if unavailable."""
    if not tiktoken:
        return -1
    try:
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return -1


def _estimate_tokens(text: str) -> int:
    """Fast token estimate: ~1 token per 3 chars (intentionally conservative for code)."""
    return max(1, len(text) // 3)


# ---------------------------------------------------------------------------
# Repo acquisition helpers (unchanged from original)
# ---------------------------------------------------------------------------

def get_repo_id(repo_str):
    parts = repo_str.split('/')
    if len(parts) < 2:
        raise ValueError("Invalid repo identifier. Expected 'user/repo'.")
    return f"{parts[0]}/{parts[1]}", (parts[2] if len(parts) > 2 else None)


def clone_repo(user_repo, ref, temp_dir):
    try:
        repo_url = f"https://github.com/{user_repo}.git"
        cmd = ["git", "clone", "--depth", "1", repo_url, temp_dir]
        if ref:
            cmd.extend(["-b", ref])
        subprocess.run(cmd, check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", temp_dir, "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True,
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Git clone failed: {e}. Falling back to zip download.")
        return None


def download_zip(user_repo, ref, temp_dir):
    import zipfile
    ref = ref or "HEAD"
    url = f"https://github.com/{user_repo}/archive/{ref}.zip"
    response = requests.get(url)
    response.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall(temp_dir)
    nested_dir = os.listdir(temp_dir)[0]
    extracted_path = os.path.join(temp_dir, nested_dir)
    for item in os.listdir(extracted_path):
        shutil.move(os.path.join(extracted_path, item), temp_dir)
    os.rmdir(extracted_path)
    return ref


# ---------------------------------------------------------------------------
# File filtering
# ---------------------------------------------------------------------------

def is_ignored(path: str, root_dir: str) -> bool:
    """Return True if the path should be excluded from ingestion."""
    filename = os.path.basename(path)

    # Always include priority manifests regardless of other rules
    if filename in CONFIG_FILES:
        return False

    # Exclude all README variants — captured separately as ground truth.
    if filename.lower().startswith("readme"):
        return True

    # Exclude legal / project-management boilerplate (LICENSE, CHANGELOG, etc.)
    stem = os.path.splitext(filename)[0].lower()
    if stem in BOILERPLATE_STEMS:
        return True

    # .pyi stub files are consumed via sibling lookup during .py processing; never standalone.
    if os.path.splitext(filename)[1].lower() == ".pyi":
        return True

    # .txt files are only useful as requirements* inputs; everything else
    # (license bodies, changelogs, release notes, template text) is noise.
    if os.path.splitext(filename)[1].lower() == ".txt":
        if not re.match(r"^requirements", filename, re.IGNORECASE):
            return True

    rel_path = os.path.relpath(path, root_dir)
    parts = rel_path.replace(os.sep, "/").split("/")

    if any(p in DEFAULT_IGNORE_DIRS for p in parts):
        return True

    if any(fnmatch.fnmatch(filename, pat) for pat in DEFAULT_IGNORE_PATTERNS):
        return True

    # Binary sniff
    try:
        if os.path.isfile(path):
            with open(path, "rb") as f:
                if b"\x00" in f.read(1024):
                    return True
    except Exception:
        return True

    return False


# ---------------------------------------------------------------------------
# Priority scoring
# ---------------------------------------------------------------------------

def score_file(rel_path: str) -> tuple:
    """
    Returns a sortable tuple (tier, depth, name).
    Lower tier = higher priority.

    Tiers:
      0  — build/deploy manifests (PRIORITY_MANIFESTS)
      20 — root-level config/schema files
      30 — likely entrypoints at any depth
      40 — all other source files (depth used as tiebreaker)
      50 — docs / examples / samples (low priority; budget usually cuts these)
    """
    parts = rel_path.replace(os.sep, "/").split("/")
    filename = parts[-1]
    stem = os.path.splitext(filename)[0].lower()
    depth = len(parts) - 1

    if filename in PRIORITY_MANIFESTS:
        return (0, depth, filename)

    # Root-level config-like files
    if depth == 0:
        ext = os.path.splitext(filename)[1].lower()
        if ext in (".toml", ".yaml", ".yml", ".json", ".ini", ".cfg") or filename.startswith("."):
            return (20, depth, filename)

    # Likely entrypoints
    if stem in ENTRYPOINT_STEMS:
        return (30, depth, filename)

    # Docs / examples — include last so budget cuts them first
    if parts[0].lower() in ("docs", "doc", "examples", "example", "samples", "sample", "demo", "demos"):
        return (50, depth, filename)

    return (40, depth, filename)


# ---------------------------------------------------------------------------
# Structural extraction: Python (ast)
# ---------------------------------------------------------------------------

def _try_unparse(node) -> str:
    """ast.unparse added in 3.9; gracefully degrade."""
    try:
        return ast.unparse(node)
    except AttributeError:
        return "..."
    except Exception:
        return "..."


def _get_docstring_snippet(node, max_len: int = 160) -> str | None:
    if (
        node.body
        and isinstance(node.body[0], ast.Expr)
        and isinstance(node.body[0].value, ast.Constant)
        and isinstance(node.body[0].value.value, str)
    ):
        doc = node.body[0].value.value.strip().replace("\n", " ")
        return doc[:max_len] + ("..." if len(doc) > max_len else "")
    return None


def _format_func_sig(node) -> str:
    """Render a FunctionDef/AsyncFunctionDef as a one-line signature."""
    prefix = "async def " if isinstance(node, ast.AsyncFunctionDef) else "def "
    try:
        args_str = _try_unparse(node.args)
    except Exception:
        args_str = "..."
    ret = ""
    if node.returns:
        ret = f" -> {_try_unparse(node.returns)}"
    decorators = "".join(f"    @{_try_unparse(d)}\n" for d in node.decorator_list)
    return f"{decorators}    {prefix}{node.name}({args_str}){ret}: ..."


def _format_class(node) -> str:
    lines = []
    bases = ", ".join(_try_unparse(b) for b in node.bases)
    header = f"class {node.name}" + (f"({bases})" if bases else "") + ":"
    doc = _get_docstring_snippet(node)
    if doc:
        lines.append(f'    """{ doc }"""')

    for child in node.body:
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
            lines.append(_format_func_sig(child))
            child_doc = _get_docstring_snippet(child)
            if child_doc:
                lines.append(f'        """{ child_doc }"""')
        elif isinstance(child, ast.Assign):
            # Class-level attributes
            for t in child.targets:
                lines.append(f"    {_try_unparse(t)} = ...")
        elif isinstance(child, ast.AnnAssign):
            ann = _try_unparse(child.annotation)
            lines.append(f"    {_try_unparse(child.target)}: {ann}")

    if not lines:
        lines.append("    ...")
    return header + "\n" + "\n".join(lines)


def _extract_python_structure(source: str) -> str | None:
    """
    Use the built-in ast module to extract a structural skeleton of a Python file.
    Returns None on parse failure (caller should fall back to raw content).
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    out = []

    # Module docstring
    doc = _get_docstring_snippet(tree)
    if doc:
        out.append(f'"""{ doc }"""')
        out.append("")

    # Imports (all top-level)
    for node in tree.body:
        if isinstance(node, ast.Import):
            out.append(_try_unparse(node))
        elif isinstance(node, ast.ImportFrom):
            out.append(_try_unparse(node))

    out.append("")

    # Top-level classes and functions
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            out.append(_format_class(node))
            out.append("")
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Top-level function: include decorators + signature + docstring
            decorators = "".join(f"@{_try_unparse(d)}\n" for d in node.decorator_list)
            prefix = "async def " if isinstance(node, ast.AsyncFunctionDef) else "def "
            args_str = _try_unparse(node.args)
            ret = f" -> {_try_unparse(node.returns)}" if node.returns else ""
            sig = f"{decorators}{prefix}{node.name}({args_str}){ret}:"
            func_doc = _get_docstring_snippet(node)
            body = f'    """{ func_doc }"""' if func_doc else "    ..."
            out.append(sig)
            out.append(body)
            out.append("")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Structural extraction: JS / TS / Java / Go / Rust  (regex-based)
# ---------------------------------------------------------------------------

# Patterns: lines that are "worth keeping" for skeleton purposes.
# We include declaration/import lines and omit bodies.

_JS_KEEP = re.compile(
    r"""
    ^ \s* (
        import \b
        | export \b
        | (export\s+)?(default\s+)?(async\s+)?function\b
        | (export\s+)?class\b
        | (export\s+)?(const|let|var)\s+\w+\s*=\s*(async\s+)?(\(|function\b)
        | (async\s+)?\w[\w$]*\s*\(        # method-like
        | (public|private|protected|static|abstract|override|readonly)\b
        | \}                              # closing braces for context
    )
    """,
    re.VERBOSE,
)

_JAVA_KEEP = re.compile(
    r"""
    ^ \s* (
        package \b
        | import \b
        | @\w+                            # annotations
        | (public|private|protected|abstract|final|static|default)\b
        | class\b | interface\b | enum\b | record\b
        | \}
    )
    """,
    re.VERBOSE,
)

_GO_KEEP = re.compile(
    r"""
    ^ \s* (
        package \b
        | import \b
        | \" [\w./]                       # import path inside block
        | func\b
        | type\b
        | var\b
        | const\b
        | \}
    )
    """,
    re.VERBOSE,
)

_RUST_KEEP = re.compile(
    r"""
    ^ \s* (
        use\b | pub\b | fn\b | struct\b | enum\b
        | trait\b | impl\b | mod\b | type\b
        | extern\b | const\b | static\b
        | \#\[                            # attributes
        | \}
    )
    """,
    re.VERBOSE,
)

_KOTLIN_KEEP = re.compile(
    r"""
    ^ \s* (
        package\b | import\b
        | (public|private|protected|internal|abstract|open|final|override|data|sealed|inline|suspend)\b
        | (fun|class|object|interface|enum|typealias)\b
        | @\w+
        | \}
    )
    """,
    re.VERBOSE,
)


def _extract_regex_structure(content: str, pattern: re.Pattern, max_out_lines: int = 300) -> str:
    """Keep only lines matching *pattern* plus blank separators. Collapse runs of }."""
    kept = []
    prev_was_brace = False
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if pattern.search(line):
            if stripped == "}" and prev_was_brace:
                continue  # de-duplicate close-brace runs
            kept.append(line.rstrip())
            prev_was_brace = stripped.startswith("}")
        else:
            prev_was_brace = False
        if len(kept) >= max_out_lines:
            kept.append("// ... (truncated)")
            break
    return "\n".join(kept)


_EXT_TO_REGEX: dict[str, re.Pattern] = {
    ".js":   _JS_KEEP,
    ".jsx":  _JS_KEEP,
    ".ts":   _JS_KEEP,
    ".tsx":  _JS_KEEP,
    ".mjs":  _JS_KEEP,
    ".cjs":  _JS_KEEP,
    ".java": _JAVA_KEEP,
    ".go":   _GO_KEEP,
    ".rs":   _RUST_KEEP,
    ".kt":   _KOTLIN_KEEP,
    ".kts":  _KOTLIN_KEEP,
}


# ---------------------------------------------------------------------------
# Optional tree-sitter extraction
# ---------------------------------------------------------------------------

def _ts_extract_declarations(source_bytes: bytes, parser) -> str | None:
    """
    Walk a tree-sitter parse tree and collect declaration/import nodes.
    Returns a skeleton string or None on failure.
    """
    try:
        tree = parser.parse(source_bytes)
        root = tree.root_node

        DECL_TYPES = {
            "import_statement", "import_from_statement",
            "export_statement",
            "class_definition", "class_declaration",
            "function_definition", "function_declaration",
            "method_definition", "arrow_function",
            "lexical_declaration", "variable_declaration",
            "type_alias_declaration", "interface_declaration",
            # Go
            "function_declaration", "method_declaration",
            "type_declaration", "short_var_declaration",
            # Rust
            "use_declaration", "function_item", "struct_item",
            "enum_item", "trait_item", "impl_item", "mod_item",
        }

        lines = source_bytes.decode("utf-8", errors="replace").splitlines()
        kept_lines: set[int] = set()

        def visit(node):
            if node.type in DECL_TYPES:
                # Include only the first line of multi-line nodes (the signature)
                kept_lines.add(node.start_point[0])
            for child in node.children:
                visit(child)

        visit(root)

        result = []
        for i, line in enumerate(lines):
            if i in kept_lines:
                result.append(line)
        return "\n".join(result) if result else None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Structural extraction: .pyi stub files
# ---------------------------------------------------------------------------

def _extract_pyi_structure(full_path: str) -> str | None:
    """Use sibling .pyi stub as skeleton for a .py file. Returns None if not found."""
    pyi_path = os.path.splitext(full_path)[0] + ".pyi"
    if not os.path.isfile(pyi_path):
        return None
    try:
        with open(pyi_path, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read().strip()
        return content if content else None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Structural extraction: universal-ctags fallback
# ---------------------------------------------------------------------------

def _format_ctags_output(json_lines: str, filename: str) -> str | None:
    """Parse ctags JSON-per-line output into a grouped readable skeleton."""
    from collections import defaultdict
    KIND_ORDER = [
        "class", "interface", "struct", "enum", "trait",
        "function", "method", "procedure", "subroutine",
        "field", "member", "variable", "constant", "macro",
        "module", "namespace", "package", "type", "typedef",
    ]
    groups: dict[str, list[str]] = defaultdict(list)
    for line in json_lines.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            tag = json.loads(line)
        except json.JSONDecodeError:
            continue
        name = tag.get("name", "")
        kind = tag.get("kind", "unknown").lower()
        scope = tag.get("scope", "")
        pattern = tag.get("pattern", "")
        if pattern.startswith("/^") and pattern.endswith("$/"):
            pattern = pattern[2:-2].strip()
        elif pattern.startswith("/^"):
            pattern = pattern[2:].rstrip("/").strip()
        display = pattern if pattern else (f"  {scope}.{name}" if scope else name)
        groups[kind].append(display)
    if not groups:
        return None
    lines = [f"# {os.path.basename(filename)} (ctags skeleton)"]
    for kind in KIND_ORDER:
        if kind in groups:
            lines.append(f"\n## {kind.capitalize()}s")
            lines.extend(groups[kind])
    for kind, entries in groups.items():
        if kind not in KIND_ORDER:
            lines.append(f"\n## {kind.capitalize()}s")
            lines.extend(entries)
    return "\n".join(lines) if len(lines) > 1 else None


def _extract_ctags_structure(content: str, filename: str) -> str | None:
    """Shell out to universal-ctags to extract a symbol skeleton. Returns None if unavailable."""
    ctags_bin = _check_ctags()
    if not ctags_bin:
        return None
    ext = os.path.splitext(filename)[1].lower()
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        result = subprocess.run(
            [ctags_bin, "--output-format=json", "--fields=+nKz", "--extras=-F", "-f", "-", tmp_path],
            capture_output=True, text=True, timeout=15,
        )
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None
    finally:
        if tmp_path:
            try:
                os.unlink(tmp_path)
            except Exception:
                pass
    if result.returncode != 0 or not result.stdout.strip():
        return None
    return _format_ctags_output(result.stdout, filename)


# ---------------------------------------------------------------------------
# Main extraction dispatcher
# ---------------------------------------------------------------------------

def extract_structure(content: str, filename: str, full_path: str = "") -> tuple[str, bool]:
    """
    Return (possibly_condensed_content, was_structurally_extracted).

    Strategy (in order of preference):
      0. .pyi sibling stub (for .py files, when full_path provided)
      1. tree-sitter (if parser available for this extension)
      2. Python built-in ast (for .py)
      3. Regex skeleton (for js/ts/java/go/rs/kt)
      4. ctags (for languages in CTAGS_EXTENSIONS)
      5. Raw content (fallback)
    """
    ext = os.path.splitext(filename)[1].lower()

    if ext not in STRUCTURAL_EXTENSIONS and ext not in CTAGS_EXTENSIONS:
        return content, False

    # --- .pyi stub path ---
    if ext == ".py" and full_path:
        result = _extract_pyi_structure(full_path)
        if result is not None:
            return result, True

    # --- tree-sitter path ---
    if ext in _TS_PARSERS:
        parser, _ = _TS_PARSERS[ext]
        result = _ts_extract_declarations(content.encode("utf-8", errors="replace"), parser)
        if result:
            return result, True
        # fall through

    # --- Python ast path ---
    if ext == ".py":
        result = _extract_python_structure(content)
        if result is not None:
            return result, True
        return content, False     # parse failed – keep raw

    # --- Regex path ---
    if ext in _EXT_TO_REGEX:
        return _extract_regex_structure(content, _EXT_TO_REGEX[ext]), True

    # --- ctags path (languages outside existing extractor coverage) ---
    if ext in CTAGS_EXTENSIONS:
        result = _extract_ctags_structure(content, filename)
        if result:
            return result, True

    return content, False


# ---------------------------------------------------------------------------
# Dependency extraction
# Replaces lock/requirements files with a compact "Required Packages" block.
# ---------------------------------------------------------------------------

def _fmt_deps(pairs: list[tuple[str, str]]) -> str:
    """Format (name, version_spec) pairs into a compact paragraph."""
    if not pairs:
        return "### Required Packages\n(none detected)"
    items = [f"{n}{v}" if v else n for n, v in pairs]
    # 10 packages per line keeps it readable but compact
    lines = [", ".join(items[i:i + 10]) for i in range(0, len(items), 10)]
    return "### Required Packages\n" + "\n".join(lines)


# --- per-format parsers ---

def _parse_requirements_txt(content: str) -> list[tuple[str, str]]:
    pairs = []
    for line in content.splitlines():
        line = line.split("#")[0].strip()
        if not line or line.startswith("-"):
            continue
        m = re.match(r"^([A-Za-z0-9][A-Za-z0-9._-]*(?:\[[^\]]*\])?)\s*([><=!~^][^\s#]*)?", line)
        if m:
            pairs.append((m.group(1), m.group(2) or ""))
    return pairs


def _parse_poetry_lock(content: str) -> list[tuple[str, str]]:
    pairs = []
    for m in re.finditer(
        r'\[\[package\]\][^\[]*?name\s*=\s*"([^"]+)"[^\[]*?version\s*=\s*"([^"]+)"',
        content, re.DOTALL,
    ):
        pairs.append((m.group(1), f"=={m.group(2)}"))
    return pairs


def _parse_uv_lock(content: str) -> list[tuple[str, str]]:
    # Same TOML-block structure as poetry.lock
    return _parse_poetry_lock(content)


def _parse_cargo_lock(content: str) -> list[tuple[str, str]]:
    return _parse_poetry_lock(content)   # identical [[package]] structure


def _parse_package_lock_json(content: str) -> list[tuple[str, str]]:
    try:
        data = json.loads(content)
        deps: dict[str, str] = {}
        if "packages" in data:                          # v2/v3
            for key, val in data["packages"].items():
                if key:
                    name = key.split("node_modules/")[-1]
                    deps[name] = val.get("version", "")
        elif "dependencies" in data:                    # v1
            for name, val in data["dependencies"].items():
                deps[name] = val.get("version", "")
        return [(n, f"=={v}" if v else "") for n, v in sorted(deps.items())]
    except Exception:
        return []


def _parse_yarn_lock(content: str) -> list[tuple[str, str]]:
    pairs, seen = [], set()
    for m in re.finditer(
        r'^"?(@?[^@\s"]+)@[^":\n]*"?:\s*\n\s+version\s+"([^"]+)"',
        content, re.MULTILINE,
    ):
        key = m.group(1)
        if key not in seen:
            seen.add(key)
            pairs.append((key, f"=={m.group(2)}"))
    return pairs


def _parse_pnpm_lock(content: str) -> list[tuple[str, str]]:
    pairs, seen = [], set()
    for m in re.finditer(
        r"^\s+/?(@?[^@\s/]+(?:/[^@\s/]+)?)@([^:\s]+):",
        content, re.MULTILINE,
    ):
        key = (m.group(1), m.group(2))
        if key not in seen:
            seen.add(key)
            pairs.append((m.group(1), f"=={m.group(2)}"))
    return pairs


def _parse_gemfile_lock(content: str) -> list[tuple[str, str]]:
    pairs, in_gems = [], False
    for line in content.splitlines():
        if line.strip() == "GEM":
            in_gems = True
            continue
        if in_gems:
            if line == "" or (line and not line[0].isspace()):
                in_gems = False
                continue
            m = re.match(r"^    ([a-z][a-z0-9_-]*)\s+\(([^)]+)\)", line)
            if m:
                pairs.append((m.group(1), f"=={m.group(2)}"))
    return pairs


def _parse_composer_lock(content: str) -> list[tuple[str, str]]:
    try:
        data = json.loads(content)
        pairs = []
        for section in ("packages", "packages-dev"):
            for pkg in data.get(section, []):
                pairs.append((pkg.get("name", ""), f"=={pkg.get('version', '')}"))
        return pairs
    except Exception:
        return []


def _parse_pipfile_lock(content: str) -> list[tuple[str, str]]:
    try:
        data = json.loads(content)
        pairs = []
        for section in ("default", "develop"):
            for name, info in data.get(section, {}).items():
                pairs.append((name, info.get("version", "")))
        return pairs
    except Exception:
        return []


def _parse_mix_lock(content: str) -> list[tuple[str, str]]:
    pairs = []
    for m in re.finditer(r'"([^"]+)":\s*\{[^}]*:version,\s*"([^"]+)"', content):
        pairs.append((m.group(1), f"=={m.group(2)}"))
    return pairs


def _parse_gemfile(content: str) -> list[tuple[str, str]]:
    pairs = []
    for m in re.finditer(r"""gem\s+['"]([^'"]+)['"]\s*(?:,\s*['"]([^'"]+)['"])?""", content):
        pairs.append((m.group(1), m.group(2) or ""))
    return pairs


def _parse_pipfile(content: str) -> list[tuple[str, str]]:
    pairs, in_section = [], False
    for line in content.splitlines():
        stripped = line.strip()
        if re.match(r"^\[(packages|dev-packages)\]", stripped, re.IGNORECASE):
            in_section = True
            continue
        if stripped.startswith("["):
            in_section = False
            continue
        if in_section and "=" in stripped and not stripped.startswith("#"):
            name, _, ver = stripped.partition("=")
            ver = ver.strip().strip('"').strip("'")
            pairs.append((name.strip(), f"=={ver}" if ver and ver != "*" else ""))
    return pairs


def _parse_go_mod(content: str) -> list[tuple[str, str]]:
    pairs = []
    # single-line: require module/path v1.2.3
    for m in re.finditer(r"^require\s+(\S+)\s+(v\S+)", content, re.MULTILINE):
        pairs.append((m.group(1), f"=={m.group(2)}"))
    # block: require (\n  mod v1.2.3 // indirect\n)
    for block in re.finditer(r"require\s*\(([^)]+)\)", content, re.DOTALL):
        for m in re.finditer(r"^\s+(\S+)\s+(v\S+)", block.group(1), re.MULTILINE):
            if not m.group(1).startswith("//"):
                pairs.append((m.group(1), f"=={m.group(2)}"))
    return pairs


def _parse_go_sum(content: str) -> list[tuple[str, str]]:
    """
    go.sum: one entry per module, latest version only.
    Skips /go.mod checksum lines (v[^space/]+ excludes the /go.mod suffix).
    When the same module appears at multiple versions, last occurrence wins
    (go.sum lists them in encountered order, so last ≈ highest used).
    """
    seen: dict[str, str] = {}
    for m in re.finditer(r"^(\S+)\s+(v[^\s/]+)\s+h1:", content, re.MULTILINE):
        seen[m.group(1)] = m.group(2)   # overwrite → last version kept
    return [(mod, f"=={ver}") for mod, ver in sorted(seen.items())]


_LOCKFILE_PARSERS = {
    "package-lock.json": _parse_package_lock_json,
    "yarn.lock":         _parse_yarn_lock,
    "pnpm-lock.yaml":   _parse_pnpm_lock,
    "poetry.lock":       _parse_poetry_lock,
    "cargo.lock":        _parse_cargo_lock,
    "gemfile.lock":      _parse_gemfile_lock,
    "uv.lock":           _parse_uv_lock,
    "composer.lock":     _parse_composer_lock,
    "pipfile.lock":      _parse_pipfile_lock,
    "mix.lock":          _parse_mix_lock,
}


def extract_dependencies(content: str, filename: str) -> str | None:
    """
    If *filename* is a dependency/lockfile, return a compact
    '### Required Packages\\n...' string.  Returns None otherwise.
    """
    fname_lower = filename.lower()

    # requirements*.txt / requirements*.in
    if re.match(r"requirements.*\.(txt|in)$", fname_lower):
        return _fmt_deps(_parse_requirements_txt(content))

    if filename == "Pipfile":
        return _fmt_deps(_parse_pipfile(content))

    if filename == "Gemfile":
        return _fmt_deps(_parse_gemfile(content))

    if filename == "go.mod":
        return _fmt_deps(_parse_go_mod(content))

    if filename == "go.sum":
        return _fmt_deps(_parse_go_sum(content))

    if fname_lower in _LOCKFILE_PARSERS:
        return _fmt_deps(_LOCKFILE_PARSERS[fname_lower](content))

    return None


# ---------------------------------------------------------------------------
# Directory structure renderer (unchanged from original)
# ---------------------------------------------------------------------------

def get_repo_structure(root_dir: str) -> str:
    lines = []

    def _build_tree(current_dir, prefix=""):
        try:
            items = sorted(os.listdir(current_dir))
        except Exception:
            return
        valid_items = [i for i in items if not is_ignored(os.path.join(current_dir, i), root_dir)]
        for idx, item in enumerate(valid_items):
            item_path = os.path.join(current_dir, item)
            is_last = idx == len(valid_items) - 1
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{item}")
            if os.path.isdir(item_path):
                new_prefix = prefix + ("    " if is_last else "│   ")
                _build_tree(item_path, new_prefix)

    lines.append(".")
    _build_tree(root_dir)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Prioritised file collection
# ---------------------------------------------------------------------------

def collect_prioritized_files(root_dir: str) -> list[tuple[str, str]]:
    """
    Walk root_dir, filter with is_ignored, score, and return
    [(rel_path, full_path)] sorted by (tier, depth, name).
    """
    candidates = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = sorted(d for d in dirs if d not in DEFAULT_IGNORE_DIRS)
        for filename in files:
            full_path = os.path.join(root, filename)
            if is_ignored(full_path, root_dir):
                continue
            rel_path = os.path.relpath(full_path, root_dir)
            candidates.append((score_file(rel_path), rel_path, full_path))

    candidates.sort()
    return [(rel_path, full_path) for _, rel_path, full_path in candidates]


# ---------------------------------------------------------------------------
# Core ingest logic
# ---------------------------------------------------------------------------

def run_ingest(args):
    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    for repo_str in args.repo:
        user_repo, ref = get_repo_id(repo_str)
        print(f"--- Processing {user_repo} ---")

        prefix = args.prefix if args.prefix else user_repo.replace("/", "_") + "_"

        with tempfile.TemporaryDirectory() as temp_dir:
            sha = clone_repo(user_repo, ref, temp_dir)
            if not sha:
                sha = download_zip(user_repo, ref, temp_dir)

            stats = {
                "total_scanned": 0,
                "included": 0,
                "skipped_rule": 0,
                "skipped_size": 0,
                "skipped_budget": 0,
                "extracted_structural": 0,
                "extracted_deps": 0,
                "languages": {},
                "top_files": [],
            }

            # --- Extract README (ground truth; not fed to the model) ---
            readme_content = ""
            for f in os.listdir(temp_dir):
                if f.lower().startswith("readme") and os.path.isfile(os.path.join(temp_dir, f)):
                    with open(os.path.join(temp_dir, f), "r", encoding="utf-8", errors="ignore") as rf:
                        readme_content = rf.read()
                    break
            if not readme_content:
                readme_content = "(No README.md found in repository)"

            readme_name = f"{prefix}README.md"
            parsed_name = f"{prefix}parsed_code.txt"
            with open(os.path.join(out_dir, readme_name), "w", encoding="utf-8") as f:
                f.write(readme_content)

            # --- Priority-ordered file collection ---
            ordered = collect_prioritized_files(temp_dir)
            stats["total_scanned"] = len(ordered)

            output_data = []
            token_budget = args.budget_tokens
            basename_copies: dict[str, int] = {}  # deduplicate repeated manifests

            for rel_path, full_path in ordered:
                filename = os.path.basename(full_path)
                size = os.path.getsize(full_path)

                # Deduplicate: repos that repeat the same manifest filename across
                # many version subdirectories (e.g. 12 Dockerfiles) are capped.
                if filename in PRIORITY_MANIFESTS:
                    basename_copies[filename] = basename_copies.get(filename, 0) + 1
                    if basename_copies[filename] > MAX_COPIES_PER_BASENAME:
                        stats["skipped_budget"] += 1
                        continue

                is_config = filename in CONFIG_FILES
                byte_cap = args.max_bytes * 5 if is_config else args.max_bytes

                if size > byte_cap:
                    stats["skipped_size"] += 1
                    continue

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as fh:
                        raw_lines = fh.readlines()
                except Exception:
                    stats["skipped_rule"] += 1
                    continue

                num_lines = len(raw_lines)

                # Per-file line cap (config files exempt)
                if num_lines > args.max_lines and not is_config:
                    stats["skipped_size"] += 1
                    continue

                raw_content = "".join(raw_lines)

                # --- Dependency extraction (highest priority) ---
                dep_content = extract_dependencies(raw_content, filename)
                if dep_content is not None:
                    content = dep_content
                    was_extracted = True
                    stats["extracted_deps"] += 1

                # --- Structural extraction (source files) ---
                elif (
                    not args.no_ast
                    and (num_lines > AST_THRESHOLD_LINES or (
                        os.path.splitext(filename)[1].lower() == ".py"
                        and os.path.isfile(os.path.splitext(full_path)[0] + ".pyi")
                    ))
                    and (
                        os.path.splitext(filename)[1].lower() in STRUCTURAL_EXTENSIONS
                        or os.path.splitext(filename)[1].lower() in CTAGS_EXTENSIONS
                    )
                    and filename not in PRIORITY_MANIFESTS
                ):
                    content, was_extracted = extract_structure(raw_content, filename, full_path)
                    if was_extracted:
                        stats["extracted_structural"] += 1
                    else:
                        content = raw_content

                else:
                    content = raw_content
                    was_extracted = False

                # --- Token budget check ---
                est = _estimate_tokens(content)
                if token_budget is not None and est > token_budget:
                    stats["skipped_budget"] += 1
                    continue
                if token_budget is not None:
                    token_budget -= est

                # --- Collect ---
                ext = os.path.splitext(filename)[1].lower() or "no_ext"
                stats["languages"][ext] = stats["languages"].get(ext, 0) + 1
                stats["included"] += 1
                stats["top_files"].append((size, rel_path))

                if dep_content is not None:
                    extraction_note = " [deps]"
                elif was_extracted:
                    extraction_note = " [structural]"
                else:
                    extraction_note = ""
                output_data.append(
                    f"---\nFile: {rel_path}\n"
                    f"Size: {size} bytes\n"
                    f"Lines: {num_lines}{extraction_note}\n"
                    f"---\n{content}\n"
                )

            # --- Assemble output ---
            stats["top_files"].sort(key=lambda x: x[0], reverse=True)
            stats["top_files"] = stats["top_files"][:15]

            header_lines = [
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
                f"Files skipped by budget: {stats['skipped_budget']}",
                f"Files with structural extraction: {stats['extracted_structural']}",
                f"Files with dependency extraction: {stats['extracted_deps']}",
                f"Detected languages count: {len(stats['languages'])}",
                "Top 15 largest included files:",
            ]
            for s, p in stats["top_files"]:
                header_lines.append(f"  {s} bytes - {p}")
            header_lines.append("-----------------------")

            full_content = "\n".join(header_lines) + "\n\n" + "\n".join(output_data)
            tokens = count_tokens(full_content)
            token_line = f"Tokens: {tokens if tokens >= 0 else 'N/A (tiktoken not installed)'}"
            final_output = f"{token_line}\n{full_content}"

            with open(os.path.join(out_dir, parsed_name), "w", encoding="utf-8") as f:
                f.write(final_output)

            print(
                f"Ingest complete for {user_repo}. "
                f"Output: {parsed_name} "
                f"({tokens} tokens, {stats['included']} files, "
                f"{stats['extracted_structural']} structural, "
                f"{stats['extracted_deps']} dep-extracted)"
            )


# ---------------------------------------------------------------------------
# Chunk command (unchanged from original, preserves format compatibility)
# ---------------------------------------------------------------------------

def run_chunk(args):
    input_file = os.path.abspath(args.input)
    out_file = os.path.abspath(args.out)

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    blocks = content.split("\n---\nFile: ")
    if len(blocks) < 2:
        print("No files found in the input file or format is invalid.")
        return

    file_blocks = blocks[1:]
    chunks = []
    chunk_size_chars = args.chunk_tokens * 4
    overlap_chars = args.overlap * 4

    for block in file_blocks:
        full_block = "File: " + block
        try:
            header_lines = full_block.split("\n", 4)
            if len(header_lines) < 5:
                continue
            file_path = header_lines[0].replace("File: ", "").strip()
            file_content = header_lines[4]

            if len(file_content) <= chunk_size_chars:
                chunks.append({"file": file_path, "chunk": file_content.strip(), "chunk_id": 0})
            else:
                start = 0
                chunk_id = 0
                while start < len(file_content):
                    end = start + chunk_size_chars
                    chunks.append({
                        "file": file_path,
                        "chunk": file_content[start:end].strip(),
                        "chunk_id": chunk_id,
                    })
                    if end >= len(file_content):
                        break
                    start = end - overlap_chars
                    chunk_id += 1
        except Exception as e:
            print(f"Error parsing block: {e}")
            continue

    os.makedirs(os.path.dirname(out_file) or ".", exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c) + "\n")

    print(f"Chunking complete. {len(chunks)} chunks written to {out_file}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Repo Ingest CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- ingest ---
    ingest_parser = subparsers.add_parser("ingest", help="Ingest one or more repositories")
    ingest_parser.add_argument("repo", nargs="+", help="GitHub repo(s) (user/repo[/branch-or-commit])")
    ingest_parser.add_argument("--out", default="./out", help="Output directory")
    ingest_parser.add_argument("--prefix", default="", help="Override default prefix (sanitized_repo_name_)")
    ingest_parser.add_argument("--max-lines", type=int, default=3000,
                               help="Per-file line cap (config files exempt)")
    ingest_parser.add_argument("--max-bytes", type=int, default=2_000_000,
                               help="Per-file byte cap (config files get 5x)")
    ingest_parser.add_argument("--budget-tokens", type=int, default=DEFAULT_BUDGET_TOKENS,
                               help=f"Total token budget for parsed output (default {DEFAULT_BUDGET_TOKENS}). "
                                    "Tier-0 manifests always bypass this limit.")
    ingest_parser.add_argument("--no-ast", action="store_true",
                               help="Disable structural extraction; always include raw file content")

    # --- chunk ---
    chunk_parser = subparsers.add_parser("chunk", help="Chunk the parsed code")
    chunk_parser.add_argument("input", help="Path to parsed_code.txt")
    chunk_parser.add_argument("--out", default="./out/chunks.jsonl", help="Output JSONL file")
    chunk_parser.add_argument("--chunk-tokens", type=int, default=800,
                               help="Approximate tokens per chunk")
    chunk_parser.add_argument("--overlap", type=int, default=80,
                               help="Approximate overlap tokens")

    args = parser.parse_args()

    if args.command == "ingest":
        run_ingest(args)
    elif args.command == "chunk":
        run_chunk(args)


if __name__ == "__main__":
    main()
