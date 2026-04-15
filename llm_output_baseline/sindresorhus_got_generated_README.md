# got

[![Build Status](https://img.shields.io/github/actions/workflow/status/sindresorhus/got/ci.yml?branch=main)](https://github.com/sindresorhus/got/actions)
[![Version](https://img.shields.io/npm/v/got)](https://www.npmjs.com/package/got)
[![License](https://img.shields.io/npm/l/got)](https://github.com/sindresorhus/got/blob/main/LICENSE)
[![Sponsored](https://img.shields.io/badge/sponsored-by-sindresorhus-007acc.svg)](https://github.com/sindresorhus/got?sponsor=1)

A human-friendly and powerful HTTP request library for Node.js. `got` provides a simple, intuitive API for making HTTP requests with built-in support for streaming, retries, pagination, and advanced request customization.

> ✅ Built for developers who want a clean, readable API  
> ✅ Supports HTTP/2, streaming, and modern HTTP features  
> ✅ Extensible with hooks, custom handlers, and request chaining  
> ✅ Handles redirects, timeouts, and error recovery automatically  

---

## Description

`got` is a modern, feature-rich HTTP client for Node.js that simplifies making HTTP requests while providing robust error handling, automatic retries, and advanced request customization. Designed with developer experience in mind, it offers a clean, intuitive API that closely mirrors familiar tools like `curl` and `wget`, while adding powerful features such as streaming, pagination, and request transformation.

Unlike traditional HTTP libraries, `got` is designed to be both simple and extensible. It supports all major HTTP methods, handles redirects intelligently, and provides built-in support for streaming responses, content encoding (gzip, br, zstd), and automatic retry logic. It also includes a rich set of hooks and handlers that allow you to customize behavior at any stage of the request lifecycle.

Whether you're building a simple API client or a complex web scraping tool, `got` provides the flexibility and reliability you need.

---

## Features

- ✅ **Human-friendly API** – Simple syntax that closely resembles `curl` and `wget`
- ✅ **Streaming support** – Handle large responses with `got.stream()`
- ✅ **Automatic retries** – Configurable retry logic with exponential backoff
- ✅ **Pagination support** – Easily iterate through paginated APIs
- ✅ **Content encoding support** – Automatic decompression of gzip, br, zstd
- ✅ **Request customization** – Full control over headers, cookies, body, and options
- ✅ **Extensible hooks** – Modify request/response behavior with hooks and handlers
- ✅ **Built-in error handling** – Clear, structured error types for debugging
- ✅ **HTTP/2 support** – Native HTTP/2 via `http2-wrapper`
- ✅ **Unix socket support** – Handle local Unix domain socket URLs
- ✅ **Progress tracking** – Monitor upload/download progress in real-time
- ✅ **Response type control** – Choose between text, JSON, buffer, or raw response

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

- **Node.js v22+** – `got` requires Node.js 22 or higher due to ES2024+ features and modern HTTP APIs.
- **Modern JavaScript** – The library uses modern JavaScript syntax (ES2024+), including `async/await`, `type guards`, and `weak maps`.

> ⚠️ `got` does not support older versions of Node.js. Ensure your environment meets the minimum version requirement.

---

## Installation

Install `got` via npm or yarn:

```bash
npm install got
```

or

```bash
yarn add got
```

> 💡 The library is built with TypeScript and supports ESM (ES Modules). It is automatically compiled to JavaScript during installation.

---

## Usage

### Basic GET Request

```ts
import got from 'got';

const {body} = await got('https://api.github.com/users/octocat');
console.log(body);
```

### GET with JSON Response

```ts
const {body} = await got('https://api.github.com/users/octocat').json();
console.log(body.login); // 'octocat'
```

### POST Request with Body

```ts
const response = await got.post('https://httpbin.org/post', {
  body: {name: 'John', age: 30}
});
console.log(response.body);
```

### Streaming Response

```ts
const stream = await got.stream('https://httpbin.org/stream/10');
stream.on('data', chunk => {
  console.log(`Received chunk: ${chunk.length} bytes`);
});
stream.on('end', () => {
  console.log('Stream completed');
});
```

### Request with Custom Headers

```ts
const response = await got('https://httpbin.org/headers', {
  headers: {
    'User-Agent': 'MyApp/1.0',
    'X-Custom': 'value'
  }
});
```

---

## Examples

### 1. GitHub API with Rate Limiting (documentation/examples/gh-got.js)

```js
import got from 'got';

const instance = got.extend({
  prefixUrl: 'https://api.github.com',
  headers: {
    'accept': 'application/vnd.github.v3+json',
    'user-agent': 'gh-got/1.0'
  },
  hooks: {
    init: [
      (raw, options) => {
        if ('token' in raw) {
          options.context.token = raw.token;
          delete raw.token;
        }
      }
    ],
    response: [
      (options, response) => {
        response.rateLimit = {
          limit: parseInt(response.headers['x-ratelimit-limit'], 10),
          remaining: parseInt(response.headers['x-ratelimit-remaining'], 10),
          reset: new Date(parseInt(response.headers['x-ratelimit-reset'], 10) * 1000)
        };
      }
    ]
  }
});

const {body} = await instance('users/octocat').json();
console.log(body);
```

### 2. Pagination with API Results (documentation/examples/pagination.js)

```js
const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
  pagination: {
    paginate({response, currentItems}) {
      const page = Number(response.request.options.searchParams.get('page') || 1);
      return {searchParams: {page: page + 1}};
    },
    transform: response => response.body,
    filter({item}) {
      const date = new Date(item.commit.committer.date);
      return date.getTime() > Date.now() - (1000 * 86400 * 7);
    },
    countLimit: 50,
    backoff: 1000,
    requestLimit: 10
  }
});

for await (const commit of iterator) {
  console.log(commit.commit.message.split('\n')[0]);
}
```

### 3. HTTP/2 with H2C (documentation/examples/h2c.js)

```js
import http2 from 'http2-wrapper';
import got from 'got';

let sessions = {};
const getSession = ({origin}) => {
  if (sessions[origin] && !sessions[origin].destroyed) return sessions[origin];
  const session = http2.connect(origin);
  session.once('error', () => delete sessions[origin]);
  sessions[origin] = session;
  return session;
};

const instance = got.extend({
  hooks: {
    beforeRequest: [
      options => {
        options.h2session = getSession(options.url);
        options.http2 = true;
        options.request = http2.request;
      }
    ]
  }
});

const server = http2.createServer((req, res) => res.end('{}'));
server.listen(async () => {
  const {headers, body} = await instance(`http://localhost:${server.address().port}`, {context: {h2c: true}});
  console.log(headers, body);
});
```

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your help is appreciated.

### How to Contribute

1. **Fork the repository** on GitHub
2. **Create a new feature branch** for your changes
3. **Submit a pull request** with a clear description of your changes
4. **Run tests** to ensure your changes don't break existing functionality

> 🔍 All PRs are reviewed by the maintainers. We follow a strict code quality standard, including TypeScript typing, clean code, and comprehensive tests.

### Reporting Issues

If you find a bug or have a feature request, please open an issue in the [GitHub Issues](https://github.com/sindresorhus/got/issues) section.

---

## License

MIT License

> This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

Created by [Sindre Sorhus](https://sindresorhus.com)  
Project maintained by the [Sindresorhus team](https://github.com/sindresorhus)

- 📧 Questions? Email: [sindresorhus@protonmail.com](mailto:sindresorhus@protonmail.com)
- 🌐 Follow on Twitter: [@sindresorhus](https://twitter.com/sindresorhus)
- 📚 Documentation: [https://github.com/sindresorhus/got](https://github.com/sindresorhus/got)
- 💬 Join the community: [GitHub Discussions](https://github.com/sindresorhus/got/discussions)

> ✅ Sponsored by [Sindresorhus](https://sindresorhus.com) – A community-driven open-source project.