# Apache PredictionIO Ruby SDK

![Build Status](https://travis-ci.org/apache/predictionio-sdk-ruby.svg?branch=master)
![Version](https://img.shields.io/github/v/release/apache/predictionio-sdk-ruby.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

A Ruby SDK for the [Apache PredictionIO](http://prediction.io) machine learning server, enabling developers to easily integrate predictive analytics into their applications using simple, high-performance REST APIs.

---

## Description

The Apache PredictionIO Ruby SDK provides a convenient, robust interface to the PredictionIO machine learning platform. It allows Ruby developers to send user events, manage user and item data, and retrieve predictions from trained models—all through simple, idiomatic Ruby code.

This SDK is designed to work seamlessly with the PredictionIO server, which runs as a standalone service that can be deployed on any platform. It supports both synchronous and asynchronous request patterns, with built-in handling of network reconnections, request retries, and timeouts to ensure reliable performance in production environments.

Whether you're building a recommendation engine, a personalized content feed, or a user behavior analysis system, this SDK simplifies the integration of machine learning capabilities into your Ruby applications.

---

## Features

- ✅ **Asynchronous & Synchronous Requests**: Both blocking and non-blocking methods are available for flexible performance needs.
- ✅ **Built-in Error Handling**: Automatic handling of network failures, timeouts, and HTTP error codes (e.g., 404, 400, 500).
- ✅ **Support for All PredictionIO Events**: Full support for user, item, and action events with rich metadata.
- ✅ **High-Performance Backend**: Uses multithreaded HTTP connections with automatic reconnection and retry logic.
- ✅ **Easy Integration**: Simple API design that mirrors standard Ruby idioms and patterns.
- ✅ **Flexible Configuration**: Customizable API endpoints, connection threads, and timeouts.
- ✅ **Batch Event Support**: Efficiently send multiple events in a single request.
- ✅ **Event Exporting**: Export data to files for later import into PredictionIO using `pio import`.

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

- **Ruby version**: 2.0 or higher (recommended: 2.7+)
- **RubyGems**: Version 2.0 or higher
- **PredictionIO Server**: Must be running locally or remotely (typically on ports 7070 for events and 8000 for engine API)

> ⚠️ The PredictionIO server must be installed and running before using this SDK. Download and install it from [http://prediction.io](http://prediction.io).

---

## Installation

To install the PredictionIO Ruby SDK, use RubyGems:

```bash
gem install predictionio
```

Alternatively, if you're managing dependencies via a `Gemfile`:

```ruby
# Gemfile
gem 'predictionio'
```

Then run:

```bash
bundle install
```

> 💡 The SDK is compatible with Ruby 2.0 and above. It requires the `json` gem (version ≥ 1.8), which is included in most Ruby installations.

---

## Usage

### 1. Basic Setup

First, include the SDK in your Ruby application:

```ruby
require 'predictionio'
```

Create an `EventClient` to send events to the PredictionIO server:

```ruby
client = PredictionIO::EventClient.new('your-access-key', 'http://localhost:7070')
```

> Replace `'your-access-key'` with your actual access key from the PredictionIO server UI.

### 2. Record a User Action (Synchronous)

```ruby
begin
  result = client.record_user_action_on_item('rate', 'user123', 'item456', { 'rating' => 4 })
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Failed to record event: #{e.message}"
end
```

### 3. Set User Properties (Asynchronous)

```ruby
response = client.aset_user('user123', { 'age' => 30, 'city' => 'New York' })
# Process response in background
begin
  result = client.set_user(response)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "User update failed: #{e.message}"
end
```

### 4. Query Predictions from Engine (Synchronous)

```ruby
client = PredictionIO::EngineClient.new('http://localhost:8000')

begin
  result = client.send_query({ 'uid' => 'user123' })
  puts "Prediction result: #{result}"
rescue PredictionIO::EngineClient::BadRequestError => e
  puts "Invalid query: #{e.message}"
rescue PredictionIO::EngineClient::NotFoundError => e
  puts "User not found: #{e.message}"
rescue PredictionIO::EngineClient::ServerError => e
  puts "Server error: #{e.message}"
end
```

### 5. Export Events to File

```ruby
exporter = PredictionIO::FileExporter.new('events.json')

exporter.create_event('view', 'item', 'item123', { 'eventTime' => Time.now.iso8601 })
exporter.create_event('purchase', 'user', 'user123', { 'amount' => 99.99 })

exporter.close
```

> The exported file can be imported into PredictionIO using the `pio import` command.

---

## Contributing

We welcome contributions to improve the stability, documentation, and usability of this SDK.

- **Report bugs**: Open an issue on GitHub.
- **Submit feature requests**: Describe your use case in a new issue.
- **Contribute code**: Fork the repository and submit a pull request with clear documentation and tests.

For detailed contribution guidelines, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file (to be created).

> This project follows the [Apache License 2.0](LICENSE) and is maintained by the Apache PredictionIO community.

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Project Maintainer**: Apache PredictionIO Team  
- **Email**: user@predictionio.apache.org  
- **Website**: [http://prediction.io](http://prediction.io)  
- **GitHub**: [https://github.com/apache/predictionio-sdk-ruby](https://github.com/apache/predictionio-sdk-ruby)

For support or questions, please visit the [PredictionIO Community Forum](https://community.prediction.io) or contact the team directly.