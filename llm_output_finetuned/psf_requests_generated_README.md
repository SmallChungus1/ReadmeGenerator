# Requests

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-lightgrey.svg)
![Build Status](https://img.shields.io/github/workflow/status/psf/requests/ci/main)
![Documentation](https://img.shields.io/badge/documentation-readme-blue)

> **Python HTTP for Humans**

Requests is a simple, elegant, and powerful HTTP library for Python. It simplifies making HTTP requests by abstracting away the complexity of low-level networking, providing a clean and intuitive API that makes it easy to send requests, handle responses, and manage common HTTP operations.

Built with simplicity and reliability in mind, Requests is the go-to library for Python developers who want to interact with web APIs, scrape data, or automate interactions with web services — all without writing boilerplate code.

---

## Description

Requests is a Python library that makes it easy to send HTTP/1.1 requests. It provides a user-friendly interface for making GET, POST, PUT, DELETE, and other HTTP methods, with built-in support for:

- Automatic handling of redirects
- Cookie management
- Authentication (basic, digest, and more)
- JSON parsing
- SSL/TLS verification
- Content encoding and decoding
- Request and response hooks

Whether you're building a simple script to fetch data from a public API or integrating with a complex web service, Requests gives you the tools you need — without the complexity.

---

## Features

- ✅ **Simple & Intuitive API** – Send HTTP requests with just a few lines of code.
- ✅ **Automatic Redirect Handling** – Follows redirects automatically and manages them safely.
- ✅ **Built-in JSON Support** – Automatically parse JSON responses with `.json()` method.
- ✅ **Cookie Management** – Handles cookies automatically and stores them in a session.
- ✅ **Authentication Support** – Supports basic, digest, and proxy authentication.
- ✅ **SSL/TLS Verification** – Secure connections with optional certificate validation.
- ✅ **Robust Error Handling** – Clear exceptions for common network issues.
- ✅ **Extensible with Hooks** – Customize request/response behavior via hooks.
- ✅ **Cross-Platform Compatibility** – Works on all major operating systems.
- ✅ **Active Community & Maintenance** – Regular updates and strong community support.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites

Requests requires Python 3.10 or later. It also depends on the following external packages:

- `urllib3` ≥ 1.26
- `idna` ≥ 2.5
- `charset_normalizer` ≥ 2.0

These dependencies are automatically managed via `pip` and included in the project’s `pyproject.toml`.

> ⚠️ **Note**: Python 2.7 and 3.8–3.9 are no longer supported. Requests requires **Python 3.10+**.

---

## Installation

Install Requests using `pip`:

```bash
pip install requests
```

For development (e.g., contributing or testing):

```bash
pip install -e .
```

To install with additional features like SOCKS support:

```bash
pip install "requests[socks]"
```

To enable chardet-based encoding detection (for Python 3):

```bash
pip install "requests[use_chardet_on_py3]"
```

---

## Usage

Here’s how to use Requests in your Python scripts:

### 1. Make a GET Request

```python
import requests

response = requests.get("https://httpbin.org/json")
print(response.json())
```

### 2. Make a POST Request with JSON Data

```python
import requests

data = {"name": "Alice", "age": 30}
response = requests.post("https://httpbin.org/post", json=data)
print(response.status_code)
print(response.json())
```

### 3. Send a Request with Headers and Authentication

```python
import requests

headers = {"User-Agent": "MyApp/1.0"}
auth = ("username", "password")

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers,
    auth=auth
)

print(response.headers)
```

### 4. Handle Errors and Status Codes

```python
import requests

try:
    response = requests.get("https://httpbin.org/status/404")
    response.raise_for_status()  # Raises an HTTPError for bad responses
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
```

### 5. Use Sessions for Persistent Connections

```python
import requests

session = requests.Session()
session.get("https://httpbin.org/cookies/set/sessionid/12345")
response = session.get("https://httpbin.org/cookies")
print(response.json())
```

> 💡 **Tip**: Sessions automatically manage cookies and reuses connections for better performance.

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding documentation, or proposing a new feature, your input is valuable.

### How to Contribute

1. **Fork the repository** on [GitHub](https://github.com/psf/requests).
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/new-auth-method
   ```
3. **Commit your changes** with clear, descriptive messages.
4. **Run the tests**:
   ```bash
   make test
   ```
5. **Submit a pull request** with a detailed description of your changes.

### Reporting Issues

If you find a bug or have a feature request, please open an issue in the [Requests GitHub Issues](https://github.com/psf/requests/issues) repository.

> 📚 For detailed contribution guidelines, see the [Contributors Guide](https://requests.readthedocs.io/en/latest/dev/contributing.html).

---

## License

Requests is licensed under the **Apache License 2.0**.

This means you can:

- Use it freely in commercial or open-source projects
- Modify and distribute it
- Use it in any context, including closed-source software

For full details, see the [LICENSE](LICENSE) file.

---

## Contact / Authors

**Primary Author**:  
Kenneth Reitz  
📧 me@kennethreitz.org  
🔗 [GitHub Profile](https://github.com/kennethreitz)

**Maintainers**:  
- Ian Stapleton Cordasco (`graffatcolmingov@gmail.com`)  
- Nate Prewitt (`nate.prewitt@gmail.com`)

**Project Home**:  
🔗 [https://requests.readthedocs.io](https://requests.readthedocs.io)

**GitHub Repository**:  
🔗 [https://github.com/psf/requests](https://github.com/psf/requests)

**Issue Tracker**:  
🔗 [https://github.com/psf/requests/issues](https://github.com/psf/requests/issues)

For questions or feedback, feel free to open an issue or reach out directly to the maintainers.