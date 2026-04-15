# Requests

## Description

**Requests** is a simple, elegant, and powerful HTTP library for Python, built with human beings in mind. It simplifies making HTTP requests, handling responses, and managing common web interactions—making it the go-to choice for Python developers who want to work with HTTP without the complexity of low-level networking code.

With Requests, you can easily send GET, POST, PUT, PATCH, and DELETE requests, handle cookies, manage authentication, work with JSON data, and set custom headers—all with clean, readable syntax.

## Features

- ✅ **Simple and intuitive API** for making HTTP requests (GET, POST, PUT, PATCH, DELETE, etc.)
- ✅ **Automatic JSON handling** with built-in `.json()` method
- ✅ **Cookie management** with support for persistent sessions
- ✅ **Authentication support** (Basic, Digest, and Proxy)
- ✅ **Built-in support for redirects** and automatic handling of 3xx responses
- ✅ **Robust error handling** with clear exceptions for common issues
- ✅ **Support for proxies** and custom headers
- ✅ **SSL/TLS certificate verification** using the `certifi` bundle
- ✅ **Unicode and encoding support** with automatic content decoding
- ✅ **Extensible hooks system** for custom request/response processing
- ✅ **Session-based requests** for reusing connections and preserving cookies
- ✅ **Modern Python 3.10+ compatibility** with full support for latest language features

## Installation

Install Requests using `pip`:

```bash
pip install requests
```

For development or testing environments, install the full development set:

```bash
pip install -r requirements-dev.txt
```

> **Note**: Requests requires Python 3.10 or later.

## Usage

### Making a Simple GET Request

```python
import requests

response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.json())
```

### Sending a POST Request with JSON Data

```python
import requests

data = {"name": "Alice", "age": 30}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())
```

### Using Sessions for Persistent Cookies

```python
import requests

session = requests.Session()
session.get('https://httpbin.org/cookies/set/sessionid/12345')
response = session.get('https://httpbin.org/cookies')
print(response.json())
```

### Handling Authentication

```python
import requests

response = requests.get('https://httpbin.org/headers', auth=('user', 'pass'))
print(response.json())
```

### Setting Custom Headers

```python
import requests

headers = {'User-Agent': 'MyApp/1.0', 'X-API-Key': 'abc123'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())
```

### Error Handling

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

> 💡 All examples assume you have a valid endpoint to test. For real-world usage, refer to the [official documentation](https://requests.readthedocs.io).

---

**License**: Apache-2.0  
**Homepage**: [https://requests.readthedocs.io](https://requests.readthedocs.io)  
**Source Code**: [https://github.com/psf/requests](https://github.com/psf/requests)  
**Maintainers**: Kenneth Reitz, Ian Stapleton Cordasco, Nate Prewitt