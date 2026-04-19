# PredictionIO Ruby SDK

## Description

The PredictionIO Ruby SDK provides convenient access to the Apache PredictionIO API for Ruby programmers. This allows you to focus on application logic while leveraging the power of PredictionIO for machine learning.  It supports both synchronous and asynchronous requests.

## Features

*   Ruby SDK for Apache PredictionIO
*   Synchronous and asynchronous request methods
*   Support for creating events and recording user actions
*   Handles network reconnection and request retries automatically

## Prerequisites / Requirements

*   Ruby >= 2.0
*   Gemfile dependencies: `coveralls`, `rspec~> 3.6.0`, `webmock~> 2.3.2`, `rdoc~> 4.0.0`, `activesupport~> 4.2`
*   Apache PredictionIO server running (default: `http://localhost:8000` or `http://localhost:7070`)

## Installation

```bash
gem install predictionio
```

## Usage

```ruby
require 'predictionio'

client = PredictionIO::EventClient.new('YOUR_ACCESS_KEY')

# Example: Record a user action
begin
  result = client.record_user_action_on_item('rate', 'foouser', 'baritem', 'rating' => 4)
  puts "Result: #{result}"
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Error: #{e}"
end
```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

## License

Apache License, Version 2.0 (See NOTICE file for details)

## Contact / Authors

Apache PredictionIO Team