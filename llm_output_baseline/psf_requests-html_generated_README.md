# Requests-HTML

## Description
**Requests-HTML** is a Python library designed to simplify the process of parsing HTML content, particularly for web scraping tasks. It combines the power of `requests` with browser automation via `pyppeteer`, enabling users to render dynamic HTML pages and extract data with ease. The library provides a clean, intuitive API that abstracts away the complexity of JavaScript execution and DOM manipulation, making it ideal for developers who need to scrape modern, JavaScript-heavy websites.

## Features
- **Dynamic Page Rendering**: Renders HTML pages using a real browser engine (via pyppeteer), allowing JavaScript to execute and DOM to load fully.
- **Intuitive API**: Offers a familiar interface similar to `requests`, with methods like `html()`, `find()`, and `xpath()` for easy content extraction.
- **Support for JavaScript-Driven Sites**: Handles pages that rely on client-side JavaScript to generate content.
- **Built-in User-Agent Rotation**: Automatically rotates user agents to avoid detection by websites.
- **Cookie Management**: Seamlessly manages cookies through integration with `requests` and browser sessions.
- **Error Handling & Retries**: Implements retry logic with configurable timeouts and backoff for robust scraping.
- **Async Support**: Provides asynchronous capabilities for non-blocking, high-performance scraping workflows.
- **HTML Parsing Flexibility**: Supports multiple parsing backends (PyQuery and lxml) for different use cases.
- **Automatic URL Resolution**: Handles relative URLs and resolves them to absolute ones.
- **Navigation and Pagination**: Enables easy navigation between pages via `next()` and `absolute_links()` methods.

## Installation

Install the latest version of Requests-HTML using pip:

```bash
pip install requests-html
```

Alternatively, if you're working in a project with a `Pipfile`, install via:

```bash
pipenv install requests-html
```

## Usage

Here's a practical example of how to use Requests-HTML to scrape a dynamic webpage:

```python
import requests_html

# Create a new HTML session
session = requests_html.HTMLSession()

# Render a page with JavaScript execution
response = session.get('https://httpbin.org/html')

# Extract text content using PyQuery
text = response.html.find('h1', first=True).text
print(text)  # Output: "Hello, world!"

# Extract links using XPath
links = response.html.xpath('//a[@href]')
for link in links:
    print(link.text)

# Navigate to the next page
next_page = response.html.next()
if next_page:
    next_response = session.get(next_page)
    print("Navigated to:", next_page)
```

For asynchronous operations:

```python
import asyncio
import requests_html

async def scrape_async():
    async_session = requests_html.AsyncHTMLSession()
    async_response = await async_session.get('https://httpbin.org/html')
    
    # Extract content
    title = async_response.html.find('title', first=True).text
    print("Async Title:", title)

# Run the async function
asyncio.run(scrape_async())
```

### Key Methods Overview

| Method | Purpose |
|-------|--------|
| `session.get(url)` | Fetch a page with JavaScript rendering |
| `response.html.find(selector)` | Find elements using CSS selectors |
| `response.html.xpath(selector)` | Find elements using XPath |
| `response.html.text()` | Get the full text of the page |
| `response.html.links()` | Get all links on the page |
| `response.html.next()` | Navigate to the next page |
| `session.browser()` | Access the underlying browser instance |

> **Note**: This library requires a modern version of Python (3.6+). Ensure your environment has `pyppeteer`, `requests`, `pyquery`, and `fake-useragent` installed as dependencies.