# Cordova Plugin Splashscreen

A Cordova plugin to display and hide a splash screen during application launch.

## Description

This plugin provides a way to show a splash screen while your Cordova application is loading, and then hide it once the application is ready. It's designed to improve the user experience by providing visual feedback during the startup process. This plugin supports the browser platform.

## Features

*   Displays a splash screen during app launch.
*   Hides the splash screen programmatically.
*   Supports configuration via `config.xml`.
*   Browser platform support.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Cordova CLI installed.
*   Node.js and npm installed.

## Installation

1.  Add the plugin to your Cordova project:

    ```bash
    cordova plugin add cordova-plugin-splashscreen
    ```

2.  Configure the plugin in your `config.xml` file (optional, defaults are used if not configured):

    You can customize the splash screen's appearance and behavior through the following preferences in your `config.xml`:

    *   `ShowSplashScreen`:  (Boolean, default: `true`) Whether to show the splash screen.
    *   Other splash screen preferences (e.g., `SplashScreenDelay`, `SplashImageSrc`) are handled by the core Cordova splashscreen functionality. Refer to the [Cordova documentation](https://cordova.apache.org/docs/en/latest/reference/cordova-plugin-splashscreen/) for a complete list.

## Usage

After installing the plugin, you can use the `navigator.splashscreen` object to control the splash screen.

```javascript
// Show the splash screen (usually handled automatically on app start)
navigator.splashscreen.show();

// Hide the splash screen
navigator.splashscreen.hide();
```

## Contributing

We welcome contributions to the project! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to report bugs, submit feature requests, and contribute code.  You can also find information on the project's governance and community guidelines.

## License

This project is licensed under the [Apache License, Version 2.0](LICENSE).

## Contact / Authors

This project is maintained by the [Apache Software Foundation](https://www.apache.org/).

For questions or support, please visit the [GitHub issues page](https://github.com/apache/cordova-plugin-splashscreen/issues).