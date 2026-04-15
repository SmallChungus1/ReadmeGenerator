# Cordova Splashscreen Plugin

A Cordova plugin that enables the display and hiding of a splash screen during application launch in the browser platform.

## Description

The **Cordova Splashscreen Plugin** provides a simple interface to show and hide a splash screen in Cordova-based web applications running in the browser. This plugin is designed to work specifically with the browser platform and leverages Cordova's JavaScript API to manage the splash screen lifecycle. It is part of the Apache Cordova ecosystem and is licensed under the Apache License 2.0.

The plugin exposes a `navigator.splashscreen` object with two primary methods: `show()` to display the splash screen and `hide()` to dismiss it. It is particularly useful for maintaining a consistent user experience during app startup, especially when loading assets or initializing the application.

## Features

- ✅ Display a splash screen during app launch  
- ✅ Hide the splash screen when the app is ready  
- ✅ Works seamlessly with the Cordova browser platform  
- ✅ Fully compatible with Cordova 2.0+ and modern versions  
- ✅ Configurable via `config.xml` preferences  
- ✅ Type definitions available for TypeScript support  
- ✅ Maintained under the Apache Software Foundation  

## Installation

To install the Cordova Splashscreen Plugin, run the following command in your Cordova project directory:

```bash
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

> **Note**: This plugin is included in the default Cordova browser platform setup and may be automatically available when using `cordova platform add browser`.

## Usage

The plugin is accessed via the `navigator.splashscreen` object. Here's how to use it in your JavaScript code:

### Show the Splash Screen

```javascript
// Display the splash screen
navigator.splashscreen.show();
```

### Hide the Splash Screen

```javascript
// Dismiss the splash screen after app initialization
navigator.splashscreen.hide();
```

### Example: Using in a Browser App Startup

```javascript
document.addEventListener('DOMContentLoaded', function () {
    // Show splash screen on app load
    navigator.splashscreen.show();

    // Simulate app initialization (e.g., load assets, start services)
    setTimeout(function () {
        // Hide splash screen once the app is ready
        navigator.splashscreen.hide();
    }, 3000);
});
```

### Configuration (via `config.xml`)

You can control whether the splash screen is shown by default using the `config.xml` file:

```xml
<preference name="ShowSplashScreen" value="true" />
```

- `value="true"`: Shows the splash screen by default  
- `value="false"`: Hides the splash screen on startup  

> **Note**: The default behavior is to show the splash screen (`showSplashScreen = true`) unless overridden in the configuration.

## Dependencies

- Cordova 2.0.0 or later  
- Cordova Android 3.6.0+ (for Android platforms)  
- Cordova Windows 4.4.0+ (for Windows platforms)  
- Cordova iOS <6.0.0 (for iOS platforms, prior to version 6.0.0)  

> The plugin supports multiple Cordova versions through version-specific engine constraints defined in `package.json`.

## License

Apache License 2.0

For more information, see the [Apache License](http://www.apache.org/licenses/LICENSE-2.0).