# Cordova Splashscreen Plugin

## Description

The **Cordova Splashscreen Plugin** is a lightweight, cross-platform plugin designed to display and hide a splash screen during application launch in Cordova-based web applications. This plugin is specifically optimized for the **browser platform**, providing a consistent user experience by showing a visual indicator while the app loads, and automatically hiding it once the main content is ready.

Built on the Apache Cordova framework, this plugin leverages native JavaScript APIs to expose a simple, developer-friendly interface through the `navigator.splashscreen` object. It is part of the Apache Cordova project and is licensed under the **Apache License 2.0**.

## Features

- ✅ **Display and hide splash screen** via simple JavaScript API calls (`show()` and `hide()`).
- 📱 **Platform-specific support** for the browser platform (via `navigator.splashscreen`).
- 🔧 **Configurable behavior** through `config.xml` preferences (e.g., enabling/disabling splash screen).
- 🚀 **Automatic hiding** after a configurable delay (default: 3 seconds).
- 📂 **Modular structure** with clear separation of browser-specific logic and JavaScript bindings.
- 📚 **Type definitions** provided for TypeScript support via `types/index.d.ts`.

## Installation

To install the plugin in a Cordova project, use the following command:

```bash
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

Alternatively, if you're using a local copy of the plugin:

```bash
cordova plugin add path/to/cordova-plugin-splashscreen
```

> **Note**: This plugin is primarily designed for use with the **Cordova browser platform**. It does not provide native splash screen support for Android, iOS, or Windows platforms.

## Usage

The plugin exposes a `navigator.splashscreen` object that can be used to control the splash screen lifecycle.

### Basic Usage

```javascript
// Show the splash screen
navigator.splashscreen.show();

// Hide the splash screen after the app has loaded
navigator.splashscreen.hide();
```

### Example: Auto-hide after a delay

```javascript
// Show splash screen with automatic hide after 3 seconds
navigator.splashscreen.show();

// Hide splash screen after 3 seconds (default behavior)
setTimeout(function() {
    navigator.splashscreen.hide();
}, 3000);
```

### Customization via config.xml

You can customize splash screen behavior by adding preferences to your `config.xml` file:

```xml
<platform name="browser">
    <preference name="ShowSplashScreen" value="true" />
    <preference name="SplashScreenDelay" value="2000" />
</platform>
```

> **Note**: The `ShowSplashScreen` preference controls whether the splash screen is displayed. The `SplashScreenDelay` preference sets the time (in milliseconds) before the splash screen is automatically hidden.

---

### Plugin Source Structure

- `src/browser/SplashScreenProxy.js` – Browser-specific logic for managing splash screen display and hide.
- `www/splashscreen.js` – JavaScript module exposing the `navigator.splashscreen` API.
- `types/index.d.ts` – TypeScript type definitions for the plugin interface.
- `plugin.xml` – Plugin metadata and platform-specific configuration.

> The plugin uses Cordova's `exec()` mechanism to communicate with the underlying platform, ensuring compatibility across different environments.