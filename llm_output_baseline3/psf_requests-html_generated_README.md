# Requests-HTML

![Build Status](https://github.com/psf/requests-html/workflows/CI/badge.svg)
![Version](https://img.shields.io/pypi/v/requests-html.svg)
![License](https://img.shields.io/pypi/l/requests-html.svg)

A powerful HTML parsing library for Python that makes web scraping and HTML manipulation as simple and intuitive as possible. Built on top of `requests` and `pyppeteer`, it provides a seamless way to render dynamic HTML content and extract data with ease.

---

## Description

**Requests-HTML** is a Python library designed to simplify the process of parsing and interacting with HTML content, especially when dealing with JavaScript-rendered pages. Unlike traditional HTML parsers that only work with static content, Requests-HTML uses a headless browser (via Pyppeteer) to render pages fully, allowing you to extract data from dynamic, interactive websites.

This library is ideal for developers who need to scrape content from modern websites that rely heavily on JavaScript for content delivery. It combines the simplicity of `requests` with the power of browser automation, offering a clean, readable API for both synchronous and asynchronous operations.

---

## Features

- ✅ **Dynamic Page Rendering**: Render JavaScript-heavy pages using a headless browser (Pyppeteer).
- ✅ **Intuitive API**: Familiar syntax inspired by `requests`, with methods like `find()`, `xpath()`, and `text()`.
- ✅ **Support for Both Sync and Async**: Use `HTMLSession` or `AsyncHTMLSession` for synchronous or asynchronous workflows.
- ✅ **Built-in User-Agent Rotation**: Automatically rotate user agents to avoid IP blocking.
- ✅ **Cookie Management**: Handle cookies seamlessly with built-in support for session cookies.
- ✅ **Automatic URL Resolution**: Convert relative links to absolute URLs.
- ✅ **Error Handling & Retries**: Built-in retry logic for network failures.
- ✅ **Support for Multiple Selectors**: Use CSS, XPath, or text-based selectors to find elements.
- ✅ **Rich HTML Parsing**: Access full HTML structure via `lxml` and `PyQuery` for deep manipulation.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites

- Python 3.6 or higher
- Internet connection (required for browser rendering)
- A modern web browser (headless via Pyppeteer)

> **Note**: Pyppeteer requires a stable version of Chromium or Chrome. Ensure your system has access to a compatible browser version.

---

## Installation

Install the latest version of Requests-HTML using `pip`:

```bash
pip install requests-html
```

For development (with documentation and tests):

```bash
pip install -e .
```

> **Note**: The package depends on several external libraries, including `requests`, `pyppeteer`, `pyquery`, and `fake-useragent`. These are automatically installed as dependencies.

---

## Usage

### Basic Example: Scrape a Dynamic Page

```python
import requests_html

# Create a session
session = requests_html.HTMLSession()

# Render a page with JavaScript
r = session.get('https://httpbin.org/headers')

# Extract data using PyQuery-style selectors
title = r.html.find('title', first=True).text
print(title)

# Find all links
links = r.html.find('a')
for link in links:
    print(link.text)
```

### Asynchronous Example

```python
import asyncio
import requests_html

async def fetch_page():
    async_session = requests_html.AsyncHTMLSession()
    r = await async_session.get('https://httpbin.org/headers')
    print(r.html.find('title', first=True).text)

# Run the async function
asyncio.run(fetch_page())
```

### Custom Headers and User-Agent

```python
session = requests_html.HTMLSession()
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
r = session.get('https://example.com')
print(r.html.text)
```

### Handling Cookies

```python
session = requests_html.HTMLSession()
session.cookies.set('session_id', 'abc123')

r = session.get('https://example.com')
print(r.html.find('div#profile', first=True).text)
```

### Search with Templates

```python
result = r.html.search('Price: {price}')
print(result[0].get('price'))
```

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your help is appreciated.

- 📝 **Report Issues**: Open an issue on GitHub with a clear description.
- 🚀 **Submit Pull Requests**: Ensure your code follows PEP 8 and passes all tests.
- 📚 **Improve Documentation**: Help make the docs more accessible and complete.
- 💬 **Discuss Ideas**: Join the conversation in the [GitHub Discussions](https://github.com/psf/requests-html/discussions).

For detailed contribution guidelines, see the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

**Author**: Kenneth Reitz  
🔗 [Website](https://kennethreitz.org)  
🐦 [Twitter](https://twitter.com/kennethreitz)  
💬 [Say Thanks](https://saythanks.io/to/kennethreitz)

This project is part of Kenneth Reitz's broader suite of tools for making Python development more accessible and intuitive. Explore his other projects:

- [requests](https://2.python-requests.org/)
- [pipenv](http://pipenv.org/)
- [records](https://github.com/kennethreitz/records)
- [maya](https://github.com/timofurrer/maya)
- [legit](http://www.git-legit.org)

For more information, visit the official documentation at:  
👉 [https://requests-html.readthedocs.io](https://requests-html.readthedocs.io)