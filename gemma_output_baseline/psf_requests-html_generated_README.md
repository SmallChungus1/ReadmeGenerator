# Requests-HTML

![requests-html logo](ext/requests-html-logo.ai)

## Description

Requests-HTML is a Python library for human-friendly HTML parsing. It aims to simplify web scraping and HTML manipulation by providing a more intuitive and Pythonic API compared to traditional libraries like Beautiful Soup or lxml. It builds on top of popular libraries like `requests`, `pyquery`, and `pyppeteer` to offer a powerful and flexible solution for web data extraction.

## Features

*   **Human-Friendly API:** Designed for ease of use and readability.
*   **HTML Parsing:**  Parses HTML content efficiently.
*   **JavaScript Rendering:**  Can render JavaScript-heavy websites using `pyppeteer`.
*   **CSS Selectors:** Supports CSS selectors for element selection.
*   **XPath Support:** Allows querying elements using XPath expressions.
*   **Automatic Encoding Detection:** Handles character encoding automatically.
*   **Asynchronous Support:** Offers asynchronous operations for improved performance.
*   **Session Management:** Provides a session object for managing cookies and headers.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Python 3.6 or higher
*   `requests`
*   `pyquery`
*   `fake-useragent`
*   `parse`
*   `beautifulsoup4`
*   `w3lib`
*   `pyppeteer` (for JavaScript rendering)

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/psf/requests-html
    cd requests-html
    ```

2.  Install the package using `pip`:

    ```bash
    pip install .
    ```

    Alternatively, install using `pipenv`:

    ```bash
    pipenv install .
    ```

## Usage

```python
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.example.com')

# Render JavaScript (if needed)
# r.html.render()

# Extract title
title = r.html.find('title', first=True).text
print(f"Title: {title}")

# Find all links
links = r.html.links
for link in links:
    print(link)
```

## Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to the project.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Contact / Authors

*   **Kenneth Reitz:** [me@kennethreitz.org](mailto:me@kennethreitz.org)
*   **GitHub Repository:** [https://github.com/psf/requests-html](https://github.com/psf/requests-html)