# Apache PredictionIO Ruby SDK

## Description

The Apache PredictionIO Ruby SDK provides a convenient, high-performance interface to the Apache PredictionIO machine learning server. This gem enables Ruby developers to interact with PredictionIO's Event and Engine APIs using simple, intuitive methods, allowing them to build predictive applications in production environments.

The SDK supports both synchronous and asynchronous request patterns, with automatic network reconnection and request retry handling. It abstracts the complexity of HTTP/HTTPS communication, allowing developers to focus on application logic rather than low-level networking details.

## Features

- **Event Management**: Create, update, delete, and track user and item events with support for rich metadata.
- **Asynchronous Operations**: Non-blocking requests that return immediately with a `PredictionIO::AsyncResponse` object for later processing.
- **Synchronous Operations**: Blocking requests that wait for a response before continuing execution.
- **High-Performance Backend**: Built-in multithreaded HTTP client with persistent connections and automatic retry logic.
- **Error Handling**: Comprehensive exception handling for common HTTP errors like 400, 404, and 500 responses.
- **Batch Operations**: Support for batch event creation to improve performance when processing large volumes of data.
- **Data Export**: Export events to a file for later import using the `pio import` command.

## Installation

Install the PredictionIO Ruby SDK via RubyGems:

```bash
gem install predictionio
```

Alternatively, add it to your project's `Gemfile`:

```ruby
gem 'predictionio'
```

Then run:

```bash
bundle install
```

## Usage

### Basic Setup

```ruby
require 'predictionio'

# Initialize the Event Client with your access key
client = PredictionIO::EventClient.new('your-access-key')

# Initialize the Engine Client (optional)
engine_client = PredictionIO::EngineClient.new('http://localhost:8000')
```

### Recording User Actions

```ruby
# Record a user rating for an item
begin
  result = client.record_user_action_on_item(
    'rate', 
    'user123', 
    'item456', 
    rating: 4
  )
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Failed to record action: #{e.message}"
end
```

### Setting User Properties

```ruby
# Set user properties asynchronously
response = client.aset_user('user123', {
  age: 30,
  city: 'New York'
})

# Retrieve the result synchronously
begin
  result = client.set_user(response)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "User update failed: #{e.message}"
end
```

### Querying Predictions

```ruby
# Send a query to an engine for predictions
begin
  result = engine_client.send_query({ uid: 'user123' })
rescue PredictionIO::EngineClient::NotFoundError => e
  puts "User not found: #{e.message}"
rescue PredictionIO::EngineClient::BadRequestError => e
  puts "Invalid query: #{e.message}"
rescue PredictionIO::EngineClient::ServerError => e
  puts "Server error: #{e.message}"
end
```

### Batch Event Creation

```ruby
# Create multiple events in a batch
events = [
  { event: 'view', entityType: 'item', entityId: 'item1', eventTime: DateTime.now.iso8601 },
  { event: 'purchase', entityType: 'item', entityId: 'item2', eventTime: DateTime.now.iso8601 }
]

batch_response = client.create_batch_event(events)

# Handle the response
begin
  result = client.create_batch_event(batch_response)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Batch creation failed: #{e.message}"
end
```

### Exporting Events to File

```ruby
# Export events to a file
exporter = PredictionIO::FileExporter.new('events.json')

exporter.create_event('view', 'item', 'item1', {
  eventTime: DateTime.now.iso8601,
  source: 'mobile'
})

exporter.create_event('purchase', 'user', 'user1', {
  eventTime: DateTime.now.iso8601,
  amount: 99.99
})

exporter.close
```

> **Note**: The SDK supports both synchronous and asynchronous methods. When using asynchronous methods, you receive a `PredictionIO::AsyncResponse` object immediately. You can later call `.get` on this object to retrieve the response when it becomes available.