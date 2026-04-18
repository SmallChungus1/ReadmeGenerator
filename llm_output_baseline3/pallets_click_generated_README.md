# Click: Composable Command Line Interface Toolkit

![Build Status](https://github.com/pallets/click/workflows/CI/badge.svg)
![Version](https://img.shields.io/pypi/v/click)
![License](https://img.shields.io/pypi/l/click)
![Python Version](https://img.shields.io/pypi/pyversions/click)

> A powerful and flexible command-line interface toolkit for Python.

---

## Description

Click is a composable command-line interface (CLI) toolkit for Python. It provides a clean, intuitive, and extensible way to build robust command-line applications. Designed with simplicity and power in mind, Click enables developers to create rich, interactive CLI tools with features like argument parsing, option handling, type validation, shell completion, and user-friendly prompts—all while maintaining a minimal and readable codebase.

Click is widely used in the Python ecosystem and serves as the foundation for many popular tools, including `pip`, `pytest`, and `flask`. Whether you're building a simple script or a complex command-line application with nested commands and dynamic behavior, Click offers the tools to make your CLI both functional and user-friendly.

---

## Features

- ✅ **Composable Design**: Build complex CLI structures using nested commands and groups.
- ✅ **Flexible Argument Parsing**: Support for options, arguments, flags, and custom types.
- ✅ **Type Validation**: Built-in support for types like integers, floats, strings, paths, and more.
- ✅ **Shell Completion**: Automatic shell completion for Bash, Zsh, and Fish.
- ✅ **User Interaction**: Built-in functions for prompts, confirmation, progress bars, and pagination.
- ✅ **Cross-Platform Compatibility**: Works seamlessly on Windows, macOS, and Linux.
- ✅ **Rich Error Handling**: Clear, user-friendly error messages with contextual help.
- ✅ **Extensible with Decorators**: Use `@click.command`, `@click.option`, and more to define CLI behavior.
- ✅ **Built-in Documentation**: Automatic help generation and formatting.

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

Click requires **Python 3.10 or higher**. It is compatible with all major operating systems.

Additional dependencies (for development and testing):
- `colorama` (for Windows console support)
- `pytest` (for testing)
- `mypy`, `pyright` (for type checking)
- `ruff` (for linting and formatting)

---

## Installation

To install Click for use in your Python project:

```bash
pip install click
```

For development (including type checking, linting, and testing):

```bash
pip install -e .
```

To install with pre-commit hooks (recommended for development):

```bash
pip install -e . --pre-commit
```

> **Note**: The project uses `uv` and `tox` for dependency management and testing. Ensure `uv` is installed via `pip install uv` before running tests or development commands.

---

## Usage

Click provides a clean and intuitive API for defining command-line interfaces. Below is a minimal example of how to create a CLI with Click.

### Basic CLI Example

```python
import click

@click.command()
@click.option("--name", prompt="Enter your name", help="Your full name")
@click.option("--age", type=int, help="Your age")
def hello(name, age):
    click.echo(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    hello()
```

### Advanced Example: Nested Commands

```python
import click

class Environment:
    def __init__(self):
        self.verbose = False

    def log(self, msg, *args):
        if args:
            msg %= args
        click.echo(msg, file=open("/dev/stderr", "w"))

@click.command(cls=ComplexCLI, context_settings=dict(auto_envvar_prefix="COMPLEX"))
@click.option("--home", type=click.Path(exists=True, file_okay=False), help="Change working directory")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose mode")
@pass_environment
def cli(ctx, verbose, home):
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home
```

> See the `examples/complex/complex/cli.py` for a full working example of nested commands and context management.

---

## Examples

The `examples/` directory contains several practical use cases demonstrating different aspects of Click:

| Example | Purpose |
|--------|---------|
| `aliases/` | Demonstrates command aliases using a configuration file. |
| `colors/` | Shows how to use `click.style()` to render colored output. |
| `completion/` | Implements shell completion for environment variables and user lists. |
| `imagepipe/` | A pipeline tool that processes images with filters (resize, blur, etc.). |
| `inout/` | Mimics Unix `cat` behavior for copying files between stdin/stdout. |
| `naval/` | A CLI for managing ships and mines (based on the "Naval Fate" example). |
| `repo/` | A simple Git-like repository manager with commands for clone, commit, and set user. |
| `termui/` | Demonstrates interactive features like progress bars, prompts, and pagination. |
| `validation/` | Shows parameter validation using callbacks and custom types. |

To run any example:

```bash
cd examples/colors
python colors.py
```

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a new feature, or improving documentation, your help is valuable.

### How to Contribute

1. **Fork the repository** on GitHub.
2. **Create a new feature branch** (e.g., `feature/add-advanced-validation`).
3. **Write tests** for new functionality.
4. **Update documentation** as needed.
5. **Submit a pull request** with a clear description of your changes.

### Reporting Issues

Bug reports and feature requests can be submitted via GitHub Issues. Please include:
- A clear description of the issue.
- Steps to reproduce.
- Expected vs. actual behavior.

### Code Style & Standards

- All code follows PEP 8 and Python best practices.
- Use `ruff` for linting and formatting.
- Run `pre-commit` hooks before committing.

> See the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines.

---

## License

Click is licensed under the **BSD-3-Clause** license. This means you are free to use, modify, and distribute the software, even commercially, as long as you include the original copyright notice and license text.

> See [LICENSE.txt](LICENSE.txt) for full details.

---

## Contact / Authors

**Project Maintainers**:  
Pallets Project Team  
Email: `contact@palletsprojects.com`

**Official Resources**:
- 📚 [Documentation](https://click.palletsprojects.com/)
- 💬 [Discord Chat](https://discord.gg/pallets)
- 🎁 [Donate](https://palletsprojects.com/donate)
- 📂 [Source Code](https://github.com/pallets/click/)

For questions or feedback, reach out to the team via the official channels. We actively monitor the community and respond promptly to issues and suggestions.

--- 

> Click is built by the [Pallets](https://palletsprojects.com/) team, a group dedicated to creating high-quality, open-source Python tools.