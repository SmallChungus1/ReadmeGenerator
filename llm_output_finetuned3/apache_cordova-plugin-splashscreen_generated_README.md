# Cordova Splashscreen Plugin

## Description

The Cordova Splashscreen Plugin provides functionality to display and hide a splash screen during application launch in browser-based Cordova applications. It is designed to work with the Cordova browser platform and exposes a simple API for showing and hiding the splash screen.

## Features

- Displays a splash screen when the application starts.
- Hides the splash screen when requested.
- Uses a default image path (`/img/logo.png`) and dimensions (170x200 pixels).
- Supports configuration via `config.xml` preferences.
- Exposes `navigator.splashscreen` API for use in JavaScript.

## Prerequisites / Requirements

- Cordova 2.0.0 or later (with specific version constraints as defined in `package.json`).
- Cordova browser platform.
- A valid `config.xml` file with splash screen preferences.

## Installation

To install the plugin, use the Cordova CLI:

```bash
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

## Usage

The plugin exposes a `navigator.splashscreen` object with two methods:

- `show()` – Displays the splash screen.
- `hide()` – Hides the splash screen.

### Example Usage

```javascript
// Show splash screen
navigator.splashscreen.show();

// Hide splash screen
navigator.splashscreen.hide();
```

### Configuration

Splash screen behavior can be configured in `config.xml` using preferences:

```xml
<preference name="ShowSplashScreen" value="true" />
<preference name="SplashScreenDelay" value="3000" />
```

- `ShowSplashScreen`: Controls whether the splash screen is shown (default: `true`).
- `SplashScreenDelay`: Delay in milliseconds before hiding the splash screen (default: `3000` ms).

> Note: The plugin uses `cordova/exec` to communicate with the underlying platform. The actual splash screen image is loaded from the default path `/img/logo.png`.

## Contributing

Contributions are welcome. Please follow the Apache Software Foundation contribution guidelines.

- Fork the repository.
- Create a feature branch.
- Commit changes with clear messages.
- Open a pull request.

For issues or feature requests, please open an issue at:  
[https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)

## License

Apache License, Version 2.0

## Contact / Authors

Apache Software Foundation  
Project maintainers: Apache Cordova Team  
Issue reporting: [https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)