# Apache Cordova Splashscreen Plugin

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Build Status](https://img.shields.io/github/workflow/status/apache/cordova-plugin-splashscreen/build?logo=github)
![Version](https://img.shields.io/github/v/tag/apache/cordova-plugin-splashscreen?label=version)

A Cordova plugin that enables the display and hiding of a splash screen during application launch in the browser platform. This plugin provides a simple API to show and hide the splash screen, ensuring a smooth user experience when launching a Cordova-based web app in a browser environment.

---

## Description

The **Cordova Splashscreen Plugin** is a lightweight, cross-platform solution designed to show and hide a splash screen during the initial launch of a Cordova app in the browser. It integrates seamlessly with the Cordova framework and exposes a clean JavaScript API via `navigator.splashscreen`, allowing developers to control when the splash screen appears and disappears.

This plugin is specifically tailored for the **browser platform**, making it ideal for developers building progressive web apps (PWAs) or hybrid apps that run in a browser context (e.g., via Cordova's `cordova-browser` or in testing environments). It does not require native code and operates entirely through JavaScript and the Cordova runtime.

---

## Features

- ✅ Show a splash screen at app launch using `navigator.splashscreen.show()`
- ✅ Hide the splash screen with `navigator.splashscreen.hide()`
- ✅ Configurable splash screen duration via `ShowSplashScreen` preference
- ✅ Automatically hides the splash screen after a default delay (3 seconds)
- ✅ Fully compatible with Cordova 2.0+ and modern versions (v8+)
- ✅ Type-safe interface via TypeScript definitions
- ✅ Open-source under the Apache License 2.0

---

## Table of Contents

- [Project Title](#project-title)
- [Description](#description)
- [Features](#features)
- [Table of Contents](#table-of-contents)
- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

- **Node.js** v14 or higher (required for Cordova CLI and plugin management)
- **Cordova CLI** v2.0.0 or later (with support for browser platform)
- **Cordova Browser Platform** (via `cordova platform add browser`)
- **Cordova Dependencies**:
  - For Cordova Android: `>=3.6.0` (with version constraints based on Cordova version)
  - For Cordova iOS: `<6.0.0` (prior to v6.0.0)
  - For Cordova Windows: `>=4.4.0` (from v4.4.0 onward)

> ⚠️ This plugin is **only intended for use in the browser platform**. It does not support native mobile platforms (iOS/Android) directly.

---

## Installation

To install the Apache Cordova Splashscreen Plugin in your Cordova project:

```bash
# Navigate to your Cordova project root
cd your-cordova-project

# Install the plugin via Cordova CLI
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

Or, if you're using a local copy:

```bash
# Clone the repository locally
git clone https://github.com/apache/cordova-plugin-splashscreen.git

# Install the plugin
cordova plugin add ./cordova-plugin-splashscreen
```

> ✅ The plugin will automatically register the `navigator.splashscreen` object in the browser environment.

---

## Usage

After installation, you can control the splash screen using the `navigator.splashscreen` API.

### Show Splash Screen

```javascript
// Display the splash screen when the app starts
navigator.splashscreen.show();
```

### Hide Splash Screen

```javascript
// Hide the splash screen after a delay or when the app is ready
navigator.splashscreen.hide();
```

### Example: Auto-hide after 3 seconds

```javascript
// Show splash screen initially
navigator.splashscreen.show();

// Hide after 3 seconds (default delay)
setTimeout(() => {
    navigator.splashscreen.hide();
}, 3000);
```

> 💡 The splash screen is automatically hidden after a default delay of **3000 milliseconds** (3 seconds) if no explicit hide call is made. This behavior can be overridden via configuration.

---

## Configuration (Optional)

You can customize splash screen behavior by setting preferences in your `config.xml` file:

```xml
<platform name="browser">
    <preference name="ShowSplashScreen" value="true" />
    <preference name="SplashScreenDelay" value="5000" />
</platform>
```

- `ShowSplashScreen`: Enables or disables the splash screen (default: `true`)
- `SplashScreenDelay`: Sets the delay (in milliseconds) before auto-hiding the splash screen (default: `3000`)

> These preferences are read at runtime and affect the behavior of the `show()` and `hide()` methods.

---

## Contributing

We welcome contributions from the community! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository** on GitHub
2. **Create a feature branch** for your changes
3. **Ensure code quality** by running linting:
   ```bash
   npm run lint
   ```
4. **Submit a pull request** with a clear description of your changes

Please note:
- All contributions must adhere to the [Apache License 2.0](LICENSE)
- Code must follow the existing style and structure
- All changes must be accompanied by appropriate documentation

For bug reports or feature requests, please open an issue at:  
👉 [https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

> This license allows for free use, modification, and distribution of the software, with attribution required.

---

## Contact / Authors

This plugin is maintained by the **Apache Software Foundation (ASF)** as part of the Apache Cordova ecosystem.

- 📧 **Project Notifications**:  
  - Commits: `commits@cordova.apache.org`  
  - Issues: `issues@cordova.apache.org`  
  - Pull Requests: `issues@cordova.apache.org`

- 🌐 **Project Repository**:  
  [https://github.com/apache/cordova-plugin-splashscreen](https://github.com/apache/cordova-plugin-splashscreen)

- 📚 **Documentation & Support**:  
  For more information, visit the official Cordova documentation at [https://cordova.apache.org](https://cordova.apache.org)

> The plugin is developed and maintained by the open-source community under the Apache Software Foundation.