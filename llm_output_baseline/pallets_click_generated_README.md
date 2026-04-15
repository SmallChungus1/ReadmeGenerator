# Click: Composable Command Line Interface Toolkit

![Build Status](https://github.com/pallets/click/workflows/CI/badge.svg)
![Version](https://img.shields.io/pypi/v/click)
![License](https://img.shields.io/pypi/l/click)
![Python Version](https://img.shields.io/pypi/pyversions/click)

> A lightweight, composable command-line interface toolkit for Python.

---

## Description

**Click** is a powerful and flexible command-line interface (CLI) toolkit for Python. Designed to be simple yet expressive, Click enables developers to build robust, user-friendly command-line applications with minimal boilerplate code.

Unlike traditional CLI frameworks, Click emphasizes **composition** and **modularity**, allowing you to create complex command structures with intuitive syntax. It supports advanced features such as:

- Parameter validation and type conversion
- Automatic help generation
- Interactive user prompts (e.g., confirmation, input)
- Shell completion (Bash, Zsh, Fish)
- Progress bars and formatters
- Context management and state preservation

Click is widely used in Python projects ranging from simple scripts to full-featured tools, and it integrates seamlessly with Python's ecosystem.

---

## Features

- ✅ **Composable CLI design** – Build nested commands and groups with ease.
- ✅ **Type-safe parameters** – Validate input with built-in types (e.g., `int`, `float`, `path`, `choice`, `uuid`).
- ✅ **Automatic help generation** – Generate clear, formatted help text for every command.
- ✅ **Interactive user input** – Support for prompts, confirmations, and editing.
- ✅ **Shell completion** – Automatic completion for Bash, Zsh, and Fish.
- ✅ **Cross-platform compatibility** – Works on Windows, macOS, and Linux.
- ✅ **Rich formatting** – Support for colors, bold, underline, blinking, and reverse text.
- ✅ **Progress bars** – Visual feedback during long-running operations.
- ✅ **Error handling** – Clear, user-friendly error messages with context.
- ✅ **Extensible** – Custom types, validators, and decorators can be easily added.

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

Click requires **Python 3.10 or higher**.

- Python 3.10+
- A modern terminal (supports ANSI escape sequences)
- Optional: `colorama` (for Windows console color support)

> Note: Click is compatible with all major operating systems and terminal emulators.

---

## Installation

To install Click, use `pip`:

```bash
pip install click
```

For development (including testing and pre-commit hooks):

```bash
pip install -e .
```

To install with all development dependencies:

```bash
pip install -e .[dev]
```

> 💡 The `uv` tool (used in CI/CD and development) is recommended for faster dependency resolution and installation.

---

## Usage Examples

Click provides a rich set of examples in the `examples/` directory. Below are key use cases demonstrating core features.

### 1. Basic Command with Options

```python
import click

@click.command()
@click.option("--name", default="World", help="Name to greet")
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()
```

**Output:**
```
Hello, World!
```

### 2. Interactive Prompt with Confirmation

```python
import click

@click.command()
@click.option("--delete", is_flag=True, help="Delete the file")
def remove(delete):
    if delete:
        click.confirm("Are you sure you want to delete?", abort=True)
        click.echo("File deleted.")
    else:
        click.echo("No deletion.")
```

### 3. Type Validation with Custom Types

```python
import click

@click.command()
@click.option("--count", type=click.IntRange(1, 100), help="Count between 1 and 100")
def run(count):
    click.echo(f"Running {count} times.")
```

### 4. Shell Completion Example

```python
import click
from click.shell_completion import CompletionItem

def get_env_vars(ctx, param, incomplete):
    return [k for k in os.environ if incomplete in k]

@cli.command()
@click.argument("envvar", shell_complete=get_env_vars)
def show_env(envvar):
    click.echo(f"Environment variable: {envvar}")
```

### 5. Complex CLI with Context Management

```python
import os
import click

CONTEXT_SETTINGS = dict(auto_envvar_prefix="COMPLEX")

class Environment:
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        click.echo(msg, file=sys.stderr)

pass_environment = click.make_pass_decorator(Environment, ensure=True)

class ComplexCLI(click.Group):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir("commands"):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"complex.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli

@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option("--home", type=click.Path(exists=True, file_okay=False, resolve_path=True), help="Change working directory.")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose mode.")
@pass_environment
def cli(ctx, verbose, home):
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home
```

> See the full `examples/complex/` directory for a complete, working example of a complex CLI with nested commands and context management.

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a new feature, or improving documentation, your help is valuable.

### How to Contribute

1. **Fork the repository** on GitHub.
2. **Create a new feature branch** (e.g., `feature/interactive-prompts`).
3. **Make your changes** and ensure they are well-documented.
4. **Run the test suite**:
   ```bash
   tox -e py3.13
   ```
5. **Submit a pull request** with a clear description of your changes.

### Reporting Issues

Report bugs or feature requests via the [Issue Tracker](https://github.com/pallets/click/issues).

### Pre-Commit Hooks

The project uses `pre-commit` to enforce code quality. Run:

```bash
pre-commit run --all-files
```

> All changes must pass the pre-commit checks (linting, formatting, type checking).

---

## License

Click is licensed under the **BSD-3-Clause** license. See the [LICENSE.txt](LICENSE.txt) file for details.

This means you can use, modify, and distribute the software freely, even in commercial products, as long as you include the original copyright notice and disclaimer.

---

## Contact / Authors

**Project Maintainers:**  
Pallets (contact@palletsprojects.com)

**Official Resources:**
- 📚 [Documentation](https://click.palletsprojects.com/)
- 💬 [Discord Chat](https://discord.gg/pallets)
- 📢 [Donations](https://palletsprojects.com/donate)
- 📂 [Source Code](https://github.com/pallets/click/)

**Feedback?**  
Open an issue or reach out via email to `contact@palletsprojects.com`.

---

> Click is part of the **Pallets** ecosystem — a collection of open-source tools for Python developers.  
> Learn more at [palletsprojects.com](https://palletsprojects.com)