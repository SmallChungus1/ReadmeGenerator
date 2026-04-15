# Requests

## Description

**Requests** is a simple, elegant, and powerful HTTP library for Python, designed specifically for human beings. It simplifies making HTTP requests with a clean, intuitive API, enabling developers to send GET, POST, PUT, DELETE, and other HTTP methods with minimal code. Built on top of `urllib3`, it provides robust features like automatic SSL verification, connection pooling, and support for cookies, authentication, and redirects.

Requests is widely adopted across the Python ecosystem and is the go-to choice for any Python project requiring HTTP communication.

## Features

- ✅ **Simple and Intuitive API** – Send HTTP requests with minimal code using `requests.get()`, `requests.post()`, etc.
- ✅ **Automatic SSL Verification** – Secure connections with built-in certificate validation.
- ✅ **Support for Cookies and Authentication** – Handle session cookies and various authentication schemes (Basic, Digest).
- ✅ **Built-in Error Handling** – Comprehensive exception hierarchy for network errors, timeouts, and invalid responses.
- ✅ **Support for Headers, Parameters, and Data** – Easily pass headers, query parameters, form data, or JSON payloads.
- ✅ **Response Parsing** – Automatically decode responses as JSON or text with proper encoding handling.
- ✅ **Redirect Handling** – Automatically follow redirects with configurable maximum redirects.
- ✅ **Session Management** – Reuse connections and maintain cookies across multiple requests.
- ✅ **Proxy Support** – Configure proxies for requests and support SOCKS protocols.
- ✅ **Custom Headers and Hooks** – Extend functionality with request/response hooks.
- ✅ **Cross-Platform Compatibility** – Works seamlessly on all major operating systems.

## Installation

Install the latest version of Requests using `pip`:

```bash
pip install requests
```

For development purposes, install the package with additional test dependencies:

```bash
pip install -r requirements-dev.txt
```

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

data = {'name': 'Alice', 'age': 30}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())
```

### Using a Session for Reusable Connections

```python
import requests

session = requests.Session()
session.get('https://httpbin.org/headers')
session.post('https://httpbin.org/post', data={'key': 'value'})

# Cookies are automatically maintained across requests
```

### Handling Authentication

```python
import requests

response = requests.get('https://httpbin.org/headers', auth=('user', 'password'))
print(response.status_code)
```

### Custom Headers and Query Parameters

```python
import requests

headers = {'User-Agent': 'MyApp/1.0'}
params = {'page': 1, 'limit': 10}

response = requests.get(
    'https://httpbin.org/get',
    headers=headers,
    params=params
)
print(response.url)  # Shows the full URL with query parameters
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

> 💡 **Note**: The `requests` library is compatible with Python 3.10 and above. Older versions are no longer supported.

For more detailed documentation, visit the official [Requests Documentation](https://requests.readthedocs.io).