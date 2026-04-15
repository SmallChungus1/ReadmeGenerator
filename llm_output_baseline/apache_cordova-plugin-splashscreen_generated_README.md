# Cordova Splashscreen Plugin

![Apache License 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Build Status](https://github.com/apache/cordova-plugin-splashscreen/workflows/CI/badge.svg?branch=main)
![Version](https://img.shields.io/npm/v/cordova-plugin-splashscreen.svg?style=flat)

A Cordova plugin that provides a splash screen interface for web applications, allowing developers to display a visual indicator during app launch and hide it when the main content is ready.

---

## Description

The **Cordova Splashscreen Plugin** enables web-based mobile applications to show a splash screen when launching, improving user experience by providing visual feedback during the initial loading phase. This plugin is designed to work seamlessly with the Cordova browser platform and integrates with the native `navigator.splashscreen` API.

This plugin is part of the Apache Cordova ecosystem and is maintained by the **Apache Software Foundation**. It is primarily used in Cordova-based hybrid apps to display a logo or image while the app loads, ensuring a professional and polished first impression.

---

## Features

- ✅ Displays a customizable splash screen during app launch  
- ✅ Hides the splash screen automatically after a configurable delay  
- ✅ Fully compatible with the Cordova browser platform  
- ✅ Supports dynamic show/hide via JavaScript API  
- ✅ Configurable splash screen duration and visibility  
- ✅ Maintained under the Apache License 2.0 for open-source collaboration  

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

Before using this plugin, ensure you have the following:

- **Cordova CLI** (version 10.0.0 or higher recommended)
- **Node.js** (v14+)
- A Cordova project configured for the browser platform
- Access to a web-based application with a `config.xml` file

> ⚠️ This plugin is specifically designed for **Cordova browser platform** use cases. It does not support native Android, iOS, or Windows platforms directly.

---

## Installation

To install the Cordova Splashscreen Plugin in your Cordova project:

```bash
# Navigate to your Cordova project root
cd your-cordova-project

# Install the plugin via Cordova CLI
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git#7.0.0-dev
```

Alternatively, install directly from npm:

```bash
npm install cordova-plugin-splashscreen@7.0.0-dev
```

Then, add the plugin to your project:

```bash
cordova plugin add cordova-plugin-splashscreen
```

> 💡 The plugin is automatically compatible with the browser platform as defined in the `plugin.xml`.

---

## Usage

After installation, you can control the splash screen using the `navigator.splashscreen` API in JavaScript.

### Show the Splash Screen

```javascript
// Display the splash screen when the app starts
window.navigator.splashscreen.show();
```

### Hide the Splash Screen

```javascript
// Hide the splash screen after the main content loads
window.navigator.splashscreen.hide();
```

### Configure Splash Screen Behavior (via config.xml)

You can customize the splash screen behavior in your `config.xml` file:

```xml
<platform name="browser">
    <preference name="ShowSplashScreen" value="true" />
    <preference name="SplashScreenDelay" value="3000" />
</platform>
```

> 🔍 The default splash screen delay is **3 seconds**. The splash screen will be shown by default (`ShowSplashScreen=true`).

> 📝 Note: The plugin uses `cordova/exec` to communicate with the underlying platform. The actual image is loaded from a local path (e.g., `/img/logo.png`) and displayed via the browser's DOM.

---

## Contributing

We welcome contributions to improve the Cordova Splashscreen Plugin. Please follow these guidelines:

- Fork the repository on GitHub
- Create a new feature branch for your changes
- Ensure all tests pass (if applicable)
- Update documentation as needed
- Submit a pull request with a clear description of your changes

For bug reports or feature requests, please open an issue at:  
👉 [https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)

A detailed contributing guide is available in the [CONTRIBUTING.md](CONTRIBUTING.md) file (to be created).

---

## License

This project is licensed under the **Apache License, Version 2.0**.  
See the [LICENSE](LICENSE) file for details.

> This license allows for free use, modification, and distribution of the software, provided that appropriate credit is given and any derivative works are licensed under the same terms.

---

## Contact / Authors

This plugin is maintained by the **Apache Software Foundation**.

- 📧 For issues and bug reports: [issues@cordova.apache.org](mailto:issues@cordova.apache.org)
- 📧 For general plugin updates: [commits@cordova.apache.org](mailto:commits@cordova.apache.org)
- 🌐 GitHub Repository: [https://github.com/apache/cordova-plugin-splashscreen](https://github.com/apache/cordova-plugin-splashscreen)
- 📚 Documentation: [https://cordova.apache.org](https://cordova.apache.org)

Join the Cordova community on [Discord](https://discord.gg/cordova) or follow updates on [Twitter](https://twitter.com/cordova) for announcements and best practices.