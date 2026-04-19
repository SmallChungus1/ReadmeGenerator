# requests

## Description
`requests` is a Python HTTP library designed for human beings. It provides simple, intuitive methods for making HTTP requests and handling responses, with built-in support for authentication, cookies, and redirects.

## Features
- Simple and readable API for making HTTP requests (GET, POST, PUT, DELETE, etc.)
- Built-in support for cookies, authentication, and redirects
- Automatic handling of content encoding and character set decoding
- Support for streaming large responses
- Comprehensive error handling with specific exceptions for different failure modes
- Integration with urllib3 for underlying HTTP transport
- Support for custom headers, request bodies, and query parameters
- Session objects for reusing connections and maintaining state

## Prerequisites / Requirements
- Python 3.10 or later
- `urllib3` >= 1.26, < 3
- `idna` >= 2.5, < 4
- `charset_normalizer` >= 2, < 4
- `certifi` >= 2023.5.7

## Installation
Install the requests library using pip:

```bash
pip install requests
```

## Usage
Make HTTP requests using the high-level API:

```python
import requests

# GET request
response = requests.get('https://httpbin.org/get')

# POST request with JSON data
response = requests.post('https://httpbin.org/post', json={'key': 'value'})

# Custom headers and parameters
response = requests.get(
    'https://httpbin.org/headers',
    headers={'User-Agent': 'MyApp/1.0'},
    params={'page': 1, 'count': 10}
)

# Handle response
print(response.status_code)
print(response.text)
print(response.json())

# Check if request was successful
if response.ok:
    print("Request succeeded")
```

For more advanced usage, use a `Session` object to maintain connection state:

```python
import requests

session = requests.Session()
session.get('https://httpbin.org/get')
session.post('https://httpbin.org/post', data={'key': 'value'})
```

## Contributing
Contributions are welcome. Please follow the project's contribution guidelines:

1. Fork the repository on GitHub
2. Create a new feature branch
3. Commit your changes with clear, descriptive messages
4. Push to the branch and open a pull request

The project uses pre-commit hooks and Ruff for code formatting and linting. Ensure your changes pass all checks before submitting.

## License
Apache-2.0

## Contact / Authors
- Kenneth Reitz (original author)
- Ian Stapleton Cordasco (maintainer)
- Nate Prewitt (maintainer)

Project homepage: https://requests.readthedocs.io  
Source code: https://github.com/psf/requests  
Issue tracker: https://github.com/psf/requests/issues