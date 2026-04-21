# requests-html

## Description
`requests-html` is a Python library that provides HTML parsing capabilities with a simple and intuitive interface. It combines the power of `requests` for HTTP communication with browser-like rendering capabilities using `pyppeteer`, enabling dynamic content rendering and interaction similar to a real web browser.

## Features
- Renders HTML pages dynamically using a headless browser (via pyppeteer)
- Supports both synchronous and asynchronous operations
- Offers a clean, human-friendly API for parsing HTML content
- Includes built-in support for JavaScript execution, scrolling, and waiting for content
- Provides access to standard HTML parsing methods (e.g., `find`, `xpath`, `search`) via `PyQuery` and `lxml`
- Handles cookies, redirects, and user agent rotation
- Supports automatic detection and setting of encoding

## Prerequisites / Requirements
- Python 3.6 or higher
- `requests`, `pyquery`, `fake-useragent`, `parse`, `beautifulsoup4`, `w3lib`, and `pyppeteer>=0.0.14`

## Installation
Install the package using pip:

```bash
pip install requests-html
```

## Usage
### Basic Usage (Synchronous)
```python
import requests_html

session = requests_html.HTMLSession()
r = session.get('https://httpbin.org/html')

# Render the page (executes JavaScript, handles dynamic content)
r.html.render()

# Access parsed content
print(r.html.find('h1')[0].text)
print(r.html.find('a', first=True).attrs['href'])
```

### Asynchronous Usage
```python
import asyncio
import requests_html

async def fetch_page():
    async_session = requests_html.AsyncHTMLSession()
    r = await async_session.get('https://httpbin.org/html')
    await r.html.render()
    print(r.html.find('h1')[0].text)

# Run the async function
asyncio.run(fetch_page())
```

### Custom Configuration
```python
import requests_html

session = requests_html.HTMLSession(
    verify=False,  # Disable SSL verification if needed
    mock_browser=True  # Use a mock browser instead of real one
)

r = session.get('https://example.com')
r.html.render(wait=1.0, scrolldown=True, sleep=2)
```

## Contributing
Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

For documentation updates, ensure changes are reflected in the `docs/source/` directory and run `make html` to verify formatting.

## License
MIT

## Contact / Authors
- **Author**: Kenneth Reitz
- **Email**: me@kennethreitz.org
- **Project URL**: https://github.com/psf/requests-html

For more information, visit the [project homepage](https://github.com/psf/requests-html).