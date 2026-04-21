# Click

## Description

Click is a composable command line interface toolkit for Python. It provides a clean, intuitive way to build command-line interfaces with support for options, arguments, subcommands, and advanced features like validation, formatting, and terminal interaction.

## Features

- Composable command-line interface design
- Support for options, arguments, and subcommands
- Built-in support for shell completion (Bash, Zsh, Fish)
- Terminal UI features: prompts, progress bars, confirmation, pagination
- Type validation and conversion with custom types
- Context management and decorators for parameter passing
- Cross-platform compatibility with Windows support via `colorama`
- Integration with Python's type system and static analysis tools

## Prerequisites / Requirements

- Python 3.10 or higher
- `colorama` (required only on Windows)

## Installation

Install Click using `pip`:

```bash
pip install click
```

For development, install with additional dependencies:

```bash
pip install -e .
```

## Usage

Click is used by defining commands and options using decorators. Here is a basic example:

```python
import click

@click.command()
@click.option("--count", default=1, help="Number of times to print")
@click.option("--name", prompt="Your name", help="Your name")
def hello(count, name):
    """Print a greeting."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()
```

Run the script:

```bash
python hello.py --count 3 --name Alice
```

For more details, see the official documentation at [https://click.palletsprojects.com/](https://click.palletsprojects.com/).

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes with clear messages
4. Push to the branch and open a pull request

The project uses pre-commit hooks and automated testing via `tox`. Ensure your changes pass all tests before submitting.

## License

Click is licensed under the BSD-3-Clause license.

## Contact / Authors

Project maintained by Pallets. For questions or feedback, contact:

- Website: [https://palletsprojects.com](https://palletsprojects.com)
- Documentation: [https://click.palletsprojects.com](https://click.palletsprojects.com)
- Issue Tracker: [https://github.com/pallets/click/issues](https://github.com/pallets/click/issues)
- Chat: [https://discord.gg/pallets](https://discord.gg/pallets)