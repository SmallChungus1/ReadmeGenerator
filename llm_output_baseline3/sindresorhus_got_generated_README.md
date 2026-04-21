# got

## Description

A human-friendly and powerful HTTP request library for Node.js. It provides a simple, flexible interface for making HTTP requests with support for streaming, error handling, retries, and various response types.

## Features

- Makes HTTP requests with support for `GET`, `POST`, `PUT`, `DELETE`, and other methods
- Supports streaming responses and requests
- Built-in retry logic with configurable backoff and error conditions
- Automatic handling of redirects
- Response type support: `text`, `json`, `buffer`, and `unknown`
- Customizable request and response hooks
- Support for HTTP/2 via `http2-wrapper`
- Unix socket URL support
- Progress tracking for uploads and downloads
- Built-in support for decompression (gzip, deflate, br, zstd)
- Configurable timeouts and connection settings
- Extensible with custom handlers and request extensions

## Prerequisites / Requirements

- Node.js 22 or higher
- Requires the `node:http`, `node:https`, and `node:net` modules

## Installation

```bash
npm install got
```

## Usage

### Basic GET request

```js
import got from 'got';

const response = await got('https://api.example.com/data');
console.log(response.body);
```

### GET request with JSON response

```js
const response = await got('https://api.example.com/data', {
  responseType: 'json'
});
console.log(response.body);
```

### POST request with form data

```js
const response = await got.post('https://api.example.com/data', {
  body: {
    name: 'John Doe',
    age: 30
  }
});
```

### Streaming response

```js
const stream = got.stream('https://example.com/large-file');
stream.on('data', (chunk) => {
  console.log('Received chunk:', chunk);
});
stream.on('end', () => {
  console.log('Stream complete');
});
```

### Custom headers and authentication

```js
const response = await got('https://api.example.com/data', {
  headers: {
    'Authorization': 'Bearer token123',
    'Content-Type': 'application/json'
  },
  username: 'user',
  password: 'pass'
});
```

### Request with retry logic

```js
const response = await got('https://api.example.com/data', {
  retry: {
    limit: 3,
    methods: ['GET'],
    statusCodes: [500, 502, 503, 504]
  }
});
```

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with clear, descriptive messages
4. Push to the branch and open a pull request

Please ensure your changes are well-documented and pass all tests.

## License

MIT

## Contact / Authors

- [Sindre Sorhus](https://sindresorhus.com)
- Project maintained by the community at [github.com/sindresorhus/got](https://github.com/sindresorhus/got)