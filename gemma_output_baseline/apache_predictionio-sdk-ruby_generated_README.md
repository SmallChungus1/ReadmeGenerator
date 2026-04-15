# PredictionIO Ruby SDK

[![Build Status](https://travis-ci.org/apache/predictionio-sdk-ruby.svg?branch=master)](https://travis-ci.org/apache/predictionio-sdk-ruby)

Apache PredictionIO Ruby SDK provides convenient access to the Apache PredictionIO API for Ruby programmers, allowing you to focus on application logic.

## Description

This gem provides a Ruby interface for interacting with Apache PredictionIO, an open-source machine learning server. It enables developers to create predictive engines for production environments and manage events, users, and items.  This SDK supports both synchronous and asynchronous requests for efficient interaction with the PredictionIO platform.

## Features

*   **Event API Access:**  Easily import user actions and data into PredictionIO.
*   **Engine API Access:** Query trained engines for predictions.
*   **Asynchronous Support:**  Non-blocking requests for improved performance.
*   **User and Item Management:** Create, update, and delete user and item profiles.
*   **RESTful Interface:**  Leverages standard REST principles for communication.
*   **Comprehensive Error Handling:**  Provides specific exception types for common errors.
*   **File Exporting:**  Export events for offline import.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Ruby >= 2.0
*   A running Apache PredictionIO instance.

## Installation

1.  Add the gem to your `Gemfile`:

    ```ruby
    gem 'predictionio'
    ```

2.  Run `bundle install`:

    ```bash
    bundle install
    ```

## Usage

Here are a few examples of how to use the PredictionIO Ruby SDK:

**1. Initialize the Event Client:**

```ruby
require 'predictionio'

client = PredictionIO::EventClient.new('your_access_key')
```

**2. Record a User Action:**

```ruby
begin
  result = client.record_user_action_on_item('rate', 'user123', 'item456', 'rating' => 4)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Error recording event: #{e.message}"
end
```

**3. Set User Properties:**

```ruby
begin
  result = client.set_user('user123', 'name' => 'John Doe', 'age' => 30)
rescue PredictionIO::EventClient::NotCreatedError => e
  puts "Error setting user properties: #{e.message}"
end
```

**4. Initialize the Engine Client:**

```ruby
require 'predictionio'

engine_client = PredictionIO::EngineClient.new
```

**5. Query the Engine for Predictions:**

```ruby
begin
  result = engine_client.send_query('uid' => 'user123')
  puts result
rescue PredictionIO::EngineClient::NotFoundError => e
  puts "Error querying engine: #{e.message}"
rescue PredictionIO::EngineClient::BadRequestError => e
  puts "Bad Request Error: #{e.message}"
rescue PredictionIO::EngineClient::ServerError => e
  puts "Server Error: #{e.message}"
end
```

## Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## Contact / Authors

*   **Authors:** Apache PredictionIO Team
*   **Email:** user@predictionio.apache.org
*   **Website:** http://predictionio.apache.org