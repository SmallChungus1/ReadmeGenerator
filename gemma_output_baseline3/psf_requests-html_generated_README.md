# Project Title: Requests-HTML

## Description

Requests-HTML is a Python library that simplifies HTML parsing and web scraping. It provides a user-friendly interface for extracting data from websites, making it accessible to both beginners and experienced developers.  It leverages the power of Pyppeteer, Requests, and other libraries to provide a robust and efficient solution for web scraping tasks.

## Features

*   **Simple API:** Offers a straightforward and intuitive API for common web scraping tasks.
*   **Pyppeteer Integration:** Uses Pyppeteer to render JavaScript-heavy websites, ensuring accurate data extraction.
*   **Requests Support:** Leverages the Requests library for efficient HTTP requests.
*   **Automatic Cookie Handling:**  Handles cookies automatically, simplifying scraping of websites that require authentication.
*   **User-Agent Control:** Allows you to specify a custom user agent to mimic different browsers.
*   **HTML Parsing:**  Provides tools for parsing and navigating HTML documents.
*   **Link Extraction:** Easily extracts links from web pages.
*   **Text Extraction:** Extracts text content from HTML elements.
*   **CSS Selectors:** Supports CSS selectors for precise element targeting.
*   **XPath Support:**  Includes XPath support for advanced element selection.

## Prerequisites / Requirements

*   Python 3.6 or higher
*   `requests`
*   `pyquery`
*   `fake-useragent`
*   `parse`
*   `beautifulsoup4`
*   `w3lib`
*   `pyppeteer>=0.0.14`

## Installation

```bash
pip install requests-html
```

## Usage

```python
from requests_html import HTML

# Example: Scrape a website and extract all links
html = HTML()
r = html.open('https://www.example.com')
links = r.links
for link in links:
    print(link)

# Example:  Scrape a website and extract the title
html = HTML()
r = html.open('https://www.example.com')
title = r.html.find('title')[0].text
print(title)
```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute.

## License

MIT License

## Contact / Authors

*   **Kenneth Reitz:** [https://kennethreitz.org/](https://kennethreitz.org/)
*   **Project:** [https://github.com/psf/requests-html](https://github.com/psf/requests-html)