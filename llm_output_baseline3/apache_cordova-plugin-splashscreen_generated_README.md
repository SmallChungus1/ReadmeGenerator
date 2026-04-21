# Cordova Splashscreen Plugin

## Description

This plugin provides a splash screen interface for Cordova applications. It allows developers to display and hide a splash screen during app launch, improving user experience by showing a visual indicator while the app initializes.

The plugin is designed to work with the Cordova browser platform and exposes a `navigator.splashscreen` API for controlling the splash screen lifecycle.

## Features

- Displays a splash screen during app launch
- Hides the splash screen when the app is ready
- Configurable via `config.xml` preferences
- Works with the Cordova browser platform
- Exposes `navigator.splashscreen.show()` and `navigator.splashscreen.hide()` methods

## Prerequisites / Requirements

- Cordova CLI version 2.0.0 or later
- Cordova platform: `browser`
- Cordova dependencies:
  - For Cordova Android: `>=3.6.0` (with specific version constraints based on Cordova version)
  - For Cordova Windows: `>=4.4.0`
  - For Cordova iOS: `<6.0.0` (prior to version 6.0.0)
  - For Cordova version 8.0.0+: requires Cordova version >100 (likely a placeholder or version constraint)

## Installation

Install the plugin using the Cordova CLI:

```bash
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

Or via npm:

```bash
npm install cordova-plugin-splashscreen
```

Then add the browser platform:

```bash
cordova platform add browser
```

## Usage

The plugin exposes a `navigator.splashscreen` object with two methods:

```javascript
// Show the splash screen
navigator.splashscreen.show();

// Hide the splash screen
navigator.splashscreen.hide();
```

The splash screen is automatically shown by default during app launch and will hide after a configured delay (3000ms) unless explicitly hidden.

To customize behavior, configure preferences in `config.xml`:

```xml
<preference name="ShowSplashScreen" value="true" />
<preference name="SplashScreenDelay" value="3000" />
```

## Contributing

Contributions are welcome. Please follow the Apache Software Foundation contribution guidelines.

- Fork the repository on GitHub
- Create a feature branch
- Commit your changes with clear, descriptive messages
- Push to the branch and open a pull request

For issues or feature requests, please open an issue on the GitHub repository.

## License

Apache License, Version 2.0

## Contact / Authors

Apache Software Foundation  
Project maintainers: Apache Cordova Team  
Issue tracker: https://github.com/apache/cordova-plugin-splashscreen/issues  
Repository: https://github.com/apache/cordova-plugin-splashscreen