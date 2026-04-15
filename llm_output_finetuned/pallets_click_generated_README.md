# Click

## Description

**Click** is a composable command-line interface toolkit for Python. Designed to be simple, powerful, and flexible, Click enables developers to build robust command-line interfaces with minimal boilerplate. It provides a clean, intuitive API for defining commands, options, arguments, and custom types, while handling parsing, validation, and user interaction seamlessly.

Click supports advanced features such as shell completion, rich text formatting, progress bars, prompts, and interactive UI elements. It is widely used in Python projects to create intuitive and user-friendly command-line tools.

---

## Features

- ✅ **Composable Command Structure** – Build complex CLI applications using groups, commands, and subcommands.
- ✅ **Flexible Option & Argument Handling** – Define options, arguments, and parameters with rich type support.
- ✅ **Built-in Validation** – Validate user input through custom types, callbacks, and parameter constraints.
- ✅ **Shell Completion** – Generate tab-completion support for Bash, Zsh, and Fish.
- ✅ **Rich Text Formatting** – Support for colors, bold, underline, blinking, and reverse text via `click.style()`.
- ✅ **Interactive UI Elements** – Prompts, confirmations, progress bars, and pausing for enhanced user experience.
- ✅ **Cross-Platform Compatibility** – Works seamlessly on Windows, macOS, and Linux with proper console handling.
- ✅ **Extensible with Decorators** – Use `@click.command`, `@click.option`, and other decorators to define CLI behavior.
- ✅ **Testing Support** – Built-in `CliRunner` for testing command-line applications in isolation.
- ✅ **Type Hints & Static Analysis** – Full support for type annotations and integration with mypy, pyright, and ruff.

---

## Installation

Click can be installed via `pip` for use in Python projects.

```bash
pip install click
```

For development or testing purposes, install the package in editable mode:

```bash
pip install -e .
```

> **Note**: Click requires Python 3.10 or higher.

---

## Usage

Click is used by defining commands, options, and arguments using decorators. Below are examples of common patterns.

### Basic Command

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

### Command with Subcommands

```python
import click

@click.group()
def cli():
    """A simple CLI with subcommands."""
    pass

@cli.command()
@click.option("--verbose", is_flag=True, help="Enable verbose output")
def status(verbose):
    """Show current status."""
    if verbose:
        click.echo("Verbose mode enabled.")
    else:
        click.echo("Status: OK")

@cli.command()
@click.argument("filename")
def copy(filename):
    """Copy a file."""
    click.echo(f"Copying {filename}")

if __name__ == "__main__":
    cli()
```

### Using Custom Types and Validation

```python
import click
from datetime import datetime

@click.command()
@click.option("--date", type=click.DateTime(formats=["%Y-%m-%d"]), help="A valid date in YYYY-MM-DD format")
@click.option("--count", type=click.IntRange(min=1, max=100), help="A number between 1 and 100")
def example(date, count):
    click.echo(f"Date: {date}, Count: {count}")

if __name__ == "__main__":
    example()
```

### Interactive Prompts and UI

```python
import click

@click.command()
@click.option("--confirm", is_flag=True, help="Confirm action")
def action(confirm):
    if confirm:
        click.confirm("Are you sure?", abort=True)
        click.echo("Action confirmed.")
    else:
        click.echo("Action canceled.")
```

### Example: Color Output

```python
import click

@click.command()
def colors():
    for color in ["red", "green", "blue"]:
        click.echo(click.style(f"I am {color}", fg=color))
```

> 💡 **See the full examples in the `examples/` directory** for more advanced use cases like aliases, completion, validation, and term-based UI.

---

**Documentation**: [https://click.palletsprojects.com/](https://click.palletsprojects.com/)  
**Source Code**: [https://github.com/pallets/click/](https://github.com/pallets/click/)  
**Donate**: [https://palletsprojects.com/donate](https://palletsprojects.com/donate)  
**Chat**: [https://discord.gg/pallets](https://discord.gg/pallets)