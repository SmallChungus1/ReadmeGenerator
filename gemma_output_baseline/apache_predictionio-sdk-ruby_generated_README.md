# Apache PredictionIO Ruby SDK

[![Build Status](https://travis-ci.org/apache/predictionio-sdk-ruby.svg?branch=master)](https://travis-ci.org/apache/predictionio-sdk-ruby)

## Description

Apache PredictionIO is an open source machine learning server for developers and data scientists to create predictive engines for production environments. This gem provides convenient access to the Apache PredictionIO API for Ruby programmers so that you can focus on application logic. This SDK facilitates interaction with the Event API and Engine Instances.

## Features

*   **Asynchronous & Synchronous API Access:** Offers both blocking (synchronous) and non-blocking (asynchronous) methods for interacting with the PredictionIO API.
*   **Event API Client:**  Provides a client for sending events to the PredictionIO Event Server, allowing for training data import.  Supports user and item events, property setting, unsetting, and deletion.
*   **Engine API Client:**  Enables querying trained Engine Instances to retrieve predictions.
*   **HTTP Connection Pooling:** Manages a pool of HTTP connections for performance optimization.
*   **Error Handling:** Includes exception classes for common errors like `NotFoundError`, `BadRequestError`, and `ServerError`.

## Installation

Add the following line to your Gemfile:

```ruby
gem 'predictionio'
```

Then, execute:

```bash
bundle install
```

## Usage

### Initializing Clients

**Event Client:**

```ruby
require 'predictionio'

access_key = 1
event_client = PredictionIO::EventClient.new(access_key)
```

**Engine Client:**

```ruby
require 'predictionio'

engine_client = PredictionIO::EngineClient.new
```

### Event API Examples

**Creating an event:**

```ruby
response = event_client.create_event('pageview', 'user', 'user123', { 'page' => 'home' })
```

**Setting user properties:**

```ruby
response = event_client.set_user('user123', { 'age' => 30, 'location' => 'New York' })
```

**Recording a user action on an item:**

```ruby
response = event_client.record_user_action_on_item('view', 'user123', 'item456')
```

### Engine API Examples

**Sending a query:**

```ruby
predictions = engine_client.send_query('uid' => 'user123')
puts predictions # Typically returns a hash with prediction results
```

### Asynchronous Requests

For higher performance, you can use asynchronous requests.

```ruby
async_response = event_client.acreate_event('pageview', 'user', 'user123', { 'page' => 'home' })

# Do other work...

begin
  result = async_response.get
  puts "Event created successfully!"
rescue => e
  puts "Error creating event: #{e.message}"
end
```

## Contributing

See [CONTRIBUTING.md](link to contributing guide - not present in provided files, but good practice to include in a real repo) for information on how to contribute to this project.

## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Dependencies

*   activesupport (~> 4.2)
*   json (>= 1.8)
*   webmock (~> 2.3.2) - for testing

## Additional Information

*   **PredictionIO Website:** [http://predictionio.apache.org](http://predictionio.apache.org)
*   **Documentation:**  Official documentation can be found on the PredictionIO website.
*   **Source Code:** [https://github.com/apache/predictionio-sdk-ruby](https://github.com/apache/predictionio-sdk-ruby)