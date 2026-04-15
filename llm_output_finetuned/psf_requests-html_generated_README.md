# Requests-HTML

![Build Status](https://github.com/psf/requests-html/workflows/CI/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)

A powerful, intuitive HTML parsing library for Python — designed to make web scraping and HTML manipulation as simple and human-friendly as possible.

> **Requests-HTML** combines the simplicity of `requests` with the full power of a real browser engine (via `pyppeteer`) to render dynamic HTML content, allowing you to scrape JavaScript-heavy websites with ease.

---

## Description

Requests-HTML is a Python library that extends the capabilities of `requests` by adding full HTML rendering support. Unlike traditional parsers that only handle static HTML, Requests-HTML uses a headless browser to render pages dynamically — executing JavaScript, handling cookies, and loading content that would otherwise be inaccessible through standard requests.

It provides a clean, familiar interface for parsing HTML, with built-in support for:
- Dynamic content rendering
- CSS selectors and XPath queries
- Form submission and navigation
- JavaScript execution
- Browser-level features like scrolling, waiting, and cookies

Perfect for scraping modern websites with complex JavaScript interactions — such as social media, e-commerce platforms, or dashboards.

---

## Features

- ✅ **Full JavaScript rendering** using `pyppeteer` (headless Chrome)
- ✅ **Intuitive HTML parsing** with `PyQuery` and `lxml`
- ✅ **Support for dynamic content** (e.g., infinite scroll, lazy loading)
- ✅ **Simple API** resembling `requests` — e.g., `HTMLSession().get(url)`
- ✅ **Built-in user agent rotation** with `fake-useragent`
- ✅ **Automatic URL resolution** and relative link handling
- ✅ **Support for cookies, headers, and custom timeouts**
- ✅ **Async support** via `AsyncHTMLSession` for high-performance scraping
- ✅ **Easy navigation** with `next()` and `links()` methods
- ✅ **Built-in search and text extraction** with `search()` and `text()`

---

## Table of Contents

- [Prerequisites](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

- **Python 3.6 or higher**
- Internet connection (for dynamic rendering)
- A modern browser environment (automatically handled via `pyppeteer`)

> ⚠️ Requests-HTML requires `pyppeteer`, which may require additional system dependencies (e.g., Chrome/Chromium) on certain platforms. Ensure your system has a compatible browser installed or use a containerized environment.

---

## Installation

Install Requests-HTML using `pip`:

```bash
pip install requests-html
```

For development (optional):

```bash
pip install -e .
```

> 💡 The package includes dependencies such as `requests`, `pyquery`, `fake-useragent`, `beautifulsoup4`, and `w3lib` — all automatically installed.

---

## Usage

### Basic Example: Scrape a Dynamic Page

```python
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://httpbin.org/html')

# Render the page (JavaScript will be executed)
r.html.render(wait=2)  # Wait 2 seconds for JS to load

# Extract text using PyQuery
title = r.html.find('h1', first=True).text
print(title)  # Output: "Hello, World!"

# Find all links
links = r.html.find('a')
for link in links:
    print(link.text, link.attrs['href'])
```

### Async Example

```python
from requests_html import AsyncHTMLSession

async def scrape():
    async_session = AsyncHTMLSession()
    r = await async_session.get('https://httpbin.org/html')
    await r.html.render(wait=2)
    print(r.html.find('h1', first=True).text)

# Run the async function
import asyncio
asyncio.run(scrape())
```

### Advanced: Custom Headers, Cookies, and User Agent

```python
session = HTMLSession()

r = session.get(
    'https://example.com',
    headers={'User-Agent': 'Mozilla/5.0'},
    cookies={'session': 'abc123'},
    timeout=10
)

r.html.render(wait=1, scrolldown=True, sleep=1)
print(r.html.find('div.content', first=True).text)
```

### Search with Templates

```python
result = r.html.search(r'price: (\d+)')
print(result[0])  # Output: 99
```

> 🔍 Use `search()` to extract structured data from text patterns.

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, improving documentation, or adding new features, your help is appreciated.

### How to Contribute

1. **Fork the repository** on GitHub
2. **Create a feature branch** (`git checkout -b feature/your-feature`)
3. **Commit your changes** with clear, descriptive messages
4. **Push to the branch** and open a pull request

### Reporting Issues

- Open an issue in the [GitHub Issues](https://github.com/psf/requests-html/issues) section
- Include:
  - A clear description of the problem
  - Steps to reproduce
  - Expected vs. actual behavior
  - Environment details (Python version, OS, etc.)

> 📝 A detailed `CONTRIBUTING.md` is available in the repository.

---

## License

Requests-HTML is licensed under the **MIT License**.

> Copyright (c) 2015–2026 Kenneth Reitz  
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

---

## Contact / Authors

**Author**: Kenneth Reitz  
🌐 [https://kennethreitz.org](https://kennethreitz.org)  
🐦 [@kennethreitz](https://twitter.com/kennethreitz)  
📧 me@kennethreitz.org  

> Requests-HTML is part of Kenneth Reitz’s broader mission to make Python tools **simple, intuitive, and human-friendly**.  
> Learn more about his work at [python-requests.org](https://2.python-requests.org), [pipenv.org](http://pipenv.org), and [howtopython.org](http://howtopython.org).

---

> ⚠️ **Note**: This project is actively maintained and tested on Python 3.6+. For best results, use a recent version of Python (3.8+ recommended).  
> 🚀 Try it out today — scrape the web like a human, not a script!