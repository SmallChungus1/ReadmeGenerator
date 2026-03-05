# Got - Human-Friendly and Powerful HTTP Request Library for Node.js

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![npm version](https://badge.fury.io/js/got.svg)](https://badge.fury.io/js/got)
[![Build Status](https://github.com/sindresorhus/got/workflows/main/badge.svg)](https://github.com/sindresorhus/got/actions)
[![Sponsor](https://img.shields.io/github/sponsors/sindresorhus)](https://github.com/sindresorhus/got?sponsor=1)

## Description

Got is a human-friendly and powerful HTTP request library for Node.js. It aims to make requesting data from the web as simple and intuitive as possible. It provides a clean and well-documented API, supports various features like streams, redirects, authentication, and more.

## Features

*   **Simple API:**  Easy to use and understand.
*   **Streams Support:** Works seamlessly with streams for large data.
*   **Redirect Handling:** Automatically follows redirects.
*   **Authentication:** Supports basic and other authentication methods.
*   **Timeouts:** Configurable timeouts for requests and sockets.
*   **gzip and Brotli Compression:** Automatic decompression of compressed responses.
*   **Retries:** Built-in retry mechanism with customizable delays.
*   **HTTP/1 and HTTP/2 Support:**  Supports both major HTTP protocols.
*   **Proxy Support:**  Configure proxies for requests.
*   **Cache Control** and ability to customize cache behavior.
*   **Unix Socket Support:**  Support for connecting to local Unix domain sockets.
*   **Promise-based API:**  Modern asynchronous programming with Promises.
*   **Extensible:**  Highly customizable through options and extensions.
*   **Strong Typing:**  Written in TypeScript with comprehensive type definitions.

## Installation

```bash
npm install got
```

## Usage

```javascript
import got from 'got';

async function fetchData() {
  try {
    const response = await got('https://example.com');
    console.log(response.body);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

fetchData();
```

**More examples:**

*   **Sending a POST request:**

    ```javascript
    const response = await got.post('https://example.com/api', {
      json: {
        key: 'value',
      },
    });
    ```

*   **Setting headers:**

    ```javascript
    const response = await got('https://example.com', {
      headers: {
        'Authorization': 'Bearer my-token',
      },
    });
    ```

*   **Handling timeouts:**

    ```javascript
    const response = await got('https://example.com', {
      timeout: {
        request: 5000, // 5 seconds
      },
    });
    ```

*   **Streaming data:**

    ```javascript
    const stream = got.stream('https://example.com');
    stream.on('data', (chunk) => {
      console.log(chunk.toString());
    });
    stream.on('end', () => {
      console.log('Stream finished');
    });
    ```

## Additional Information

*   **License:** [MIT](LICENSE)
*   **GitHub Repository:** [https://github.com/sindresorhus/got](https://github.com/sindresorhus/got)
*   **Documentation:**  (Link to documentation, if available)
*   **Issues:** [https://github.com/sindresorhus/got/issues](https://github.com/sindresorhus/got/issues)
*   **Funding:** [https://github.com/sindresorhus/got?sponsor=1](https://github.com/sindresorhus/got?sponsor=1)

## Examples Directory

The `documentation/examples` directory contains several examples demonstrating various features:

*   `advanced-creation.js`:  Advanced instance creation and customization.
*   `gh-got.js`:  Example for GitHub API integration.
*   `h2c.js`:  HTTP/2 Cleartext protocol example.
*   `pagination.js`:  Handling paginated APIs.
*   `runkit-example.js`:  Example for running in RunKit.
*   `uppercase-headers.js`:  Demonstrates header manipulation.