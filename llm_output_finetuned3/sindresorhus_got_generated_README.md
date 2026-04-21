# got

Human-friendly and powerful HTTP request library for Node.js.

## Description

`got` is a lightweight, feature-rich HTTP client for Node.js that provides a simple and intuitive API for making HTTP requests. It supports both synchronous and asynchronous operations, includes built-in support for streaming, retries, redirects, and response parsing, and offers a clean interface for handling common HTTP tasks.

## Features

- Makes HTTP requests with a simple, readable API.
- Supports streaming responses and bodies.
- Built-in retry logic with configurable backoff strategies.
- Automatic handling of redirects (with optional follow logic).
- Response parsing with support for JSON, text, and buffer types.
- Customizable request options and headers.
- Built-in support for HTTP/2 via `http2-wrapper`.
- Pagination support with `got.paginate`.
- Extensible via `got.extend()` for adding custom behavior.
- Comprehensive error handling with specific error types.

## Prerequisites / Requirements

- Node.js version **22 or higher**.

## Installation

```bash
npm install got
```

## Usage

### Basic GET request

```ts
import got from 'got';

const response = await got('https://api.example.com/data');
console.log(response.body);
```

### POST request with JSON body

```ts
import got from 'got';

const response = await got.post('https://api.example.com/data', {
  json: { name: 'John', age: 30 }
});
console.log(response.body);
```

### Streaming response

```ts
import got from 'got';

const stream = await got.stream('https://example.com/large-file');
stream.on('data', (chunk) => {
  console.log(chunk);
});
```

### Using with pagination

```ts
import got from 'got';

const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
  pagination: {
    paginate({ response, currentItems }) {
      return {
        searchParams: { page: Number(response.request.options.searchParams.get('page')) + 1 },
      };
    },
    transform: response => response.body,
    countLimit: 50,
  },
});

for await (const item of iterator) {
  console.log(item);
}
```

### Extending with custom behavior

```ts
import got from 'got';

const instance = got.extend({
  headers: {
    'User-Agent': 'MyApp/1.0'
  },
  hooks: {
    beforeRequest: [
      (options) => {
        options.headers['X-Custom'] = 'value';
      }
    ]
  }
});

const response = await instance('https://api.example.com');
```

## Contributing

Contributions are welcome. Please open an issue or submit a pull request for any improvements or bug fixes.

## License

MIT

## Contact / Authors

- [Sindre Sorhus](https://sindresorhus.com)  
  Original author and maintainer of `got`.  
  Repository: [github.com/sindresorhus/got](https://github.com/sindresorhus/got)  
  Funding: [https://github.com/sindresorhus/got?sponsor=1](https://github.com/sindresorhus/got?sponsor=1)