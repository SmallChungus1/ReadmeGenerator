# requests-html

## Description
A Python library that provides HTML parsing capabilities with browser-like rendering using Pyppeteer. It allows users to render web pages dynamically, execute JavaScript, and extract content in a way similar to real browsers.

## Features
- Dynamic HTML rendering via Pyppeteer
- JavaScript execution support
- Support for both synchronous and asynchronous operations
- Built-in support for user agent rotation
- Automatic handling of cookies and session state
- Methods for extracting text, links, and elements using CSS selectors and XPath
- Support for parsing HTML from URLs or raw HTML strings

## Prerequisites / Requirements
- Python 3.6 or higher
- `requests`, `pyquery`, `fake-useragent`, `parse`, `beautifulsoup4`, `w3lib`, and `pyppeteer>=0.0.14`

## Installation
```bash
pip install requests-html
```

## Usage
```python
import requests_html

# Create a session
session = requests_html.HTMLSession()

# Fetch a page
r = session.get('https://example.com')

# Render the page (executes JavaScript)
r.html.render()

# Extract text using PyQuery
text = r.html.pq('h1').text()

# Extract links
links = r.html.links()

# Access raw HTML
print(r.html.html)

# Use async operations
async def async_example():
    async_session = requests_html.AsyncHTMLSession()
    async_response = await async_session.get('https://example.com')
    await async_response.html.render()
    return async_response.html.pq('title').text()

# Run async function
# result = asyncio.run(async_example())
```

## Contributing
Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with clear, descriptive messages
4. Push to the branch and open a pull request

For documentation updates, ensure changes are reflected in the `docs/source` directory and build successfully using `make html`.

## License
MIT

## Contact / Authors
- Kenneth Reitz
- Project URL: https://github.com/psf/requests-html
- Email: me@kennethreitz.org
- Documentation: https://requests-html.readthedocs.io/