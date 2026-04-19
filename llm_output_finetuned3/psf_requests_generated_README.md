# requests

## Description
Python HTTP library for humans. Simplifies making HTTP requests with a clean, intuitive API.

## Features
- Simple and readable syntax for making HTTP requests
- Built-in support for authentication, cookies, and redirects
- Automatic handling of content encoding and decoding
- Support for various HTTP methods (GET, POST, PUT, DELETE, etc.)
- Configurable timeouts and connection settings
- Integration with urllib3 for low-level HTTP operations
- Comprehensive error handling with clear exceptions
- Support for custom headers, form data, and JSON payloads

## Prerequisites / Requirements
- Python 3.10 or later
- `charset_normalizer>=2,<4`
- `idna>=2.5,<4`
- `urllib3>=1.26,<3`
- `certifi>=2023.5.7`

## Installation
```bash
pip install requests
```

## Usage
```python
import requests

# GET request
response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.text)

# POST request with JSON data
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())

# Request with custom headers
headers = {'User-Agent': 'MyApp/1.0'}
response = requests.get('https://httpbin.org/headers', headers=headers)

# Session for multiple requests
session = requests.Session()
session.get('https://httpbin.org/get')
session.post('https://httpbin.org/post', data={'key': 'value'})
```

## Contributing
Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

The project uses pre-commit hooks and Ruff for code formatting and linting. Ensure your changes pass all checks before submitting.

## License
Apache-2.0

## Contact / Authors
- Kenneth Reitz (primary author)
- Ian Stapleton Cordasco
- Nate Prewitt

Project documentation: https://requests.readthedocs.io  
Source code: https://github.com/psf/requests  
Issue tracker: https://github.com/psf/requests/issues