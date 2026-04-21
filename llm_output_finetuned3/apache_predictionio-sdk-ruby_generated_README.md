# Apache PredictionIO Ruby SDK

## Description
The Apache PredictionIO Ruby SDK provides convenient access to the Apache PredictionIO API for Ruby programmers. It enables developers to interact with PredictionIO's Event and Engine APIs using REST calls, supporting both synchronous and asynchronous operations.

## Features
- Asynchronous HTTP request handling with automatic reconnection and retry
- Support for both synchronous and asynchronous methods
- High-performance backend with concurrent HTTP(S) connections
- Built-in error handling for common API responses (e.g., 404, 400, 500)
- Methods to create and manage user, item, and action events
- Support for batch event creation
- Data export functionality via file exporter

## Prerequisites / Requirements
- Ruby version 2.0 or higher
- `json` gem (version >= 1.8)
- `rspec` (version >= 3.6.0) for testing
- `webmock` (version >= 2.3.2) for testing
- `rdoc` (version >= 4.0.0)
- `activesupport` (version >= 4.2)

## Installation
Install the gem via RubyGems:

```bash
gem install predictionio
```

Or add to your Gemfile:

```ruby
gem 'predictionio'
```

Then run:

```bash
bundle install
```

## Usage

### Initialize Clients

```ruby
require 'predictionio'

# Event client (requires access key)
client = PredictionIO::EventClient.new('your-access-key')

# Engine client
engine_client = PredictionIO::EngineClient.new('http://your-predictionio-server:8000')
```

### Event Operations

#### Create a user event
```ruby
begin
  result = client.set_user('uid123', { 'name' => 'John Doe' })
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Error creating user: #{e.message}"
end
```

#### Record a user action
```ruby
begin
  result = client.record_user_action_on_item('rate', 'uid123', 'item456', { 'rating' => 4 })
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Error recording action: #{e.message}"
end
```

#### Create a batch of events
```ruby
events = [
  { event: 'view', entityType: 'item', entityId: 'item1', properties: { 'category' => 'electronics' } },
  { event: 'purchase', entityType: 'user', entityId: 'user2', properties: { 'amount' => 99.99 } }
]

begin
  result = client.create_batch_event(events)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Error creating batch events: #{e.message}"
end
```

### Engine Operations

#### Query an engine for predictions
```ruby
begin
  result = engine_client.send_query({ 'uid' => 'foobar' })
rescue PredictionIO::EngineClient::NotFoundError => e
  puts "User not found: #{e.message}"
rescue PredictionIO::EngineClient::BadRequestError => e
  puts "Invalid query: #{e.message}"
rescue PredictionIO::EngineClient::ServerError => e
  puts "Server error: #{e.message}"
end
```

### Asynchronous Operations
All methods have asynchronous counterparts that return an `AsyncResponse` object immediately. The response can be retrieved later using `.get()`.

```ruby
response = client.acreate_event('view', 'user', 'uid123')
# Process other work...
result = response.get
```

### Export Data to File
```ruby
exporter = PredictionIO::FileExporter.new('events.json')

exporter.create_event('view', 'item', 'item123', { 'category' => 'books' })
exporter.create_event('purchase', 'user', 'user456', { 'amount' => 29.99 })

exporter.close
```

## Contributing
Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

The project uses RSpec for testing. To run tests:

```bash
rake spec
```

## License
Apache License, Version 2.0

## Contact / Authors
- Apache PredictionIO Team
- Support: support@prediction.io
- Project homepage: http://predictionio.apache.org

This SDK is licensed under the Apache License, Version 2.0. See the LICENSE file for details.