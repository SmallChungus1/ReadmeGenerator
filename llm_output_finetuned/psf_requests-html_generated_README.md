# Requests-HTML

## Description

**Requests-HTML** is a Python library that simplifies HTML parsing and web scraping by combining the power of `requests` with a browser-like rendering engine. It allows developers to fetch web pages, render JavaScript-heavy content dynamically, and extract structured data using intuitive, human-friendly syntax—making it ideal for scraping modern, interactive websites.

Built on top of `pyppeteer`, Requests-HTML enables full-page rendering with realistic user-agent behavior, automatic cookie handling, and support for JavaScript execution. It provides a seamless interface between HTTP requests and HTML parsing, bridging the gap between traditional scraping tools and modern web applications.

## Features

- ✅ **Dynamic JavaScript Rendering**: Render pages with JavaScript (e.g., React, Vue, Angular) using a headless browser.
- ✅ **Intuitive HTML Parsing**: Access HTML content via familiar methods like `find()`, `xpath()`, and `search()`.
- ✅ **Automatic User-Agent Rotation**: Uses `fake-useragent` to simulate real browsers and avoid detection.
- ✅ **Support for Cookies & Sessions**: Handle cookies across requests and maintain session state.
- ✅ **Built-in HTML Utilities**: Access parsed content via `pq()` (PyQuery) and `lxml` for advanced manipulation.
- ✅ **Async Support**: Asynchronous rendering and requests via `AsyncHTMLSession`.
- ✅ **Next Page Navigation**: Automatically follow pagination links with `next()` method.
- ✅ **Error Resilience**: Retry mechanisms and timeout controls for robust scraping.

## Installation

Install Requests-HTML using pip:

```bash
pip install requests-html
```

> **Note**: This package requires Python 3.6 or higher. It depends on several external libraries including `requests`, `pyppeteer`, and `pyquery`.

## Usage

### Basic HTML Rendering and Parsing

```python
from requests_html import HTMLSession

# Create a session
session = HTMLSession()

# Fetch a page with JavaScript rendering
r = session.get('https://httpbin.org/html')

# Access the rendered HTML
html = r.html
print(html.html)  # Full HTML content

# Find elements using CSS selectors
links = html.find('a')
for link in links:
    print(link.text, link.attrs['href'])

# Use PyQuery for advanced parsing
pq = html.pq
title = pq('title').text()
print(title)
```

### Asynchronous Rendering

```python
from requests_html import AsyncHTMLSession

async def fetch_page():
    async_session = AsyncHTMLSession()
    r = await async_session.get('https://httpbin.org/html')
    print(r.html.find('h1')[0].text)
    await async_session.close()

# Run the async function
import asyncio
asyncio.run(fetch_page())
```

### Custom Configuration and Script Execution

```python
from requests_html import HTMLSession

session = HTMLSession()

# Render a page with custom script execution
r = session.get('https://example.com', 
                script='document.querySelector("body").innerHTML', 
                wait=1.0, 
                scrolldown=True, 
                timeout=10)

# Extract data
data = r.html.find('div[data-id]')
for item in data:
    print(item.text)
```

### Handling Pagination

```python
session = HTMLSession()

for page in range(1, 6):
    r = session.get(f'https://example.com/page/{page}')
    items = r.html.find('article.item')
    for item in items:
        print(item.text)
    # Automatically follow next page link
    next_link = r.html.links('a.next')
    if next_link:
        print(f"Next page: {next_link[0]}")
```

### Advanced Options

```python
r = session.get(
    'https://example.com',
    retries=8,
    timeout=8.0,
    sleep=1,
    reload=True,
    keep_page=True,
    cookies=[{'name': 'session', 'value': 'abc123'}]
)
```

> For full documentation, see the [official documentation](https://requests-html.org/).