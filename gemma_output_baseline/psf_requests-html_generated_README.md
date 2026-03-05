# requests-HTML

[![Travis CI Status](https://travis-ci.com/psf/requests-html.svg?branch=master)](https://travis-ci.com/psf/requests-html)

Requests-HTML is a Python library designed to simplify web scraping and HTML parsing. It aims to provide a more intuitive and human-friendly interface compared to traditional tools, while offering powerful features like full JavaScript support and seamless handling of dynamic content.

## Description

Requests-HTML combines the elegance of the Requests library with the parsing capabilities of PyQuery and the rendering power of Chromium (via pyppeteer). This allows you to easily make HTTP requests, parse HTML, and execute JavaScript to render dynamic pages, all within a concise and Pythonic workflow.  It’s perfect for tasks such as:

*   **Web Scraping:** Extracting data from websites.
*   **Data Analysis:** Gathering information for research or analysis.
*   **Automated Testing:** Verifying website behavior and content.
*   **Dynamic Content Rendering:**  Accessing content that relies on JavaScript execution.

## Features

*   **Full JavaScript Support:** Renders pages using a headless Chromium browser, handling JavaScript-generated content seamlessly.
*   **CSS Selectors:** Uses a jQuery-style syntax for easy element selection with PyQuery.
*   **XPath Selectors:** Supports XPath queries for more complex element targeting.
*   **Mocked User-Agent:** Simulates a real web browser to avoid bot detection.
*   **Automatic Redirect Handling:**  Follows redirects automatically.
*   **Connection Pooling & Cookie Persistence:** Improves performance and maintains session state.
*   **Async Support**: Offers asynchronous methods for efficient handling with coroutines.
*   **Pagination Support:** Simplified iteration over paginated content.
*   **User-Friendly API:** Provides a clean and intuitive API for common web scraping tasks.

## Installation

```bash
pip install requests-html
```

Requires Python 3.6 or higher.

## Usage

Here's a basic example of how to use requests-HTML:

```python
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://python.org/')

# Find all links on the page
links = r.html.links
print(links)

# Select an element using a CSS selector
about = r.html.find('#about', first=True)
print(about.text)

# Render the page with JavaScript
r.html.render()

# Search for text
result = r.html.search('Python is a {} language')[0]
print(result)
```

**Asynchronous usage:**

```python
from requests_html import AsyncHTMLSession

async def scrape_reddit():
    async with AsyncHTMLSession() as session:
        r = await session.get('https://www.reddit.com/')
        print(r.html.html)

# To run the async function, you'll need an event loop (e.g., using asyncio)
import asyncio
asyncio.run(scrape_reddit())
```

## API Reference

### `HTMLSession`

The `HTMLSession` class is used to make HTTP requests and manage sessions.

*   `session.get(url)`: Makes a GET request to the specified URL.
*   `session.post(url, data=None, files=None)`: Makes a POST request.  (Other request methods are available as well)

### `HTML`

The `HTML` class represents the parsed HTML content of a page.

*   `html`: The raw HTML content as a string.
*   `links`: A set of all links found on the page.
*   `absolute_links`: A set of all absolute URLs found on the page.
*   `find(selector, containing=None, first=False)`:  Finds elements matching a CSS selector.
*   `search(template)`: Searches the HTML for a specific string using a parse template.
*   `render()`: Renders the page with JavaScript using a headless Chromium browser.
*   `next()` : Attempts to automatically find and return the next page in a paginated list.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```