# got

![Build Status](https://github.com/sindresorhus/got/workflows/CI/badge.svg)
![Version](https://img.shields.io/npm/v/got.svg)
![License](https://img.shields.io/npm/l/got.svg)
![Downloads](https://img.shields.io/npm/dm/got.svg)

A human-friendly and powerful HTTP request library for Node.js. Built with simplicity, performance, and developer experience in mind.

> ✅ **Simple syntax** like `got('https://example.com')`  
> ✅ **Supports all HTTP methods** (GET, POST, PUT, DELETE, etc.)  
> ✅ **Streaming support** for large responses  
> ✅ **Built-in retry logic** with exponential backoff  
> ✅ **Automatic content decoding** (JSON, text, buffer)  
> ✅ **Extensible** with hooks and custom handlers  

---

## Description

`got` is a modern, lightweight HTTP client for Node.js that provides a clean, intuitive API for making HTTP requests. It combines the simplicity of `curl` or `wget` with the power and flexibility of modern HTTP libraries like `axios` or `ky`.

Unlike traditional HTTP clients, `got` is designed to be **human-friendly** — it handles common edge cases automatically (like redirects, timeouts, and retries) while remaining easy to use and understand. It supports both promise-based and stream-based responses, making it ideal for both simple scripts and complex applications.

Whether you're fetching data from APIs, scraping web pages, or building internal services, `got` gives you the tools to do it efficiently and reliably.

---

## Features

- ✅ **Simple, readable syntax** — `got('https://example.com')`
- ✅ **Supports all HTTP methods** (GET, POST, PUT, DELETE, PATCH, etc.)
- ✅ **Streaming responses** for large files or data streams
- ✅ **Automatic content type parsing** (JSON, text, buffer)
- ✅ **Built-in retry logic** with configurable backoff strategies
- ✅ **Supports HTTP/2 via `http2-wrapper`**
- ✅ **Extensible via hooks and custom handlers**
- ✅ **Automatic redirect handling** with configurable follow behavior
- ✅ **Progress tracking** for uploads and downloads
- ✅ **Custom headers, authentication, and cookies**
- ✅ **Supports pagination and rate limiting**
- ✅ **Built-in diagnostics and error handling**

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

- **Node.js v22+** (required due to ES2024 support)
- **npm** or **pnpm** (for package management)
- Basic understanding of JavaScript/TypeScript

> ⚠️ `got` requires Node.js v22 or higher due to its use of modern JavaScript features (e.g., `es2024`, `async/await`, and `TypedArrays`).

---

## Installation

Install `got` via npm:

```bash
npm install got
```

Or with pnpm:

```bash
pnpm add got
```

For development (with TypeScript support):

```bash
npm install got --save-dev
```

> ✅ The library is fully compatible with both **ESM** and **CommonJS** modules.

---

## Usage

### Basic GET Request

```ts
import got from 'got';

const response = await got('https://jsonplaceholder.typicode.com/posts/1');
console.log(response.body);
//=> { userId: 1, id: 1, title: 'sunt aut facere repellat provident occaecati...', body: 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum' }
```

### POST Request with JSON Body

```ts
import got from 'got';

const response = await got.post('https://jsonplaceholder.typicode.com/posts', {
  json: {
    title: 'My post',
    body: 'This is the body',
    userId: 1
  }
});

console.log(response.body);
```

### Streaming Response

```ts
import got from 'got';

const stream = await got.stream('https://example.com/large-file.zip');
stream.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes`);
});
stream.on('end', () => {
  console.log('Download complete');
});
```

### With Custom Headers

```ts
const response = await got('https://example.com', {
  headers: {
    'User-Agent': 'MyApp/1.0',
    'Authorization': 'Bearer token123'
  }
});
```

---

## Examples

See the full examples in the [documentation/examples](https://github.com/sindresorhus/got/tree/main/documentation/examples) directory.

### 1. GitHub API with Rate Limiting

```js
import got from 'got';

const instance = got.extend({
  prefixUrl: 'https://api.github.com',
  headers: {
    'User-Agent': 'github-got/1.0'
  },
  hooks: {
    init: [
      (raw, options) => {
        if (raw.token) {
          options.context.token = raw.token;
          delete raw.token;
        }
      }
    ],
    response: [
      (response) => {
        response.rateLimit = {
          limit: parseInt(response.headers['x-ratelimit-limit'], 10),
          remaining: parseInt(response.headers['x-ratelimit-remaining'], 10),
          reset: new Date(parseInt(response.headers['x-ratelimit-reset'], 10) * 1000)
        };
      }
    ]
  }
});

const {body} = await instance.get('/users/octocat');
console.log(body);
```

### 2. Pagination with Backoff

```js
const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
  pagination: {
    paginate({response, currentItems}) {
      return {
        searchParams: {
          page: Number(response.request.options.searchParams.get('page')) + 1
        }
      };
    },
    transform: response => response.body,
    countLimit: 50,
    backoff: 1000,
    requestLimit: 10
  }
});

for await (const commit of iterator) {
  console.log(commit.commit.message);
}
```

### 3. HTTP/2 with H2C

```js
import http2 from 'http2-wrapper';
import got from 'got';

const sessions = {};
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
server.listen(() => {
  const {body, headers} = await instance(`http://localhost:${server.address().port}`, {context: {h2c: true}});
  console.log(headers, body);
});
```

---

## Contributing

We welcome contributions from the community! Please follow these guidelines:

1. ✅ Open an issue to discuss a feature or bug
2. ✅ Fork the repository and create a feature branch
3. ✅ Make your changes and ensure they pass all tests
4. ✅ Submit a pull request with a clear description

See the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed instructions.

> 🚀 We use **TypeScript**, **AVA**, and **benchmarking** to ensure code quality and performance.

---

## License

MIT License

> See [LICENSE](LICENSE) for full details.

---

## Contact / Authors

- **Author**: [Sindre Sorhus](https://sindresorhus.com)
- **GitHub**: [@sindresorhus](https://github.com/sindresorhus)
- **Website**: [sindresorhus.com](https://sindresorhus.com)
- **Support**: [GitHub Discussions](https://github.com/sindresorhus/got/discussions)

💬 Want to contribute? Reach out on [Twitter/X](https://twitter.com/sindresorhus) or join the community on [Discord](https://discord.gg/sindresorhus).

> 💡 `got` is part of the [Sindre Sorhus](https://sindresorhus.com) collection of small, powerful, and well-maintained libraries.