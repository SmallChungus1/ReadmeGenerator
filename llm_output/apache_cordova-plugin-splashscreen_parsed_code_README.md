` is generated based on the provided repository code structure and contents.

---

# cordova-plugin-splashscreen

[![Chrome Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml)
[![Lint Test](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml)

The `cordova-plugin-splashscreen` is an Apache Cordova plugin that enables the display and control of a splash screen during your web application's launch process. It provides methods to show and hide the splash screen manually, and offers configuration options to customize its appearance and behavior.

**Note**: As of version 6.0.0, this repository primarily provides the splash screen implementation for the **Browser** platform. While previous versions of this plugin supported other platforms like Android, iOS, and Windows, their platform-specific code has been moved or deprecated from this repository. Users targeting those platforms should consult their respective Cordova platform guides or other relevant plugins for splash screen management.

## Description

This plugin displays a customizable splash screen that appears when your Cordova application is launching on the browser platform. It allows you to:
*   Show and hide the splash screen programmatically.
*   Configure the splash screen image, background color, size, and display delay via `config.xml`.
*   Control whether the splash screen automatically hides after a set duration.

## Features

*   **Programmatic Control**: Use JavaScript to explicitly show or hide the splash screen.
*   **Customizable Image**: Set a custom image for your splash screen.
*   **Background Color**: Define the background color behind the splash screen image.
*   **Size and Position**: Adjust the width and height of the splash screen image, which is centered on the screen.
*   **Automatic Hiding**: Configure the splash screen to automatically disappear after a specified delay.
*   **Initial Visibility**: Control whether the splash screen shows by default on application startup.

## Supported Platforms

*   **Browser**

    **Important Note**: This specific repository, `apache/cordova-plugin-splashscreen`, is currently maintained primarily for the **Browser** platform. Prior to version 6.0.0, this plugin provided support for Android, iOS, and Windows. If you require splash screen functionality for these platforms, please refer to their respective platform documentation within Cordova or consider alternative plugins.

## Installation

To add this plugin to your Cordova project, use one of the following commands:

```bash
# Install from npm (recommended)
cordova plugin add cordova-plugin-splashscreen

# You may also install directly from this repository
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

## Usage

### JavaScript API

The plugin clobbers `navigator.splashscreen`, making the following methods available after the `deviceready` event fires:

*   **`navigator.splashscreen.hide()`**
    Dismisses the splash screen.

    ```javascript
    navigator.splashscreen.hide();
    ```

*   **`navigator.splashscreen.show()`**
    Displays the splash screen.

    ```javascript
    navigator.splashscreen.show();
    ```

    **Note**: It is generally not necessary to call `navigator.splashscreen.show()` manually for initial application startup, as the splash screen can be configured to show automatically via `config.xml` preferences. Your application cannot call `navigator.splashscreen.show()` until the `deviceready` event has fired.

### Configuration in `config.xml`

You can customize the splash screen's behavior and appearance by adding preferences to your project's top-level `config.xml` file.

```xml
<platform name="browser">
    <!-- Required: Defines the splash screen image source -->
    <preference name="SplashScreen" value="/images/browser/splashscreen.jpg" />

    <!-- Optional: Controls automatic hiding (default: true) -->
    <preference name="AutoHideSplashScreen" value="true" />

    <!-- Optional: Delay in milliseconds before automatic hiding (default: 3000ms) -->
    <preference name="SplashScreenDelay" value="3000" />

    <!-- Optional: Background color behind the splash screen image (default: #464646) -->
    <preference name="SplashScreenBackgroundColor" value="green" />

    <!-- Optional: Controls if the splash screen shows by default on startup (default: true) -->
    <preference name="ShowSplashScreen" value="false" />

    <!-- Optional: Width of the splash screen image (default: 170) -->
    <preference name="SplashScreenWidth" value="600" />

    <!-- Optional: Height of the splash screen image (default: 200) -->
    <preference name="SplashScreenHeight" value="300" />
</platform>
```

#### Preference Details:

*   **`SplashScreen`** (string): The path to your splash screen image file.
    *   **Value**: An absolute path (e.g., `/images/browser/splashscreen.jpg`) relative to your `www` directory.
    *   **Default**: `/img/logo.png`
    *   **Example**: `<preference name="SplashScreen" value="/img/mylogo.png" />`
    *   **Note**: Ensure the image path is absolute within the web root (`www` directory) to function correctly in sub-pages.

*   **`AutoHideSplashScreen`** (boolean, defaults to `true`):
    *   Indicates whether to hide the splash screen automatically. If `true`, the splash screen is hidden after the duration specified by `SplashScreenDelay`.
    *   **Example**: `<preference name="AutoHideSplashScreen" value="false" />`

*   **`SplashScreenDelay`** (number, defaults to `3000`):
    *   Amount of time in milliseconds to wait before automatically hiding the splash screen.
    *   **Example**: `<preference name="SplashScreenDelay" value="5000" />`
    *   To disable the splash screen entirely (if `ShowSplashScreen` is true, it will show and immediately hide), set this to `0`: `<preference name="SplashScreenDelay" value="0" />`
    *   **Historical Note**: In older versions, values less than 30 were sometimes treated as seconds. This behavior is now deprecated; always use milliseconds.

*   **`SplashScreenBackgroundColor`** (string, defaults to `#464646`):
    *   The CSS-compatible background color for the splash screen view.
    *   **Example**: `<preference name="SplashScreenBackgroundColor" value="blue" />`

*   **`ShowSplashScreen`** (boolean, defaults to `true`):
    *   Determines if the splash screen should be shown automatically when the application starts.
    *   **Example**: `<preference name="ShowSplashScreen" value="false" />`

*   **`SplashScreenWidth`** (number, defaults to `170`):
    *   The desired width of the splash screen image in pixels. The image will scale down if the window is smaller.
    *   **Example**: `<preference name="SplashScreenWidth" value="400" />`

*   **`SplashScreenHeight`** (number, defaults to `200`):
    *   The desired height of the splash screen image in pixels. The image will scale proportionally to maintain its aspect ratio based on `SplashScreenWidth`.
    *   **Example**: `<preference name="SplashScreenHeight" value="300" />`

#### Browser Platform Specifics regarding Fading

For the Browser platform, the `hide()` method currently applies a fixed 1-second fade-out effect. Preferences like `FadeSplashScreen` and `FadeSplashScreenDuration` (which were relevant for other platforms in previous versions of this plugin) are **not** configurable for the Browser platform in this version of the plugin.

### Splash Screen Image Configuration

For the browser platform, splash screen images are standard web assets. Place your `SplashScreen` image within your `www` directory or a subdirectory thereof (e.g., `www/img/` or `www/images/browser/`).

Example directory structure:

```
projectRoot
    www/
        index.html
        img/
            logo.png
        images/browser/
            splashscreen.jpg  <-- Your splash screen image
    config.xml
    ...
```

Then, in your `config.xml`, you would reference it like this:

```xml
<platform name="browser">
    <preference name="SplashScreen" value="/images/browser/splashscreen.jpg" />
</platform>
```

## Contributing

We welcome contributions to Apache Cordova! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on how to report bugs, suggest features, and contribute code.

*   Check for GitHub issues that correspond to your contribution and link or create them if necessary.
*   Run the tests so your patch doesn't break existing functionality.

We look forward to your contributions!

## License

This plugin is licensed under the Apache 2.0 License. A full copy of the license can be found in the [LICENSE](LICENSE) file. Additional attribution information is provided in the [NOTICE](NOTICE) file.

## Release Notes

For a detailed history of changes and updates, please refer to the [RELEASENOTES.md](RELEASENOTES.md) file.