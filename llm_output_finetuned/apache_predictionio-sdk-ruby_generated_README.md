# Apache PredictionIO Ruby SDK

[![Build Status](https://travis-ci.org/apache/predictionio-sdk-ruby.svg?branch=master)](https://travis-ci.org/apache/predictionio-sdk-ruby)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

The official Ruby SDK for [Apache PredictionIO](http://prediction.io), an open-source machine learning server that enables developers and data scientists to build and deploy predictive engines in production environments.

This gem provides a clean, intuitive interface to interact with PredictionIO's Event and Engine APIs using Ruby. Whether you're recording user actions, setting user properties, or retrieving predictions, the SDK abstracts the underlying HTTP calls and handles connection management, retries, and error handling automatically.

---

## Description

Apache PredictionIO is a machine learning server designed to help developers integrate real-time prediction capabilities into their applications. The Ruby SDK simplifies access to PredictionIO's REST API by providing high-level, type-safe methods for recording events and retrieving predictions.

This SDK is ideal for Ruby developers who want to:
- Record user actions (e.g., clicks, ratings)
- Store user and item metadata
- Query prediction engines to generate personalized recommendations
- Export data for batch processing

The SDK supports both **synchronous** (blocking) and **asynchronous** (non-blocking) operations, with automatic retry logic and connection pooling for high performance and reliability.

---

## Features

- ✅ **Event Recording**: Record user actions, set user/item properties, and delete entities
- ✅ **Batch Processing**: Efficiently import large volumes of events in bulk
- ✅ **Asynchronous Operations**: Non-blocking requests with automatic response handling
- ✅ **Automatic Retry & Reconnection**: Handles network failures transparently
- ✅ **Built-in Error Handling**: Clear exceptions for common issues (e.g., 404, 400, 500)
- ✅ **High Performance**: Threaded HTTP connections for concurrent requests
- ✅ **Full API Coverage**: Access to all core PredictionIO Event and Engine APIs

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

- **Ruby** version 2.0 or higher
- **RubyGems** (version 2.0+)
- A running instance of [Apache PredictionIO](http://prediction.io) server
  - Event Server: `http://localhost:7070` (default)
  - Engine Server: `http://localhost:8000` (default)
- An **access key** for the PredictionIO Event Server (required for authentication)

---

## Installation

Install the PredictionIO Ruby SDK via RubyGems:

```bash
gem install predictionio
```

Alternatively, add it to your `Gemfile`:

```ruby
gem 'predictionio'
```

Then run:

```bash
bundle install
```

> 💡 **Note**: The SDK requires `json` (>= 1.8) and `net-http` (built-in) to be available. These are included in the gem dependencies.

---

## Usage

### 1. Basic Setup

```ruby
require 'predictionio'

# Create an EventClient with your access key
client = PredictionIO::EventClient.new(
  access_key: 'your-access-key-here',
  apiurl: 'http://localhost:7070'
)

# Create a user
client.set_user('user123', {
  name: 'John Doe',
  age: 30,
  city: 'New York'
})
```

### 2. Record a User Action

```ruby
begin
  client.record_user_action_on_item(
    'rate',
    'user123',
    'item456',
    rating: 5
  )
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Failed to record action: #{e.message}"
end
```

### 3. Query a Prediction Engine

```ruby
require 'predictionio'

client = PredictionIO::EngineClient.new('http://localhost:8000')

begin
  result = client.send_query(
    {
      'uid' => 'user123',
      'context' => {
        'device' => 'mobile',
        'location' => 'NYC'
      }
    }
  )
  puts "Prediction result: #{result}"
rescue PredictionIO::EngineClient::BadRequestError => e
  puts "Invalid query: #{e.message}"
rescue PredictionIO::EngineClient::NotFoundError => e
  puts "User not found: #{e.message}"
rescue PredictionIO::EngineClient::ServerError => e
  puts "Server error: #{e.message}"
end
```

### 4. Asynchronous Operations (Non-blocking)

```ruby
# Asynchronously create an event
response = client.acreate_event(
  'view',
  'user123',
  'item456',
  event_time: DateTime.now.iso8601
)

# Later, retrieve the result
begin
  result = client.set_user(response)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Event creation failed: #{e.message}"
end
```

### 5. Export Data to File

```ruby
exporter = PredictionIO::FileExporter.new('events.json')

exporter.create_event(
  'view',
  'user123',
  'item456',
  event_time: DateTime.now.iso8601
)

exporter.create_event(
  'purchase',
  'user123',
  'item789',
  amount: 99.99
)

exporter.close
```

> 🔍 **Tip**: For production use, always wrap event recording in `begin/rescue` blocks to handle network errors gracefully.

---

## Contributing

We welcome contributions to improve the Ruby SDK! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

Please ensure:
- All new code follows the existing style and naming conventions
- Tests are included where applicable
- Documentation is updated
- Code is properly formatted and commented

For bug reports or feature requests, please open an issue in the [GitHub Issues](https://github.com/apache/predictionio-sdk-ruby/issues) section.

> 📚 See the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed contribution guidelines.

---

## License

This project is licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

> You may use, modify, and distribute the code freely, provided that:
> - You include the original license notice
> - You do not remove or alter the attribution
> - You do not use the name "Apache PredictionIO" in a misleading way

---

## Contact / Authors

- **Project Maintainers**: Apache PredictionIO Team
- **Support Email**: support@prediction.io
- **Website**: [http://prediction.io](http://prediction.io)
- **GitHub**: [https://github.com/apache/predictionio-sdk-ruby](https://github.com/apache/predictionio-sdk-ruby)

For questions, feedback, or to report issues, please reach out via the official channels.