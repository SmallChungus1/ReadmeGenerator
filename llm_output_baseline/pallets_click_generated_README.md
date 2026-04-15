# Click

## Description

Click is a composable command line interface toolkit for Python. It provides a clean, intuitive, and powerful way to build robust command-line applications. With Click, developers can define commands, arguments, options, and subcommands with ease, while leveraging built-in features like automatic help generation, argument validation, shell completion, and interactive user prompts.

Click is designed to be both simple and extensible, making it ideal for building CLI tools that range from simple scripts to complex, multi-layered applications. It supports cross-platform compatibility, including Windows, and integrates seamlessly with Python's ecosystem.

## Features

- **Composable CLI Design**: Build complex command-line interfaces using nested commands, groups, and subcommands.
- **Automatic Help Generation**: Generates detailed help text for commands and options.
- **Flexible Argument Types**: Supports custom types (e.g., file paths, dates, integers, UUIDs) and validation logic.
- **Interactive User Prompts**: Built-in functions for prompts, confirmation, progress bars, and editing.
- **Shell Completion**: Automatic shell completion for commands and arguments (Bash, Zsh, Fish).
- **Cross-Platform Support**: Works on Windows, macOS, and Linux with proper console handling.
- **Error Handling**: Comprehensive exception handling with user-friendly error messages.
- **Testing Support**: Built-in testing utilities for unit and integration testing of CLI applications.
- **Type Safety**: Full support for type hints and static analysis (e.g., mypy, pyright).
- **Extensible Decorators**: Custom decorators for options, arguments, and context management.

## Installation

To install Click, use pip:

```bash
pip install click
```

For development purposes, including tests and pre-commit hooks:

```bash
pip install -e .
```

## Usage

### Basic Command Structure

Here's a minimal example of a Click CLI:

```python
import click

@click.command()
@click.option("--name", help="Your name")
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()
```

Run with:

```bash
python hello.py --name Alice
```

Output:
```
Hello, Alice!
```

### Advanced Example: Complex CLI with Subcommands

The `examples/complex/` directory demonstrates a full-featured CLI with a custom context and subcommands:

```python
# examples/complex/complex/cli.py
import click

CONTEXT_SETTINGS = dict(auto_envvar_prefix="COMPLEX")

class Environment:
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        if self.verbose:
            self.log(msg, *args)

pass_environment = click.make_pass_decorator(Environment, ensure=True)

@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option("--home", type=click.Path(exists=True, file_okay=False, resolve_path=True), help="Changes the folder to operate on.")
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@pass_environment
def cli(ctx, verbose, home):
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home
```

This CLI supports subcommands like `init` and `status`:

```bash
python -m complex.cli --verbose --home /path/to/repo
```

### Interactive Features

Use built-in termui functions for interactive behavior:

```python
import click

@click.command()
@click.option("--confirm", is_flag=True, help="Confirm action.")
def delete(confirm):
    if confirm:
        click.confirm("Are you sure you want to delete?", abort=True)
        click.echo("Deleted successfully.")
    else:
        click.echo("Action cancelled.")
```

### Custom Types and Validation

Define custom types for input validation:

```python
import click

class URL(click.ParamType):
    name = "url"

    def convert(self, value, param, ctx):
        if not isinstance(value, tuple):
            value = urlparse.urlparse(value)
            if value.scheme not in ("http", "https"):
                self.fail(
                    f"invalid URL scheme ({value.scheme}). Only HTTP URLs are allowed",
                    param,
                    ctx,
                )
        return value

@click.command()
@click.option("--url", help="A URL", type=URL())
def cli(url):
    click.echo(f"URL: {url!r}")
```

Run with:

```bash
python cli.py --url https://example.com
```

This example validates that only HTTP/HTTPS URLs are accepted.

### Shell Completion

Enable shell completion for commands and arguments:

```python
@cli.command(help="A command to print environment variables")
@click.argument("envvar", shell_complete=get_env_vars)
def show_env(envvar):
    click.echo(f"Environment variable: {envvar}")
    click.echo(f"Value: {os.environ[envvar]}")
```

The `examples/completion/` directory provides a complete example of shell completion with environment variable and user list suggestions.

> **Note**: For more detailed examples, see the `examples/` directory in the repository.