# Got - Delightful HTTP requests

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![npm version](https://badge.fury.io/js/got.svg)](https://badge.fury.io/js/got)
[![Build Status](https://github.com/sindresorhus/got/workflows/main/badge.svg)](https://github.com/sindresorhus/got/actions)
[![Donate](https://img.shields.io/badge/Donate-GitHub%20Sponsor-blue.svg)](https://github.com/sindresorhus/got?sponsor=1)

**Got** is a human-friendly and powerful HTTP request library for Node.js. It provides a simple and intuitive API for making HTTP requests, with advanced features such as automatic JSON parsing, request timeouts, and retry mechanisms.

## Description

Got simplifies making HTTP requests in Node.js, providing a cleaner and more expressive API compared to Node.js' built-in `http` and `https` modules. It builds on top of these modules, adding features like:

*   Automatic JSON parsing
*   Request timeouts
*   Retry mechanisms
*   Streaming support
*   Automatic decompression of response bodies (gzip, deflate, br, zstd)
*   Support for HTTP/2
*   Extensible options and plugins

## Features

*   **Simple API:** Easy-to-use methods for making various types of HTTP requests (GET, POST, PUT, DELETE, etc.).
*   **Automatic JSON Parsing:** Automatically parses JSON responses when appropriate.
*   **Request Timeouts:** Configurable timeouts for requests to prevent hanging.
*   **Retry Mechanisms:** Automatically retries failed requests with configurable rules.
*   **Streaming Support:** Supports streaming of request and response bodies.
*   **HTTP/2 Support:** Supports HTTP/2 for improved performance.
*   **Compression:** Automatic decompression of gzip, deflate, br, and zstd encoded responses.
*   **Extensible:**  Easily extendable with custom options and plugins.
*   **Unicode Support:** Full support for Unicode characters in URLs, headers, and bodies.
*   **Redirect Handling:** Handles redirects automatically.
*   **Proxy Support:** Supports proxies.
*   **Streamlined Error Handling:**  Provides clear and informative error messages.
*   **TypeScript Support:**  Written in TypeScript for strong typing and improved developer experience.

## Installation

```bash
npm install got
```

## Usage

Here are some basic examples of how to use Got:

```javascript
import got from 'got';

// Make a GET request
const response = await got('https://example.com');
console.log(response.body); // "Hello World"

// Make a POST request with JSON data
const postResponse = await got('https://example.com/api/posts', {
  method: 'POST',
  json: {
    title: 'My Post',
    body: 'This is the content of my post.'
  }
});
console.log(postResponse.body);

// Set a timeout
const timeoutResponse = await got('https://example.com', { timeout: { request: 1000 }});

// Handle errors
try {
  const errorResponse = await got('https://example.com/nonexistent');
} catch (error) {
  console.error(error.message);
}
```

## Advanced Examples

* **Custom Headers:**
```javascript
const response = await got('https://example.com', { headers: { 'User-Agent': 'My Custom Agent' } });
```

* **Authentication:**
```javascript
const response = await got('https://example.com/protected', {
  username: 'your_username',
  password: 'your_password'
});
```

* **Streaming:**
```javascript
const stream = got.stream('https://example.com/large-file');
stream.pipe(fs.createWriteStream('output.txt'));
```

* **Redirects:**
Got automatically follows redirects by default.  You can control redirect behavior using the `followRedirect` option.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

[MIT License](LICENSE)

Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (https://sindresorhus.com)