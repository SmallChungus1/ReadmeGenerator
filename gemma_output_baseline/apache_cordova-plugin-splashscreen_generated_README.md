```markdown
# Cordova Splashscreen Plugin

This plugin displays and hides a splash screen during application launch.

## Description

The Cordova Splashscreen plugin provides a simple way to display an image (or a solid background color) while your app is loading. This provides a better user experience by giving visual feedback that the application is starting.  It supports configuring the display duration and background color. The plugin is designed to work across multiple mobile platforms, with specific implementations for each platform. This repository specifically focuses on the browser implementation.

## Features

*   **Display a splash screen:** Shows a configured image or background color while the app loads.
*   **Configurable duration:** Control how long the splash screen is displayed.
*   **Customizable background color:**  Set the background color of the splash screen.
*   **Browser Support:**  Provides a browser implementation for testing and use in web environments.
*   **Auto Hide:** Optionally, the splash screen can be configured to automatically hide after a specified delay.
*   **Responsive sizing:**  Adjusts the splash screen image size to fit the screen.

## Installation

To install the plugin, use the Cordova CLI:

```bash
cordova plugin add cordova-plugin-splashscreen
```

After installing the plugin, you'll also need to configure it in your `config.xml` file to specify the splash screen image, background color, delay, and other parameters. Example:

```xml
<preference name="SplashScreen" value="resource-mdpi-port-land-hdpi" />
<preference name="SplashScreenDelay" value="3000" />
<preference name="SplashScreenBackgroundColor" value="#FFFFFF" />
<preference name="AutoHideSplashScreen" value="true" />
```

*   `SplashScreen`: The name of the image resource to use as the splash screen.
*   `SplashScreenDelay`: The duration (in milliseconds) to display the splash screen. Defaults to 3000ms.
*   `SplashScreenBackgroundColor`: The background color of the splash screen (e.g., `#FFFFFF` for white).
*   `AutoHideSplashScreen`: Whether or not the splashscreen should automatically hide after the delay (true/false).

## Usage

In your JavaScript code, you can use the `navigator.splashscreen` object to control the splash screen:

```javascript
// Show the splash screen
navigator.splashscreen.show();

// Hide the splash screen
navigator.splashscreen.hide();
```

## Browser Implementation Details

This repository contains the browser-specific implementation of the Splashscreen plugin, located in `src/browser/SplashScreenProxy.js`.  This implementation emulates the native splash screen functionality using HTML elements and CSS styling.  The `splashscreen.js` file within the `www` directory provides the JavaScript interface accessible via `navigator.splashscreen`.

## Testing

The `tests` directory contains unit tests for the browser implementation. You can run the tests using `npm test` within the `tests` directory after installing the project dependencies (`npm ci`).

## Contributing

Contributions are welcome!  Please follow the [Apache Cordova Contributing Guidelines](https://cordova.apache.org/contribute/).

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgements

This plugin is part of the Apache Cordova ecosystem and maintained by the Apache Software Foundation.
```