# Requests

[![Build Status](https://github.com/psf/requests/actions/workflows/ci.yml/badge.svg)](https://github.com/psf/requests/actions/workflows/ci.yml)
[![Coverage Status](https://codecov.io/gh/psf/requests/branch/main/graph/badge.svg)](https://codecov.io/gh/psf/requests)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Description

Requests is a simple, yet elegant, HTTP library for Python. It's designed to be human-friendly and easy to use, allowing you to send HTTP requests in a more natural and Pythonic way.  It's built for interacting with web services and APIs.

## Features

*   **Simple API:**  Easy-to-use interface for making HTTP requests.
*   **Human-Friendly:** Designed with a focus on usability and readability.
*   **Automatic Content Decoding:**  Automatically decodes content based on the response headers.
*   **Keep-Alive & Connection Pooling:**  Efficiently reuses connections for improved performance.
*   **SSL Verification:**  Supports SSL certificate verification for secure connections.
*   **Proxies:**  Supports various proxy configurations.
*   **Session Support:**  Provides session objects for managing cookies and persistent settings.
*   **File Uploads:**  Easy uploading of files through multipart/form-data encoding.
*   **Authentication:**  Supports basic, digest, and other authentication methods.
*   **Streaming Downloads:**  Allows downloading large files in a streaming manner.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Python 3.10 or higher
*   `charset_normalizer>=2,<4`
*   `idna>=2.5,<4`
*   `urllib3>=1.26,<3`
*   `certifi>=2023.5.7`

## Installation

You can install Requests using pip:

```bash
pip install requests
```

## Usage

Here are some basic examples of how to use Requests:

```python
import requests

# Make a GET request
response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.text)

# Make a POST request with data
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())

# Make a request with custom headers
headers = {'User-Agent': 'My Custom Agent'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())
```

## Contributing

We welcome contributions to Requests! Please see the [CONTRIBUTING](docs/dev/contributing.rst) guide for details on how to submit bug reports, feature requests, and pull requests.

## License

Requests is licensed under the [Apache License 2.0](LICENSE).

## Contact / Authors

*   **Kenneth Reitz:** [me@kennethreitz.org](mailto:me@kennethreitz.org)
*   **Ian Stapleton Cordasco:** graffatcolmingov@gmail.com
*   **Nate Prewitt:** nate.prewitt@gmail.com

You can find the project on GitHub: [https://github.com/psf/requests](https://github.com/psf/requests)