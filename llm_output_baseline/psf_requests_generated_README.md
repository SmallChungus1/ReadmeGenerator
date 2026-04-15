# requests

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-lightgrey.svg)
![Build Status](https://img.shields.io/github/workflow/status/psf/requests/ci)
![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)

> **Python HTTP for Humans**

`requests` is a simple, elegant, and powerful HTTP library for Python. It simplifies making HTTP requests with a clean, readable API, handling authentication, cookies, redirects, and more—without requiring you to write low-level socket code.

Built for human beings, not machines, `requests` makes it easy to interact with web APIs, scrape data, automate workflows, and build robust networked applications.

---

## Description

`requests` is a Python library that provides a simple and intuitive interface for making HTTP requests. It abstracts away the complexity of low-level networking, allowing developers to focus on their application logic rather than the intricacies of HTTP protocols.

Whether you're fetching data from a REST API, submitting a form, or downloading a file, `requests` offers a consistent, easy-to-use API that works seamlessly across Python versions.

The library is widely adopted, trusted, and maintained by the Python Software Foundation (PSF), with a strong community and comprehensive documentation.

---

## Features

- ✅ **Simple & readable API**: Make GET, POST, PUT, PATCH, DELETE, and OPTIONS requests with minimal code.
- ✅ **Automatic handling of redirects**: Follows HTTP redirects automatically (with configurable limits).
- ✅ **Built-in support for cookies**: Manages session cookies and stores them automatically.
- ✅ **Authentication support**: Handles basic, digest, and proxy authentication out of the box.
- ✅ **Robust error handling**: Comprehensive exceptions for common network issues (e.g., timeouts, SSL errors).
- ✅ **Support for JSON and form data**: Easily send JSON payloads or multipart form data.
- ✅ **Flexible headers and custom request settings**: Customize request headers, user agents, and more.
- ✅ **Session objects**: Reuse connections and maintain state across multiple requests.
- ✅ **Built-in support for proxies and SSL certificates**.
- ✅ **Extensible with hooks**: Customize request/response behavior using hooks.
- ✅ **Cross-platform compatibility**: Works on all major operating systems.

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

- **Python 3.10 or later** (minimum)
- **urllib3 ≥ 1.26, < 3**
- **idna ≥ 2.5, < 4**
- **certifi ≥ 2023.5.7**

> Note: `requests` is compatible with both CPython and PyPy.

---

## Installation

Install `requests` using `pip`:

```bash
pip install requests
```

For development (with tests and documentation), install the dev version:

```bash
pip install -e .
```

Or, if you're building from source:

```bash
pip install requests
```

> The project uses `setuptools` for packaging and `pyproject.toml` for modern Python build configuration.

---

## Usage

Here’s a simple example of how to use `requests` to make a GET request:

```python
import requests

response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.json())
```

### Making a POST Request with JSON Data

```python
import requests

data = {"name": "John", "age": 30}
response = requests.post("https://httpbin.org/post", json=data)
print(response.json())
```

### Using a Session for Reusable Connections

```python
import requests

session = requests.Session()
session.get("https://httpbin.org/headers")
session.post("https://httpbin.org/post", data={"key": "value"})
```

### Handling Authentication

```python
import requests

response = requests.get("https://httpbin.org/headers", auth=("user", "pass"))
print(response.status_code)
```

### Setting Custom Headers

```python
import requests

headers = {"User-Agent": "MyApp/1.0"}

response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.json())
```

### Error Handling

```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

try:
    response = requests.get("https://httpbin.org/status/404", timeout=5)
    response.raise_for_status()
except Timeout:
    print("Request timed out")
except ConnectionError:
    print("Failed to connect to server")
except RequestException as e:
    print(f"An error occurred: {e}")
```

> For full documentation, visit the [official documentation](https://requests.readthedocs.io).

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your help is appreciated.

### How to Contribute

1. **Fork the repository** on [GitHub](https://github.com/psf/requests).
2. **Create a new feature branch** for your changes.
3. **Write tests** to cover your changes.
4. **Submit a pull request** with a clear description of what you've done.

### Reporting Issues

Found a bug or have a feature request? Please open an issue on the [issue tracker](https://github.com/psf/requests/issues).

> We follow a strict code review process to ensure quality and maintainability.

### Code Style

- Use **PEP 8** for Python code.
- Use **Ruff** for linting and formatting (configured in `.pre-commit-config.yaml`).
- Use **Black** for formatting (configured in `pyproject.toml`).

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Kenneth Reitz** – Original creator and lead maintainer  
  Email: `me@kennethreitz.org`  
  Website: [kennethreitz.org](https://kennethreitz.org)

- **Ian Stapleton Cordasco** – Current maintainer  
  Email: `graffatcolmingov@gmail.com`

- **Nate Prewitt** – Maintainer  
  Email: `nate.prewitt@gmail.com`

For questions, feedback, or to report issues, please reach out via the [issue tracker](https://github.com/psf/requests/issues) or through the [official community channels](https://github.com/psf/requests/discussions).

> 🚀 `requests` is maintained by the Python Software Foundation (PSF) and is a cornerstone of the Python ecosystem.