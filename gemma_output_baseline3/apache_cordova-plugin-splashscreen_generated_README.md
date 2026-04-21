# Apache Cordova Splashscreen Plugin

## Description

The Apache Cordova Splashscreen Plugin provides a splashscreen functionality for Cordova applications. It allows you to display a splash screen during application launch and hide it after a specified delay. This plugin is designed for use in browser-based Cordova applications.

## Features

*   Displays a splash screen during application launch.
*   Hides the splash screen after a specified delay.
*   Configurable splash screen image, background color, and position.
*   Supports automatic hiding of the splash screen.

## Prerequisites / Requirements

*   Apache Cordova
*   JavaScript environment compatible with the plugin.

## Installation

This plugin is included as part of the Apache Cordova distribution. No separate installation is required.

## Usage

The plugin provides the following methods:

*   `splashscreen.show()`: Displays the splash screen.
*   `splashscreen.hide()`: Hides the splash screen.

Example:

```javascript
// Display the splash screen
splashscreen.show();

// Hide the splash screen after 3 seconds
setTimeout(function() {
  splashscreen.hide();
}, 3000);
```

## Contributing

Contributions to this project are welcome. Please refer to the Apache Cordova documentation for details on how to contribute.

## License

This project is licensed under the Apache License, Version 2.0. See the `LICENSE` file for more information.

## Contact / Authors

Apache Software Foundation