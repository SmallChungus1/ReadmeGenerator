```markdown
# got

[![npm version](https://badge.fury.io/js/got.svg)](https://badge.fury.io/js/got)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Human-friendly and powerful HTTP request library for Node.js.

## Description

`got` is a versatile and developer-friendly HTTP request library for Node.js. It simplifies making HTTP requests with a clean and intuitive API, while offering powerful features for handling complex scenarios like redirects, timeouts, streams, and more. It's designed to be a modern alternative to libraries like `request` and `node-fetch`.

## Features

*   **Simple and intuitive API:**  Easy to use for basic requests and highly configurable for advanced use cases.
*   **Promise-based:** Uses Promises for asynchronous operations, making it easy to integrate with async/await.
*   **Automatic JSON parsing:**  Automatically parses JSON responses.
*   **Stream support:**  Handles both request and response streams efficiently.
*   **Timeout control:**  Configurable timeouts for requests and individual stages (connect, send, response).
*   **Redirect handling:**  Automatic redirect following with customizable behavior.
*   **Retry mechanism:**  Built-in retry logic with configurable backoff strategies.
*   **HTTP/2 support:** Supports HTTP/2 for improved performance.
*   **Proxy support:**  Configurable proxy settings.
*   **Cookie handling:**  Automatic cookie management.
*   **Extensible:**  Hooks and middleware for customizing request behavior.
*   **TypeScript support:**  Provides excellent TypeScript definitions.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Node.js version 22 or higher.

## Installation

Install `got` using npm or yarn:

```bash
npm install got
# or
yarn add got
```

## Usage

Here are a few examples of how to use `got`:

**Simple GET request:**

```javascript
import got from 'got';

async function fetchData() {
  try {
    const response = await got('https://api.github.com/users/sindresorhus');
    console.log(response.body);
  } catch (error) {
    console.error(error);
  }
}

fetchData();
```

**POST request with JSON body:**

```javascript
import got from 'got';

async function postData() {
  try {
    const response = await got('https://httpbin.org/post', {
      json: {
        key: 'value'
      }
    });
    console.log(response.body);
  } catch (error) {
    console.error(error);
  }
}

postData();
```

**Using streams:**

```javascript
import got from 'got';

async function streamData() {
  const stream = got.stream('https://example.com');

  stream.on('data', (chunk) => {
    console.log(chunk.toString());
  });

  stream.on('end', () => {
    console.log('Stream finished');
  });

  stream.on('error', (error) => {
    console.error(error);
  });
}

streamData();
```

**Advanced Creation with Context:**

```javascript
import got from '../../dist/source/index.js';

const instance = got.extend({
  context: {
    secret: 'your-secret'
  }
});

const response = await instance('https://example.com');
```

## Contributing

We welcome contributions to `got`! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## License

`got` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact / Authors

*   **Author:** Sindre Sorhus
*   **Repository:** [https://github.com/sindresorhus/got](https://github.com/sindresorhus/got)