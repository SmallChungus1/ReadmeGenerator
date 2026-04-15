# Apache PredictionIO Ruby SDK

## Description

The Apache PredictionIO Ruby SDK provides a convenient and powerful interface to interact with the Apache PredictionIO machine learning server. This gem enables Ruby developers to easily send events, query predictions, and manage user and item data through RESTful APIs, all with support for both synchronous and asynchronous operations.

Built on top of HTTP/HTTPS, the SDK abstracts the complexity of direct API calls, offering a clean, idiomatic Ruby interface for integrating machine learning capabilities into applications. It supports high-performance asynchronous operations with automatic connection pooling, request retry, and timeout handling.

## Features

- **Event Management**: Create, update, and delete user and item events with full control over event properties and timestamps.
- **Asynchronous Operations**: Support for non-blocking, asynchronous requests with automatic response handling and reconnection.
- **Synchronous Operations**: Block-based methods for simple, straightforward use cases.
- **Batch Processing**: Efficiently send multiple events in a single batch request.
- **Error Handling**: Comprehensive exception handling for common API errors (e.g., not found, bad request, server errors).
- **Connection Pooling**: Background thread management for persistent HTTP connections, improving performance and reducing latency.
- **Automatic Retry & Reconnection**: Built-in network resilience with automatic retry on failures.
- **Flexible Event Types**: Support for various event types including `$set`, `$unset`, `$delete`, and user-item actions.
- **Event Exporting**: Ability to export events to a file for later import using the PredictionIO CLI.

## Installation

To install the PredictionIO Ruby SDK, use the RubyGems package manager:

```bash
gem install predictionio
```

Alternatively, if you are working with a Ruby project, add the gem to your `Gemfile`:

```ruby
gem 'predictionio'
```

Then execute:

```bash
bundle install
```

## Usage

### Basic Setup

```ruby
require 'predictionio'

# Initialize the Event Client with your access key
client = PredictionIO::EventClient.new('your-access-key')

# Record a user action (e.g., a rating)
begin
  result = client.record_user_action_on_item('rate', 'user123', 'item456', 'rating' => 4)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Error recording event: #{e.message}"
end

# Query predictions from a trained engine
engine_client = PredictionIO::EngineClient.new('http://localhost:8000')
begin
  result = engine_client.send_query('uid' => 'user123')
  puts "Prediction result: #{result}"
rescue PredictionIO::EngineClient::BadRequestError => e
  puts "Invalid query: #{e.message}"
rescue PredictionIO::EngineClient::NotFoundError => e
  puts "User not found: #{e.message}"
rescue PredictionIO::EngineClient::ServerError => e
  puts "Server error: #{e.message}"
end
```

### Asynchronous Operations (Non-blocking)

```ruby
# Create an asynchronous request
response = client.acreate_event('view', 'user', 'user123')

# Process the response later (after a delay or in a background thread)
begin
  result = response.get
  puts "Event created successfully: #{result.body}"
rescue StandardError => e
  puts "Request failed: #{e.message}"
end
```

### Batch Event Export

```ruby
# Export events to a file
exporter = PredictionIO::FileExporter.new('events.json')
exporter.create_event('view', 'user', 'user123', { 'eventTime' => Time.now.iso8601 })
exporter.create_event('purchase', 'item', 'item789', { 'amount' => 99.99 })
exporter.close
```

> **Note**: Ensure that your PredictionIO server is running and accessible at the specified URLs (typically `http://localhost:7070` for events and `http://localhost:8000` for engines). The SDK supports HTTPS as well.