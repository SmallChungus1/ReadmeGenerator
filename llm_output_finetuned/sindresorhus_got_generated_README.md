# Got

[![Build Status](https://img.shields.io/github/actions/workflow/status/sindresorhus/got/ci.yml?logo=github&logoColor=white)](https://github.com/sindresorhus/got/actions)
[![Version](https://img.shields.io/npm/v/got?logo=npm&logoColor=white)](https://www.npmjs.com/package/got)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/sindresorhus/got/blob/main/LICENSE)
[![Sponsored](https://img.shields.io/badge/sponsored-by-sindresorhus-ff69b4.svg)](https://github.com/sindresorhus/got?sponsor=1)

> A human-friendly and powerful HTTP request library for Node.js. Built with simplicity, performance, and developer experience in mind.

---

## Description

**Got** is a modern, feature-rich HTTP client for Node.js that provides a clean, intuitive API for making HTTP requests. It combines the best of `axios`, `superagent`, and `node-fetch` with native Node.js performance and robust error handling.

Got supports all standard HTTP methods, automatic redirects, streaming, response body parsing, request retries, and advanced configuration. It's designed to be easy to use while offering deep control over request behavior — perfect for both simple scripts and complex applications.

Whether you're fetching data from a REST API, downloading files, or working with streaming responses, Got handles the complexity behind the scenes so you can focus on your application logic.

---

## Features

- ✅ **Simple & readable API** — Use `got(url)` or `got(url, options)` like `fetch()`
- ✅ **Streaming support** — Handle large responses with `got.stream()`
- ✅ **Automatic redirects** — Follows 301, 302, 303, 307, and 308 redirects
- ✅ **Request retries** — Automatically retry failed requests with exponential backoff
- ✅ **Response parsing** — Automatically parse JSON, text, or buffers based on `responseType`
- ✅ **Progress tracking** — Monitor upload/download progress in real time
- ✅ **Headers and cookies** — Full control over request headers and cookie handling
- ✅ **HTTP/2 support** — Uses `http2-wrapper` for efficient HTTP/2 connections
- ✅ **Compression support** — Automatically decompress gzip, deflate, br, and zstd
- ✅ **Extensible** — Extend instances with custom handlers, hooks, and middleware
- ✅ **Pagination** — Easily paginate through large datasets with built-in support
- ✅ **Error handling** — Clear, structured errors with detailed context
- ✅ **Performance optimized** — Built on top of native Node.js modules for speed

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

Got requires **Node.js v22 or higher**.

```bash
node --version
# => v22.x.x or higher
```

---

## Installation

Install Got via npm or yarn:

```bash
npm install got
```

or

```bash
yarn add got
```

> Got is built with TypeScript and supports ES modules. It automatically resolves to the correct output format based on your project configuration.

---

## Usage

### Basic GET Request

```ts
import got from 'got';

const response = await got('https://api.github.com/users/octocat');
console.log(response.body);
```

### GET with JSON Response

```ts
const {data} = await got('https://jsonplaceholder.typicode.com/posts/1').json();
console.log(data.title);
```

### POST Request with JSON Body

```ts
const response = await got.post('https://httpbin.org/post', {
  json: {
    name: 'John Doe',
    age: 30
  }
});

console.log(response.body);
```

### Streaming Response

```ts
const stream = await got.stream('https://httpbin.org/stream/10');
stream.on('data', chunk => {
  console.log('Received chunk:', chunk.toString());
});
stream.on('end', () => {
  console.log('Stream complete');
});
```

### With Custom Headers

```ts
const response = await got('https://httpbin.org/headers', {
  headers: {
    'User-Agent': 'MyApp/1.0',
    'X-API-Key': 'abc123'
  }
});
```

### With Retry Logic

```ts
const response = await got('https://httpbin.org/delay/1', {
  retry: {
    limit: 3,
    backoff: 1000
  }
});
```

### Using Custom Handlers

```ts
const instance = got.extend({
  hooks: {
    beforeRequest: [
      (options) => {
        console.log(`Making request to ${options.url}`);
      }
    ],
    afterResponse: [
      (response) => {
        console.log(`Received status ${response.statusCode}`);
      }
    ]
  }
});

const response = await instance('https://httpbin.org/get');
```

### Pagination Example

```ts
const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
  pagination: {
    paginate({response, currentItems}) {
      const page = Number(response.request.options.searchParams.get('page') ?? 1);
      return { searchParams: { page: page + 1 } };
    },
    transform: response => response.body,
    countLimit: 50
  }
});

for await (const commit of iterator) {
  console.log(commit.commit.message);
}
```

---

## Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your help is appreciated.

### How to Contribute

1. Fork the repository
2. Create a new feature branch (`feature/your-feature`)
3. Commit your changes with clear, descriptive messages
4. Push to the branch and open a pull request

### Reporting Issues

Please open an issue on GitHub if you encounter a bug or have a feature request. Include:
- A clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Node.js version, OS)

> See the [CONTRIBUTING.md](https://github.com/sindresorhus/got/blob/main/CONTRIBUTING.md) file for detailed guidelines.

---

## License

MIT License — See [LICENSE](https://github.com/sindresorhus/got/blob/main/LICENSE) for details.

---

## Contact / Authors

**Created by:** [Sindre Sorhus](https://sindresorhus.com)

- 📧 Email: [sindresorhus@gmail.com](mailto:sindresorhus@gmail.com)
- 💬 Twitter: [@sindresorhus](https://twitter.com/sindresorhus)
- 🚀 GitHub: [github.com/sindresorhus](https://github.com/sindresorhus)
- 🌐 Website: [sindresorhus.com](https://sindresorhus.com)

Support this project? Consider becoming a sponsor on GitHub:  
👉 [https://github.com/sindresorhus/got?sponsor=1](https://github.com/sindresorhus/got?sponsor=1)