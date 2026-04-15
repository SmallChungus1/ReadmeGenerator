```markdown
# Click

## Description

Click is a Python package for creating beautiful command-line interfaces in a composable way with as little code as necessary. It's built to be flexible and many popular Python frameworks and libraries are built on top of it.

## Features

*   **Composable:** Easily combine options, arguments, and commands to build complex CLIs.
*   **Automatic Help Generation:**  Generates help pages automatically.
*   **Type Conversion:** Handles type conversion for command-line arguments.
*   **Nesting Commands:** Supports creating nested command structures.
*   **Environment Variable Support:** Integrates with environment variables.
*   **Customizable Prompts:**  Allows for interactive prompts.
*   **Extensible:** Provides options for customization and extension.
*   **Built-in Shell Completion:**  Supports shell completion for popular shells.

## Installation

```bash
pip install click
```

## Usage

Here's a basic example of a Click application:

```python
import click

@click.command()
@click.option('--name', default='World', help='Who to greet.')
def hello(name):
    """A simple program that greets NAME."""
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
```

To run this example:

1.  Save the code as a Python file (e.g., `hello.py`).
2.  Run it from the command line:

```bash
python hello.py
python hello.py --name "Your Name"
python hello.py --help
```

## Development

This repository contains the source code for the Click library.

*   **Dependencies:** Managed using `uv`.
*   **Testing:** Uses `pytest`.
*   **Documentation:** Built using Sphinx.
*   **Continuous Integration:** Utilizes GitHub Actions for testing and publishing.
*   **Pre-commit hooks:**  Used to ensure code quality and consistency.

### Contributing

Contributions are welcome!  Please refer to the project's contribution guidelines for details.

### Build and Test

1.  **Install dependencies:**
    ```bash
    uv install
    ```

2.  **Run tests:**
    ```bash
    pytest
    ```

3.  **Build documentation:**
    ```bash
    cd docs
    make html
    ```

### Workflow

*   **`pre-commit.yaml`:** Contains pre-commit hooks for linting, formatting, and other checks.
*   **`tests/`:** Directory containing all unit and integration tests.
*   **`examples/`:**  Directory containing example applications demonstrating how to use Click.
*  **`.devcontainer/`:** configuration files for a development container, ensuring a consistent development environment.
*   **`docs/`:** Directory containing the Sphinx documentation for the library.

## License

This project is licensed under the terms of the [BSD 3-Clause License](LICENSE.txt).