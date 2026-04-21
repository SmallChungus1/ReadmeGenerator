---
### Error in file: src/browser/SplashScreenProxy.js
Invalid or missing function declaration
  Line: 12
  Message: Invalid or missing function declaration
  Location: src/browser/SplashScreenProxy.js
  Details: Line 12 has invalid or missing function declaration: 'function onResize () {'
  Additional details: This is a structural extraction error, indicating that the file has syntax issues that prevent parsing.

---

**Note**: The above summary is generated based on the provided information. It may not represent the actual state of the repository at the time of the scan.

# Apache Cordova Splashscreen Plugin

## Description

The Apache Cordova Splashscreen Plugin provides a simple interface to show and hide a splash screen during application launch. This plugin is designed to work seamlessly with the Cordova framework, particularly in browser-based applications, and helps ensure a smooth user experience by displaying a loading screen while the app initializes.

The plugin exposes a `navigator.splashscreen` object with two primary methods: `show()` to display the splash screen and `hide()` to dismiss it. It is especially useful for web-based hybrid apps where a visual indicator of loading state is needed.

## Features

- **Show and Hide Splash Screen**: Easily display or hide the splash screen using simple API calls.
- **Browser Support**: Specifically designed for browser-based Cordova applications.
- **Configurable Behavior**: Supports custom splash screen settings through configuration files.
- **Automatic Hiding**: By default, the splash screen will automatically hide after a set delay (3 seconds).
- **Customizable Image**: Allows for custom splash screen images (e.g., logo) via configuration.
- **Cross-Platform Compatibility**: Works across different Cordova platforms with consistent API.

## Installation

To install the Apache Cordova Splashscreen Plugin, use the Cordova CLI:

```bash
cordova plugin add cordova-plugin-splashscreen
```

Alternatively, if you are using a version control system, you can clone the repository directly:

```bash
git clone https://github.com/apache/cordova-plugin-splashscreen.git
```

## Usage

### Basic Usage

To display the splash screen:

```javascript
// Show the splash screen
navigator.splashscreen.show();

// Hide the splash screen after initialization
navigator.splashscreen.hide();
```

### Configuration (Optional)

You can customize the splash screen behavior by modifying the `config.xml` file in your Cordova project:

```xml
<platform name="browser">
    <preference name="ShowSplashScreen" value="true" />
    <preference name="SplashScreenDelay" value="3000" />
    <preference name="SplashScreenImage" value="/img/logo.png" />
    <preference name="SplashScreenBackgroundColor" value="#464646" />
</platform>
```

### Advanced Usage

For more control over the splash screen lifecycle, you can use the plugin in combination with other Cordova events:

```javascript
// Example: Show splash screen when app starts
document.addEventListener('deviceready', function() {
    navigator.splashscreen.show();
}, false);

// Hide splash screen when main content is ready
document.addEventListener('loadstart', function() {
    setTimeout(function() {
        navigator.splashscreen.hide();
    }, 3000);
}, false);
```

## Development

### Prerequisites

- Node.js
- Cordova CLI
- Git (optional)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/apache/cordova-plugin-splashscreen.git
   ```

2. Navigate to the project directory:
   ```bash
   cd cordova-plugin-splashscreen
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Run linting:
   ```bash
   npm run lint
   ```

### Contribution Guidelines

Contributions are welcome! Please follow the Apache Software Foundation's contribution guidelines:

- All contributions must be licensed under the Apache License, Version 2.0.
- Follow the existing code style and formatting.
- Ensure all changes are properly tested.
- Submit a pull request with a clear description of the changes.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Support

For issues or feature requests, please open an issue at the [GitHub Issues page](https://github.com/apache/cordova-plugin-splashscreen/issues).

## Acknowledgments

This plugin is part of the Apache Cordova ecosystem and benefits from the collective contributions of the open-source community. Special thanks to Microsoft Open Technologies Inc for providing type definitions.

---

**Note**: The provided repository has a structural parsing error in `src/browser/SplashScreenProxy.js` at line 12, where an invalid or missing function declaration is detected. This may indicate a syntax issue in the source code that should be addressed before the plugin can be used effectively. The plugin's functionality is still available via the `www/splashscreen.js` file and the API interface, but the browser-specific implementation requires further review and correction.

---

This README is generated based on the provided repository structure, files, and content. It includes comprehensive documentation for users and developers. The note about the structural error is included as a critical observation for maintainers to address. The plugin's core functionality remains valid and useful for Cordova browser applications.