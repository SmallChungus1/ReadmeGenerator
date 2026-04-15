# Got

**Human-friendly and powerful HTTP request library for Node.js**

Got is a modern, feature-rich HTTP client for Node.js that provides a clean, intuitive API for making HTTP requests. Inspired by the simplicity of `curl` and `wget`, it offers a robust foundation for handling both simple and complex network operations with built-in support for streaming, retries, pagination, and advanced request customization.

## Description

Got is a comprehensive HTTP client designed to simplify and streamline HTTP communication in Node.js applications. It supports all standard HTTP methods, provides seamless streaming capabilities, and includes intelligent retry logic, automatic pagination, and rich error handling. With a focus on developer experience, Got abstracts away the complexity of low-level HTTP operations while maintaining full control over request configuration and response processing.

## Features

- ✅ **Simple & intuitive API** resembling `curl` and `wget`
- ✅ **Streaming support** for large responses and file downloads
- ✅ **Automatic retries** with exponential backoff and configurable limits
- ✅ **Pagination support** with customizable logic and backoff
- ✅ **Response type flexibility** (text, JSON, buffer, raw)
- ✅ **Request customization** via hooks, headers, and context
- ✅ **Advanced features** including H2C support, Unix socket handling, and proxy configuration
- ✅ **Error handling** with detailed context and structured error objects
- ✅ **Performance optimizations** including connection pooling and caching
- ✅ **Full TypeScript support** with comprehensive type definitions
- ✅ **Extensible architecture** allowing for custom request processing and middleware

## Installation

Install Got using npm or yarn:

```bash
npm install got
```

or

```bash
yarn add got
```

## Usage

### Basic GET Request

```ts
import got from 'got';

const response = await got('https://api.github.com/users/octocat');
console.log(response.body);
```

### GET with JSON Response

```ts
import got from 'got';

const {data} = await got('https://api.github.com/users/octocat').json();
console.log(data.login);
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
stream.on('data', chunk => {
  console.log('Received chunk:', chunk);
});
stream.on('end', () => {
  console.log('Stream completed');
});
```

### Custom Headers and Context

```ts
import got from 'got';

const instance = got.extend({
  headers: {
    'User-Agent': 'MyApp/1.0',
    'Authorization': 'Bearer my-token'
  },
  context: {
    userId: '12345'
  }
});

const response = await instance('https://api.example.com/data');
console.log(response.headers);
```

### Pagination with Custom Logic

```ts
import got from 'got';

const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
  pagination: {
    paginate({response, currentItems}) {
      const {searchParams} = response.request.options;
      return {
        searchParams: {
          page: Number(searchParams.get('page') ?? 1) + 1
        }
      };
    },
    transform: response => response.body,
    countLimit: 50,
    backoff: 1000
  }
});

for await (const item of iterator) {
  console.log(item.commit.message);
}
```

### Rate Limiting and Error Handling

```ts
import got from 'got';

const instance = got.extend({
  hooks: {
    beforeRequest: [
      (options) => {
        options.headers['X-RateLimit-Reset'] = Date.now() + 60000;
      }
    ],
    afterResponse: [
      (response) => {
        if (response.headers['x-ratelimit-remaining'] === '0') {
          console.log('Rate limit reached!');
        }
      }
    ]
  }
});
```

### Advanced Configuration with Custom Options

```ts
import got from 'got';

const response = await got('https://httpbin.org/get', {
  method: 'GET',
  timeout: 5000,
  retry: {
    limit: 3,
    backoff: 1000,
    methods: ['GET', 'POST']
  },
  responseType: 'json',
  resolveBodyOnly: true
});

console.log(response.body);
```