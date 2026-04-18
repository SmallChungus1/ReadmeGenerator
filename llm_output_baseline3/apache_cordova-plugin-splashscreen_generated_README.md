# Cordova Splashscreen Plugin

![Apache License 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Build Status](https://github.com/apache/cordova-plugin-splashscreen/workflows/CI/badge.svg?branch=main)
![Version](https://img.shields.io/npm/v/cordova-plugin-splashscreen.svg?style=flat)

A Cordova plugin that provides a splash screen interface for web applications, enabling developers to display a visual indicator during app launch and hide it when the main content is ready.

---

## Description

The **Cordova Splashscreen Plugin** is a lightweight, cross-platform plugin designed to display and hide a splash screen during the initial launch phase of a Cordova-based mobile or web application. It works seamlessly in the browser platform, providing a consistent user experience by showing a branded image (typically a logo) while the app loads, and automatically hiding it once the main content is ready.

This plugin is part of the Apache Cordova ecosystem and is maintained by the Apache Software Foundation. It is ideal for developers building hybrid apps using Cordova, especially those targeting the browser platform or needing a splash screen for user experience consistency.

---

## Features

- ✅ Displays a splash screen during app launch using a configurable image.
- ✅ Hides the splash screen programmatically or automatically after a delay.
- ✅ Fully compatible with the browser platform via Cordova.
- ✅ Supports configuration through `config.xml` preferences.
- ✅ Provides a clean, standardized API via `navigator.splashscreen`.
- ✅ Built with TypeScript support for type safety and better developer experience.

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

Before using this plugin, ensure the following are installed and available:

- **Cordova CLI** (version 10.0.0 or higher)
- **Node.js** (v14.0.0 or higher)
- A Cordova project configured for the **browser platform** (e.g., `cordova create my-app com.example.myapp MyApp`)
- Access to a local or remote `config.xml` file for preference configuration

> ⚠️ This plugin is specifically designed for the **browser platform** and is not intended for native Android, iOS, or Windows platforms.

---

## Installation

To install the Cordova Splashscreen Plugin in your project:

```bash
# Navigate to your Cordova project root
cd my-cordova-app

# Install the plugin via Cordova CLI
cordova plugin add cordova-plugin-splashscreen
```

> ✅ The plugin will automatically register the `navigator.splashscreen` API and integrate with your project's `www` and `src` directories.

### Optional: Install from Source

If you need to build or modify the plugin:

```bash
git clone https://github.com/apache/cordova-plugin-splashscreen.git
cd cordova-plugin-splashscreen
npm install
```

---

## Usage

After installation, you can use the splashscreen API directly in your JavaScript code.

### Display the Splash Screen

```javascript
// Show splash screen (default behavior)
navigator.splashscreen.show();

// Show splash screen with a custom image (if supported)
navigator.splashscreen.show({ image: '/img/logo.png' });
```

### Hide the Splash Screen

```javascript
// Hide the splash screen
navigator.splashscreen.hide();
```

### Auto-Hide (Optional Configuration)

The plugin supports auto-hiding after a delay (default: 3000ms). This behavior can be configured in your `config.xml`:

```xml
<platform name="browser">
    <preference name="ShowSplashScreen" value="true" />
    <preference name="SplashScreenDelay" value="3000" />
</platform>
```

> 💡 The `ShowSplashScreen` preference controls whether the splash screen is displayed at all.  
> The `SplashScreenDelay` preference sets the time (in milliseconds) before the splash screen automatically hides.

---

## Contributing

We welcome contributions to improve the plugin's functionality, documentation, and maintainability.

### How to Contribute

1. Fork the repository on GitHub.
2. Create a new feature branch (`feature/your-feature-name`).
3. Commit your changes with clear, descriptive messages.
4. Push to the branch and open a pull request.

### Reporting Issues

If you encounter bugs or have feature requests, please open an issue at:  
👉 [https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)

> All contributions are governed under the [Apache License 2.0](LICENSE).

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Maintained by**: Apache Software Foundation (ASF)
- **Project Home**: [https://github.com/apache/cordova-plugin-splashscreen](https://github.com/apache/cordova-plugin-splashscreen)
- **Issue Tracker**: [https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)
- **Email**: `issues@cordova.apache.org` (for bug reports and pull request feedback)

For questions or support, please open an issue or reach out via the project's issue tracker.