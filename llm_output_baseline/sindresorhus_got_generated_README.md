# got

## Description

**got** is a human-friendly and powerful HTTP request library for Node.js. It provides a simple, intuitive API that seamlessly handles HTTP/HTTPS requests, supports streaming, automatic retries, pagination, and advanced features like request transformation, response parsing, and custom headers. Built with performance and developer experience in mind, got offers a robust alternative to popular libraries like `axios`, `superagent`, and `node-fetch`, with full support for modern HTTP/2 and compression protocols.

## Features

- ✅ **Simple & Intuitive API** – Makes HTTP requests as easy as `got('https://example.com')`
- ✅ **Streaming Support** – Handle large responses with `got.stream()`
- ✅ **Automatic Retries** – Configurable retry logic with exponential backoff
- ✅ **Pagination Support** – Easily iterate through paginated APIs
- ✅ **Response Parsing** – Automatic JSON, text, or buffer parsing with `responseType`
- ✅ **Request Transformation** – Extend functionality with custom hooks and handlers
- ✅ **Advanced Headers** – Set and manipulate headers, including case-sensitive transformations
- ✅ **HTTP/2 Support** – Native support for HTTP/2 via `http2-wrapper`
- ✅ **Compression Support** – Automatic handling of gzip, deflate, br, and zstd
- ✅ **Error Handling** – Comprehensive error types with detailed context
- ✅ **Performance Optimized** – Built with low-level Node.js primitives for speed

## Installation

```bash
npm install got
```

## Usage

### Basic GET Request

```ts
import got from 'got';

const response = await got('https://api.github.com/users/octocat');
console.log(response.body);
```

### GET Request with JSON Parsing

```ts
import got from 'got';

const {data} = await got('https://api.github.com/users/octocat').json();
console.log(data);
```

### POST Request with Form Data

```ts
import got from 'got';

const response = await got.post('https://httpbin.org/post', {
  form: {
    name: 'John Doe',
    age: 30
  }
});
console.log(response.body);
```

### Streaming Response

```ts
import got from 'got';

const stream = await got.stream('https://httpbin.org/stream/10');
stream.on('data', (chunk) => {
  console.log('Received chunk:', chunk);
});
stream.on('end', () => {
  console.log('Stream complete');
});
```

### Custom Headers and Authentication

```ts
import got from 'got';

const response = await got('https://api.example.com', {
  headers: {
    'Authorization': 'Bearer your-token',
    'User-Agent': 'MyApp/1.0'
  },
  responseType: 'json'
});
```

### Advanced Configuration with Custom Handlers

```ts
import got from 'got';

const instance = got.extend({
  hooks: {
    beforeRequest: [
      (options) => {
        options.headers['X-Custom-Header'] = 'value';
      }
    ],
    afterResponse: [
      (response) => {
        response.headers['X-Processed'] = 'true';
      }
    ]
  }
});

const response = await instance('https://api.example.com');
```

### Pagination Example

```ts
import got from 'got';

const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
  pagination: {
    paginate({response, currentItems}) {
      return {
        searchParams: {
          page: Number(response.request.options.searchParams.get('page') ?? 1) + 1
        }
      };
    },
    transform: response => response.body,
    countLimit: 50,
    backoff: 1000
  }
});

for await (const commit of iterator) {
  console.log(commit.commit.message);
}
```