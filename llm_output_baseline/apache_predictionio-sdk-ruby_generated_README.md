# Apache PredictionIO Ruby SDK

![Build Status](https://travis-ci.org/apache/predictionio-sdk-ruby.svg?branch=master)
![Version](https://img.shields.io/badge/version-0.12.1-blue.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

A Ruby SDK for interacting with the Apache PredictionIO machine learning server. This library provides a clean, intuitive interface to send events and make predictions using the PredictionIO REST API.

---

## Description

Apache PredictionIO is an open-source machine learning server that enables developers and data scientists to build and deploy predictive engines in production environments. The **PredictionIO Ruby SDK** simplifies integration by providing a Ruby-based interface to the PredictionIO Event and Engine APIs.

This SDK allows you to:
- Record user actions and events (e.g., clicks, purchases)
- Manage user and item properties
- Query prediction engines to generate personalized recommendations
- Export data for import into PredictionIO via the `pio import` command

Whether you're building a recommendation engine or a real-time analytics system, this SDK abstracts the complexity of HTTP requests, offering both synchronous and asynchronous methods for optimal performance.

---

## Features

- ✅ **Event Management**: Create, update, delete user and item properties with full event support (e.g., `$set`, `$unset`, `$delete`)
- ✅ **Action Recording**: Log user interactions with items (e.g., ratings, views)
- ✅ **Asynchronous Operations**: Non-blocking requests with automatic retry and connection handling
- ✅ **Synchronous & Asynchronous Methods**: Choose between blocking and non-blocking execution based on your application needs
- ✅ **Automatic Error Handling**: Comprehensive error types for common failure scenarios (e.g., 404, 400, 500)
- ✅ **Built-in Connection Pooling**: Efficiently manages HTTP connections with persistent threads
- ✅ **Flexible Configuration**: Customize API endpoints, timeout settings, and thread count
- ✅ **Data Export Support**: Export events to JSON files for later import into PredictionIO

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
- **RubyGems** (for installation)
- Apache PredictionIO server running locally or remotely (typically on ports 7070 for events and 8000 for engines)

> ⚠️ The PredictionIO server must be installed and running before using this SDK. You can download it from [http://prediction.io](http://prediction.io).

---

## Installation

Install the PredictionIO Ruby SDK using RubyGems:

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

> 💡 The SDK requires the `json` gem (version ≥ 1.8), which is included in most Ruby installations.

---

## Usage

### 1. Basic Setup

```ruby
require 'predictionio'

# Initialize the Event Client (for recording events)
client = PredictionIO::EventClient.new(
  access_key: 'your-access-key',
  apiurl: 'http://localhost:7070'
)

# Initialize the Engine Client (for making predictions)
engine_client = PredictionIO::EngineClient.new(
  apiurl: 'http://localhost:8000'
)
```

### 2. Record a User Action (Synchronous)

```ruby
begin
  result = client.record_user_action_on_item(
    action: 'rate',
    uid: 'user123',
    iid: 'item456',
    optional: {
      rating: 4,
      timestamp: Time.now.iso8601
    }
  )
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Failed to record event: #{e.message}"
end
```

### 3. Set User Properties (Asynchronous)

```ruby
# Asynchronously set user properties
response = client.aset_user('user123', {
  age: 30,
  city: 'San Francisco'
})

# Retrieve result when available
begin
  result = response.get
  puts "User updated successfully: #{result.body}"
rescue StandardError => e
  puts "Error: #{e.message}"
end
```

### 4. Make a Prediction (Synchronous)

```ruby
begin
  result = engine_client.send_query(
    {
      'uid' => 'user123'
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

### 5. Export Events to File

```ruby
exporter = PredictionIO::FileExporter.new('events.json')

exporter.create_event(
  event: 'view',
  entity_type: 'item',
  entity_id: 'item123',
  optional: {
    eventTime: Time.now.iso8601,
    source: 'mobile_app'
  }
)

exporter.close
```

---

## Contributing

We welcome contributions to improve the PredictionIO Ruby SDK! Please follow these guidelines:

- Fork the repository on GitHub
- Create a new feature branch (`feature/my-feature`)
- Commit your changes with descriptive messages
- Ensure all tests pass (if applicable)
- Submit a pull request with a clear description of your changes

For detailed contribution guidelines, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

> ❗ Note: This project is maintained by the Apache PredictionIO community. All contributions are subject to the [Apache License 2.0](LICENSE).

---

## License

This project is licensed under the **Apache License, Version 2.0**. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, feedback, or support:

- **Project Home**: [http://predictionio.apache.org](http://predictionio.apache.org)
- **Support Email**: user@predictionio.apache.org
- **Community**: Join the Apache PredictionIO mailing list or community forums
- **GitHub Repository**: [https://github.com/apache/predictionio-sdk-ruby](https://github.com/apache/predictionio-sdk-ruby)

The Apache Software Foundation is committed to open source collaboration and community-driven development.