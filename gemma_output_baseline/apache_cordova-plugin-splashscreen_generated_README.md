# Cordova Plugin Splashscreen

[![Build Status](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml)
[![Build Status](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml)

## Description

This plugin displays and hides a splash screen while your application is loading. It provides a way to show a branded image or simply a background color during startup, enhancing the user experience.  This version is a development build, indicated by the version number `7.0.0-dev`.

## Features

*   **Display a splash screen:** Shows an image or background color while the application loads.
*   **Hide the splash screen:** Removes the splash screen after a specified delay or on-demand.
*   **Configuration Options:**
    *   `ShowSplashScreen`: Boolean, defaults to `true`. Controls whether the splash screen is displayed.
    *   `SplashScreenDelay`: Integer, defaults to 3000 (milliseconds).  Specifies how long the splash screen is displayed.
    *   `SplashScreen`: String, defaults to `/img/logo.png`. The path to the splash screen image.
    *   `SplashScreenBackgroundColor`: String, defaults to `#464646`. The background color of the splash screen.
    *   `SplashScreenWidth`: Integer, defaults to 170. Specifies the desired width of the splash image.
    *   `SplashScreenHeight`: Integer, defaults to 200. Specifies the desired height of the splash image.
    *   `AutoHideSplashScreen`: Boolean, defaults to `true`.  Specifies to display and automatically hide the splash screen.

## Installation

To install the plugin, use the Cordova CLI:

```bash
cordova plugin add cordova-plugin-splashscreen
```

## Usage

### JavaScript

You can control the splash screen using the `navigator.splashscreen` object.

*   **Show the splash screen:**

    ```javascript
    navigator.splashscreen.show();
    ```

*   **Hide the splash screen:**

    ```javascript
    navigator.splashscreen.hide();
    ```

### Configuration (config.xml)

You can configure the splash screen's appearance and behavior within your `config.xml` file.  Here's an example:

```xml
<preference name="ShowSplashScreen" value="true" />
<preference name="SplashScreenDelay" value="6000" />
<preference name="SplashScreen" value="splash.png" />
<preference name="SplashScreenBackgroundColor" value="#FFFFFF" />
<preference name="SplashScreenWidth" value="640" />
<preference name="SplashScreenHeight" value="480" />
<preference name="AutoHideSplashScreen" value="true" />
```

## Repository Details

*   **Repository URL:** [https://github.com/apache/cordova-plugin-splashscreen](https://github.com/apache/cordova-plugin-splashscreen)
*   **Commit Hash:** 586b988371fc57919288caacf7e1486ac44d19ca
*   **Timestamp:** 2026-03-04T19:52:35.352043

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this plugin.

## License

This plugin is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgements

This project is maintained by the Apache Software Foundation and the Cordova community.  Special thanks to the contributors who have helped improve this plugin.