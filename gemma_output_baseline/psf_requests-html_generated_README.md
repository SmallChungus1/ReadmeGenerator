```markdown
# requests-HTML

[![Travis CI](https://travis-ci.com/psf/requests-html.svg?branch=master)](https://travis-ci.com/psf/requests-html)

**requests-HTML** is a Python library designed to simplify HTML parsing and web scraping. It aims to provide a user-friendly interface with powerful features, making it ideal for both beginners and experienced developers.

## Description

requests-HTML combines the simplicity of Requests with the parsing capabilities of tools like Beautiful Soup and PyQuery. It offers features like JavaScript rendering, CSS Selectors, XPath Selectors, and automatic handling of redirects, all while maintaining a clean and intuitive API.  It provides both synchronous and asynchronous interfaces.

## Features

*   **Full JavaScript Support:** Renders JavaScript-heavy pages, enabling parsing of dynamic content.
*   **CSS Selectors:** Uses jQuery-style CSS Selectors for easy element selection.
*   **XPath Selectors:** Supports XPath selectors for more advanced element identification.
*   **Automatic User-Agent:** Mimics a real web browser with a default User-Agent.
*   **Automatic Redirect Handling:** Handles redirects seamlessly.
*   **Connection Pooling & Cookie Persistence:**  Efficiently manages connections and cookies.
*   **Synchronous and Asynchronous APIs:** Provides both synchronous (`HTMLSession`) and asynchronous (`AsyncHTMLSession`) interfaces for different use cases.
*   **Rendering:** Can render dynamic content with JavaScript execution.
*   **Pagination Support:** Simple iteration through paginated content.

## Installation

```bash
pipenv install requests-html
```

Only **Python 3.6+** is supported.

## Usage

Here are some basic examples to illustrate how to use requests-HTML:

```python
from requests_html import HTMLSession

# Create a session object
session = HTMLSession()

# Make a request to a URL
r = session.get('https://python.org/')

# Find elements using CSS Selectors
about = r.html.find('#about', first=True)  # Find the first element with ID 'about'

# Extract text content
print(about.text)

# Get all links on the page
links = r.html.links
print(links)

# Search for specific text
search_result = r.html.search('Python is a {} language')[0]
print(search_result)
```

**Asynchronous Usage:**

```python
from requests_html import AsyncHTMLSession
import asyncio

async def main():
    async_session = AsyncHTMLSession()
    r = await async_session.get('https://python.org/')
    about = r.html.find('#about', first=True)
    print(about.text)
    await async_session.close() #important to close session

if __name__ == "__main__":
    asyncio.run(main())
```

## API Documentation

The core classes and functions are:

*   **`HTMLSession`**:  Synchronous session for making HTTP requests.
*   **`AsyncHTMLSession`**: Asynchronous session for making HTTP requests.
*   **`HTML`**: Represents the parsed HTML content.
*   **`Element`**: Represents an individual HTML element.

Refer to the [full documentation](https://requests-html.readthedocs.io/en/latest/) for detailed information on all classes and methods.

## Contributing

Contributions are welcomed!  Please see the [CONTRIBUTING.md](link to contributing doc if they have one) file for guidelines.

## License

requests-HTML is licensed under the [MIT License](LICENSE).
```