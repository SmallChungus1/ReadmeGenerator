# Apache PredictionIO Ruby SDK

## Description
The Apache PredictionIO Ruby SDK provides a convenient interface to the PredictionIO API for Ruby developers. It enables interaction with PredictionIO's Event and Engine services through HTTP/HTTPS requests, allowing developers to record user actions, manage user and item data, and retrieve predictions from trained models.

## Features
- Asynchronous and synchronous request methods for both event and engine operations
- Support for creating and managing user, item, and action events
- Built-in support for asynchronous requests with automatic retry and connection handling
- Automatic handling of network reconnection and request retry
- Support for batch event creation
- Export data to a file for later import using `pio import`

## Prerequisites / Requirements
- Ruby version 2.0 or higher
- The `json` gem (version >= 1.8) is required

## Installation
Install the SDK using RubyGems:

```bash
gem install predictionio
```

## Usage

### Initialize the Event Client
```ruby
require 'predictionio'

# Create an EventClient with access key and API endpoint
client = PredictionIO::EventClient.new('your-access-key', 'http://localhost:7070')
```

### Record a User Action
```ruby
begin
  # Synchronous method
  result = client.record_user_action_on_item('rate', 'user123', 'item456', 'rating' => 4)
rescue PredictionIO::EventClient::NotCreatedError => e
  # Handle error
end
```

### Use Asynchronous Requests
```ruby
# Asynchronously create an event
response = client.acreate_event('view', 'user', 'uid123', { 'eventTime' => Time.now.iso8601 })

# Retrieve the result later
begin
  result = response.get
rescue => e
  # Handle error
end
```

### Export Data to File
```ruby
exporter = PredictionIO::FileExporter.new('events.json')
exporter.create_event('view', 'user', 'uid123', { 'eventTime' => Time.now.iso8601 })
exporter.close
```

### Initialize Engine Client
```ruby
engine_client = PredictionIO::EngineClient.new('http://localhost:8000')
result = engine_client.send_query({ 'uid' => 'user123' })
```

## Contributing
Contributions are welcome. Please follow the Apache License 2.0 guidelines and submit pull requests with clear documentation and tests.

## License
Apache License, Version 2.0

## Contact / Authors
Apache PredictionIO Team  
Email: support@prediction.io  
Project Home: http://prediction.io

> **Note**: Pre-0.7.x series support is deprecated. Users are encouraged to migrate to version 0.8.x or later. The old client interface is retained for backward compatibility and will be removed in a future minor version.