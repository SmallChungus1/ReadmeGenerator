# Requests-HTML

![Build Status](https://github.com/psf/requests-html/workflows/CI/badge.svg)
![Version](https://img.shields.io/pypi/v/requests-html.svg)
![License](https://img.shields.io/pypi/l/requests-html.svg)

> A powerful, human-friendly HTML parser built on top of `requests` and `pyppeteer` for web scraping and dynamic content rendering.

---

## Description

**Requests-HTML** is a Python library designed to simplify the process of parsing and interacting with HTML content from the web. Unlike traditional parsers that struggle with JavaScript-rendered content, Requests-HTML leverages **headless browser automation** via `pyppeteer` to render pages dynamically, allowing you to extract data from complex, interactive websites as if they were static HTML.

It combines the simplicity of `requests` with the power of a real browser, making it ideal for scraping modern web applications that rely on JavaScript to load content.

Built by [Kenneth Reitz](https://kennethreitz.org), the creator of `requests`, this library is designed with clarity, performance, and ease of use in mind.

---

## Features

- ✅ **Dynamic Page Rendering**: Render JavaScript-heavy pages using a real browser engine (via `pyppeteer`).
- ✅ **Full HTML Parsing**: Access HTML via familiar methods like `find()`, `xpath()`, and `search()` using `PyQuery` and `lxml`.
- ✅ **Support for Dynamic Navigation**: Navigate through pages using `next()` and `add_next_symbol()` for pagination.
- ✅ **Built-in User-Agent Rotation**: Automatically rotate user agents to avoid detection.
- ✅ **Cookie Management**: Handle cookies seamlessly with support for session persistence.
- ✅ **Async Support**: Use `AsyncHTMLSession` for non-blocking, concurrent scraping.
- ✅ **Configurable Rendering Options**: Set timeouts, scroll-down, sleep intervals, and retries.
- ✅ **Clean, Intuitive API**: Designed to feel like a standard `requests` session, with familiar syntax.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

- **Python 3.6+**
- A modern web browser (headless via `pyppeteer`)
- Internet connection (for dynamic rendering)

> ⚠️ Note: `pyppeteer` requires a working Node.js environment (v12+). This is managed automatically via `pip` and `pyppeteer`.

---

## Installation

Install the latest version of Requests-HTML using `pip`:

```bash
pip install requests-html
```

For development (with tests and documentation):

```bash
pip install -e .
```

> 💡 The package depends on:
> - `requests`
> - `pyppeteer` (headless browser)
> - `pyquery` (HTML parsing)
> - `fake-useragent` (rotating user agents)
> - `beautifulsoup4`, `w3lib`, `parse`

---

## Usage

### Basic Example: Fetch and Parse a Dynamic Page

```python
from requests_html import HTMLSession

session = HTMLSession()

# Fetch a page that loads content via JavaScript
r = session.get('https://httpbin.org/html')

# Get the HTML content as a parsed object
html = r.html

# Extract text using PyQuery
title = html.find('h1', first=True).text
print(title)  # Output: "Hello from httpbin.org"

# Find all links
links = html.find('a')
for link in links:
    print(link.text)
```

### Async Example: Concurrent Scraping

```python
from requests_html import AsyncHTMLSession

async def scrape_page(url):
    async_session = AsyncHTMLSession()
    r = await async_session.get(url)
    title = r.html.find('h1', first=True).text
    return title

# Run multiple requests concurrently
import asyncio
results = asyncio.gather(
    scrape_page('https://httpbin.org/html'),
    scrape_page('https://httpbin.org/json')
)

print(await results)
```

### Scroll Down and Wait for Content

```python
r = session.get('https://example.com/infinite-scroll')

# Scroll down and wait for content to load
r.html.render(wait=2, scrolldown=True, sleep=1)

# Now parse the page
content = r.html.find('div.content')
```

### Handle Cookies and Sessions

```python
session = HTMLSession()

# Set cookies
session.cookies.set('session_id', 'abc123')

# Or pass cookies directly
r = session.get('https://example.com', cookies={'session_id': 'abc123'})

# Access cookies in response
print(r.cookies)
```

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your help is appreciated.

### How to Contribute

1. Fork the repository on GitHub.
2. Create a new feature branch (`feature/your-feature`).
3. Make your changes and commit them with clear, descriptive messages.
4. Push to the branch and open a pull request.

### Reporting Issues

Please open a new issue on GitHub if you encounter a bug or have a feature request. Include:
- A clear description of the issue
- Steps to reproduce
- Expected vs. actual behavior

> 📝 See the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines.

---

## License

This project is licensed under the **MIT License**.

> See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author**: Kenneth Reitz
- **Website**: [kennethreitz.org](https://kennethreitz.org)
- **GitHub**: [@psf](https://github.com/psf)
- **Twitter**: [@kennethreitz](https://twitter.com/kennethreitz)
- **Say Thanks**: [saythanks.io/to/kennethreitz](https://saythanks.io/to/kennethreitz)

For questions or feedback, feel free to open an issue or reach out directly via email at `me@kennethreitz.org`.

--- 

> 💡 Inspired by the philosophy of "simple, human-friendly tools for developers."  
> Built with ❤️ by Kenneth Reitz.  
> Learn more: [requests-html.readthedocs.io](https://requests-html.readthedocs.io)