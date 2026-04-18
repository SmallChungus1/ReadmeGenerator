# requests: Python HTTP for Humans

[![Build Status](https://github.com/psf/requests/actions/workflows/ci.yml/badge.svg)](https://github.com/psf/requests/actions)
[![Version](https://img.shields.io/pypi/v/requests.svg)](https://pypi.org/project/requests/)
[![License](https://img.shields.io/pypi/l/requests.svg)](https://github.com/psf/requests/blob/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/requests.svg)](https://github.com/psf/requests)

---

## Description

**requests** is a simple, yet powerful HTTP library for Python, designed with human beings in mind. It provides a clean, intuitive interface for making HTTP requests, handling responses, managing authentication, and working with cookies, headers, and sessions—all without the complexity of lower-level networking code.

Originally developed by Kenneth Reitz, requests has become one of the most widely used and trusted HTTP clients in the Python ecosystem. It abstracts away the intricacies of TCP/IP, DNS, and TLS, allowing developers to focus on their application logic rather than the underlying network infrastructure.

Whether you're building a web scraper, consuming APIs, or integrating with third-party services, **requests** offers a robust, reliable, and easy-to-use foundation for all your HTTP needs.

---

## Features

- ✅ **Simple and readable syntax** for making GET, POST, PUT, PATCH, DELETE, and OPTIONS requests.
- ✅ **Automatic handling of redirects** and connection errors with built-in retry logic.
- ✅ **Support for authentication** (Basic, Digest, and custom) via built-in classes.
- ✅ **Cookie management** with automatic handling of cookies from responses and requests.
- ✅ **Session objects** that maintain connection pooling, cookies, and authentication state across multiple requests.
- ✅ **Built-in support for JSON** parsing and serialization.
- ✅ **Robust error handling** with clear, descriptive exceptions.
- ✅ **Flexible headers and request customization**.
- ✅ **Support for multipart form uploads**.
- ✅ **SSL/TLS with certificate verification** (via `certifi`).
- ✅ **Extensible via hooks** for custom request/response processing.
- ✅ **Cross-platform compatibility** (Windows, macOS, Linux).

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

- **Python 3.10 or later** (required due to modern Python features and security updates)
- **urllib3 ≥ 1.26, < 3** (for HTTP/1.1 and connection pooling)
- **idna ≥ 2.5, < 4** (for IDNA2008 encoding)
- **certifi ≥ 2023.5.7** (for trusted CA certificates)

> ⚠️ **Note**: The project does not support Python versions below 3.10. If you encounter compatibility issues, please upgrade your Python installation.

---

## Installation

To install the latest stable version of `requests`, use pip:

```bash
pip install requests
```

For development purposes (e.g., contributing or testing), install with development dependencies:

```bash
pip install -r requirements-dev.txt
```

To install from source (recommended for developers):

```bash
git clone https://github.com/psf/requests.git
cd requests
pip install .
```

> 💡 The project is available on [PyPI](https://pypi.org/project/requests/) and can be installed directly via pip without needing to clone the repository.

---

## Usage

### Basic GET Request

```python
import requests

response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.json())
```

### POST Request with JSON Data

```python
import requests

data = {"name": "Alice", "age": 30}
response = requests.post('https://httpbin.org/post', json=data)
print(response.status_code)
print(response.json())
```

### Using a Session (for persistent connections and cookies)

```python
import requests

session = requests.Session()
session.get('https://httpbin.org/cookies/set/sessionid/12345')
response = session.get('https://httpbin.org/cookies')
print(response.json())
```

### Handling Errors

```python
import requests

try:
    response = requests.get('https://httpbin.org/status/404')
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
```

### Custom Headers and Auth

```python
headers = {'User-Agent': 'MyApp/1.0'}
auth = ('username', 'password')

response = requests.get('https://httpbin.org/headers', headers=headers, auth=auth)
print(response.json())
```

> 📚 For full documentation, visit the [official documentation](https://requests.readthedocs.io).

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your input is valuable.

### How to Contribute

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and ensure they follow the code style and formatting guidelines.
4. **Run tests** to verify your changes don’t break existing functionality:
   ```bash
   make test
   ```
5. **Submit a pull request** with a clear description of what you've done.

### Code Style & Formatting

- The project uses **Ruff** for linting and formatting.
- All code must follow PEP 8 standards.
- Use `ruff format` to auto-format code before committing.

### Reporting Issues

If you find a bug or have a feature request, please open an issue on the [GitHub Issues page](https://github.com/psf/requests/issues).

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

**Primary Author**:  
Kenneth Reitz — [me@kennethreitz.org](mailto:me@kennethreitz.org)

**Maintainers**:  
- Ian Stapleton Cordasco — [graffatcolmingov@gmail.com](mailto:graffatcolmingov@gmail.com)  
- Nate Prewitt — [nate.prewitt@gmail.com](mailto:nate.prewitt@gmail.com)

For questions, suggestions, or support, please reach out to the maintainers or join the community on GitHub.

🔗 **Official Resources**:
- [Documentation](https://requests.readthedocs.io)
- [GitHub Repository](https://github.com/psf/requests)
- [PyPI Package](https://pypi.org/project/requests/)
- [Issue Tracker](https://github.com/psf/requests/issues)

💬 **Community**:  
Join discussions on GitHub, or follow the project on social media for updates and announcements.