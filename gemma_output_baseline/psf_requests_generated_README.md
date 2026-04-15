# Requests: HTTP for Humans™

[![Build Status](https://github.com/psf/requests/actions/workflows/ci.yml/badge.svg)](https://github.com/psf/requests/actions/workflows/ci.yml)
[![Code Coverage](https://codecov.io/gh/psf/requests/branch/main/graph/badge.svg)](https://codecov.io/gh/psf/requests/branch/main)
[![PyPI version](https://badge.fury.io/py/requests.svg)](https://badge.fury.io/py/requests)
[![License](https://img.shields.io/pypi/license/requests)](https://github.com/psf/requests/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/requests/badge/?version=latest)](https://requests.readthedocs.io/en/latest/)
[![Donate](https://img.shields.io/badge/Donate-via%20Open%20Collective-4169E1.svg)](https://opencollective.com/requests)


Requests is an elegant and simple HTTP library for Python, built for human beings.

-------------------

**Behold, the power of Requests**::

```python
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"type":"User"...'
>>> r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}
```

See [similar code, sans Requests](https://gist.github.com/973705).

## Description

Requests is designed to be the most human-friendly HTTP library for Python.  It simplifies the process of sending HTTP requests and handles complexities like connection pooling, authentication, and more.

## Features

*   **Simple API:**  Intuitive and easy-to-use methods for making HTTP requests.
*   **Automatic Content Decoding:** Handles character encoding automatically.
*   **Keep-Alive & Connection Pooling:**  Efficiently reuses TCP connections for performance.
*   **SSL Verification:**  Securely verifies SSL certificates.
*   **Authentication:** Supports various authentication methods (Basic, Digest, OAuth, etc.).
*   **Cookies:**  Seamlessly manages cookies.
*   **Sessions:** Persists parameters (cookies, authentication) across multiple requests.
*   **Streaming Downloads:** Efficiently download large files.
*   **Timeouts:**  Prevents requests from hanging indefinitely.
*   **Proxy Support:**  Work with proxies for increased security or access control.
*   **Multipart File Uploads:**  Easy uploading of files.

## Installation

Install the latest version using pip:

```bash
pip install requests
```

## Usage

Here's a quick example of making a GET request:

```python
import requests

response = requests.get('https://httpbin.org/get')

print(response.status_code)  # Output: 200
print(response.text)          # Output: JSON data from the server
```

### Making a POST request with data:

```python
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)

print(response.text)
```

### Using Sessions:

```python
import requests

s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
```

## Documentation

Comprehensive documentation is available at: [https://requests.readthedocs.io/](https://requests.readthedocs.io/)

## Contributing

See the [CONTRIBUTING.rst](https://github.com/psf/requests/blob/main/CONTRIBUTING.rst) file for guidelines on how to contribute to Requests.

## License

Requests is licensed under the Apache 2.0 License - see the [LICENSE](https://github.com/psf/requests/blob/main/LICENSE) file for details.

## Acknowledgements

Requests was originally created by [Kenneth Reitz](https://github.com/kennethreitz), and is now maintained by a team of dedicated contributors.  See the [AUTHORS.rst](https://github.com/psf/requests/blob/main/AUTHORS.rst) file for a complete list of contributors.

## Support

For support, please use the following resources:

*   **GitHub Issues:** [https://github.com/psf/requests/issues](https://github.com/psf/requests/issues)
*   **Stack Overflow:**  Search for existing questions or ask a new one using the `requests` tag.
*   **Open Collective:** Support the development of Requests through donations:  [https://opencollective.com/requests](https://opencollective.com/requests)