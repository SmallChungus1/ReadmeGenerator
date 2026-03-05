```markdown
# Apache PredictionIO Ruby SDK

[![Build Status](https://travis-ci.org/apache/predictionio-sdk-ruby.svg?branch=master)](https://travis-ci.org/apache/predictionio-sdk-ruby)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Description

Apache PredictionIO is an open-source machine learning server for developers and data scientists to create predictive engines for production environments. This gem provides a convenient Ruby interface to the Apache PredictionIO API, allowing developers to focus on application logic rather than the complexities of direct API interaction. This SDK enables easy integration with PredictionIO engines for event tracking and real-time predictions.

## Features

*   **Event API Integration:** Easily submit events to a PredictionIO instance for model training.
*   **Engine API Integration:**  Query trained PredictionIO engines for real-time predictions.
*   **Asynchronous and Synchronous Operations:** Supports both synchronous and asynchronous request/response handling for improved performance and responsiveness.
*   **HTTP/HTTPS Support:**  Works with both secure and non-secure connections to your PredictionIO server.
*   **Thread Safety:** Designed for multithreaded environments.
*   **Error Handling:**  Provides specific exception types for common API errors (e.g., `NotFoundError`, `BadRequestError`, `ServerError`).

## Installation

Add the gem to your `Gemfile`:

```ruby
gem 'predictionio'
```

Then run `bundle install`.

## Usage

Here's a basic example of how to use the PredictionIO Ruby SDK:

```ruby
require 'predictionio'

# Instantiate the EventClient
event_client = PredictionIO::EventClient.new(access_key: 1, apiurl: 'http://localhost:7070')

# Create a user event
response = event_client.create_event('register', 'user', 'foobar')

# Check the response code
if response.code == '201'
  puts "User event created successfully!"
else
  puts "Error creating user event: #{response.body}"
end

# Instantiate the EngineClient
engine_client = PredictionIO::EngineClient.new(apiurl: 'http://localhost:8000')

# Get predictions for a user
predictions = engine_client.send_query('uid' => 'foobar')

# Print the predictions
puts "Predictions: #{predictions}"
```

**Key Classes:**

*   `PredictionIO::EventClient`: For interacting with the Event API.  Used for sending events to track user behavior and data.
*   `PredictionIO::EngineClient`: For interacting with the Engine API. Used for making prediction requests.
*   `PredictionIO::AsyncRequest`: Represents an asynchronous HTTP request.
*   `PredictionIO::AsyncResponse`:  Represents the response to an asynchronous HTTP request.

## API Reference

Refer to the source code and comments within the `lib` directory for detailed information on each class and method.  In particular, review the comments in `lib/predictionio/event_client.rb` and `lib/predictionio/engine_client.rb` for specific method signatures, parameter descriptions, and return values.

## Configuration

The `PredictionIO::EventClient` and `PredictionIO::EngineClient` accept the following configuration options:

*   `access_key`:  Your PredictionIO access key.  Required for the EventClient.
*   `apiurl`: The URL to your PredictionIO instance (e.g., `http://localhost:7070` for the event server or `http://localhost:8000` for the engine server).
*   `threads`: The number of concurrent HTTP connections (threads) to use. Defaults to 1.
*   `thread_timeout`: The timeout (in seconds) for each HTTP connection. Defaults to 60 seconds.

## Dependencies

*   `json` (>= 1.8)
*   `activesupport` (~> 4.2)
*   `rspec` (~> 3.6.0) - For testing (development dependency)
*   `webmock` (~> 2.3.2) - For stubbing HTTP requests during testing (development dependency)
* `coveralls` - for automated test coverage reports (development dependency)

## Contributing

We welcome contributions! Please see the [Contribution Guidelines](CONTRIBUTING.md) for details on how to contribute code, documentation, or bug reports.

## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This software is developed as part of the Apache PredictionIO project: [http://predictionio.apache.org/](http://predictionio.apache.org/)