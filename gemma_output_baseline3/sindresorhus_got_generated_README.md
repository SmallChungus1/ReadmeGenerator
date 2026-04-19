# Project Title: got

## Description

`got` is a human-friendly and powerful HTTP request library for Node.js. It's designed to be simple to use, yet feature-rich, offering a great alternative to existing libraries.

## Features

*   Human-friendly API
*   HTTP/1.1 and HTTP/2 support
*   Automatic retry with exponential backoff
*   Request and response streaming
*   Automatic JSON parsing
*   Support for various content encodings
*   URL encoding and decoding
*   Rate limiting
*   Support for cookies
*   Request and response interception
*   Support for various HTTP methods
*   Support for custom headers
*   Support for custom options
*   Support for various response types (JSON, text, buffer)
*   Support for redirects
*   Support for Unix socket URLs

## Prerequisites / Requirements

*   Node.js 22 or higher

## Installation

```bash
npm install got
```

## Usage

```javascript
import got from 'got';

async function main() {
  try {
    const response = await got('https://www.example.com');
    console.log(response.body);
    console.log(response.statusCode);
  } catch (error) {
    console.error(error);
  }
}

main();
```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

## License

MIT

## Contact / Authors

*   **Sindre Koruhatn** ([https://sindresorhus.com/](https://sindresorhus.com/))