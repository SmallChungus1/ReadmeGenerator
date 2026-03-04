` is generated based on the provided repository structure and file contents for `apache/cordova-plugin-splashscreen` at commit `586b988371fc57919288caacf7e1486ac44d19ca`.

---

---
title: Browser Splashscreen
description: Control the browser platform splash screen for your app.
---
<!--
# license: Licensed to the Apache Software Foundation (ASF) under one
#         or more contributor license agreements.  See the NOTICE file
#         distributed with this work for additional information
#         regarding copyright ownership.  The ASF licenses this file
#         to you under the Apache License, Version 2.0 (the
#         "License"); you may not use this file except in compliance
#         with the License.  You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
#         Unless required by applicable law or agreed to in writing,
#         software distributed under the License is distributed on an
#         "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#         KIND, either express or implied.  See the License for the
#         specific language governing permissions and limitations
#         under the License.
-->

# cordova-plugin-splashscreen

[![Chrome Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml) [![Lint Test](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml)

## Description

The `cordova-plugin-splashscreen` is an Apache Cordova plugin designed to display and manage a splash screen for your web application during its launch sequence. While historically this plugin supported multiple platforms, its current implementation and configuration are primarily focused on the **Browser** platform. It provides functionalities to automatically show and hide a customizable splash screen or to manually control its visibility through JavaScript methods.

This plugin ensures a smoother user experience by displaying a visual placeholder while your application's web assets are loading.

## Features

*   **Automatic Splash Screen Display**: Configurable to automatically show a splash screen upon application start.
*   **Manual Control**: Programmatically show and hide the splash screen at any point in your application using JavaScript.
*   **Customizable Duration**: Define how long the splash screen is displayed before it automatically hides.
*   **Fading Effects**: Enable or disable fade-in/fade-out transitions for the splash screen, with adjustable durations.
*   **Image Configuration**: Specify a custom splash screen image, its background color, and dimensions specifically for the Browser platform.
*   **TypeScript Support**: Includes TypeScript definition files for enhanced development experience.

## Supported Platforms

Based on the current plugin structure (`plugin.xml`, `src/browser/SplashScreenProxy.js`, `package.json` `platforms` array), this plugin officially supports:

*   **Browser**

**Note on Historical Support**: Previous versions of this plugin supported other platforms like Android, iOS, and Windows. However, the platform-specific code for iOS has been explicitly removed in version 6.0.0 as noted in `RELEASENOTES.md`. The `package.json` may still contain historical `cordovaDependencies` entries for these platforms, but they do not reflect the current functionality or code within this repository.

## Installation

To add this plugin to your Cordova project, use the Cordova CLI:

```bash
# Install from npm (recommended)
cordova plugin add cordova-plugin-splashscreen

# You may also install directly from this repository
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

### Compatibility

The plugin defines certain Cordova engine dependencies in its `package.json`. While this repository is currently focused on the Browser platform, these dependencies reflect broader compatibility historically:

```json
"engines": {
    "cordovaDependencies": {
      "2.0.0": { "cordova-android": ">=3.6.0" },
      ">=4.0.0": { "cordova-android": ">=3.6.0", "cordova-windows": ">=4.4.0" },
      "<6.0.0": { "cordova-ios": "<6.0.0" },
      "6.0.2": { "cordova-android": ">=3.6.0 <11.0.0", "cordova-windows": ">=4.4.0" },
      "<7.0.0": { "cordova-android": ">=3.6.0 <11.0.0", "cordova-windows": ">=4.4.0" },
      "8.0.0": { "cordova": ">100" }
    }
}
```

## Usage

### JavaScript Methods

The plugin exposes a `splashscreen` object on the `navigator` global, providing methods to control the splash screen.

#### `navigator.splashscreen.hide()`

Dismiss the splash screen.

```javascript
navigator.splashscreen.hide();
```

#### `navigator.splashscreen.show()`

Displays the splash screen.

```javascript
navigator.splashscreen.show();
```

**Important Note**: Your application cannot call `navigator.splashscreen.show()` until the application has started and the `deviceready` event has fired. However, if you configure splash screen preferences in `config.xml`, the splash screen will automatically be shown immediately after your application is launched, before the `deviceready` event. For this reason, you will unlikely need to call `navigator.splashscreen.show()` for initial application startup.

### Configuration Preferences (config.xml)

You can customize the splash screen's behavior by adding `<preference>` tags to your project's top-level `config.xml` file.

#### General Preferences

These preferences apply to the splash screen behavior.

*   `AutoHideSplashScreen` (boolean, defaults to `true`):
    Indicates whether to hide the splash screen automatically after `SplashScreenDelay`.
    ```xml
    <preference name="AutoHideSplashScreen" value="true" />
    ```

*   `SplashScreenDelay` (number, defaults to `3000`):
    Amount of time in milliseconds to wait before automatically hiding the splash screen.
    ```xml
    <preference name="SplashScreenDelay" value="3000" />
    ```
    **Note**: This value used to be in seconds (but is now milliseconds), so values less than 30 will continue to be treated as seconds for backward compatibility (this is a deprecated patch that may be removed in future versions). To disable the splash screen, set this preference to `0`.
    ```xml
    <preference name="SplashScreenDelay" value="0"/>
    ```

*   `FadeSplashScreen` (boolean, defaults to `true`):
    Set to `false` to prevent the splash screen from fading in and out when its display state changes.
    ```xml
    <preference name="FadeSplashScreen" value="false"/>
    ```

*   `FadeSplashScreenDuration` (float, defaults to `500`):
    Specifies the number of milliseconds for the splash screen fade effect to execute.
    ```xml
    <preference name="FadeSplashScreenDuration" value="750"/>
    ```
    **Note**: `FadeSplashScreenDuration` is included into `SplashScreenDelay`. For example, if you have `<preference name="SplashScreenDelay" value="3000" />` and `<preference name="FadeSplashScreenDuration" value="1000"/>` defined in `config.xml`:
    *   00:00 - splashscreen is shown
    *   00:02 - fading has started
    *   00:03 - splashscreen is hidden
    Turning the fading off via `<preference name="FadeSplashScreen" value="false"/>` technically means fading duration to be `0` so that in this example the overall splash screen delay will still be 3 seconds.
    This only applies to the application startup - you need to take the fading timeout into account when manually showing/hiding the splash screen in your application's code:
    ```javascript
    navigator.splashscreen.show();
    window.setTimeout(function () {
        navigator.splashscreen.hide();
    }, splashDuration - fadeDuration);
    ```

#### Browser-Specific Quirks

For the **Browser** platform, you can define additional splash screen properties within a `<platform name="browser">` tag in your `config.xml`:

```xml
<platform name="browser">
    <!-- Path to the splash screen image, relative to the project root. Defaults to "/img/logo.png". -->
    <preference name="SplashScreen" value="/images/browser/splashscreen.jpg" />
    <!-- Whether to automatically hide the splash screen. Defaults to "true". -->
    <preference name="AutoHideSplashScreen" value="true" />
    <!-- Delay in milliseconds before automatically hiding the splash screen. Defaults to "3000". -->
    <preference name="SplashScreenDelay" value="3000" />
    <!-- Background color for the splash screen. Defaults to "#464646". -->
    <preference name="SplashScreenBackgroundColor" value="green" />
    <!-- Whether to show the splash screen at all. Defaults to "true". -->
    <preference name="ShowSplashScreen" value="false" />
    <!-- Desired width of the splash screen image. Defaults to "170". -->
    <preference name="SplashScreenWidth" value="600" />
    <!-- Desired height of the splash screen image. Defaults to "200". -->
    <preference name="SplashScreenHeight" value="300" />
</platform>
```
**Note**: The `SplashScreen` value (image path) should be absolute in order to work correctly, especially if your application navigates to sub-pages.

### Splash Screen Image Configuration

For the **Browser** platform, the splash screen image is specified using the `SplashScreen` preference within the `<platform name="browser">` tag in `config.xml`. The path provided for the `src` attribute is relative to the project's root directory, not the `www` directory.

**Example Directory Structure:**

```
projectRoot/
├── hooks/
├── platforms/
├── plugins/
├── www/
│   ├── css/
│   ├── img/
│   └── js/
└── res/            <-- You might place images here
    └── screen/
        └── mysplash.png
```

If you place your image at `projectRoot/res/screen/mysplash.png`, your `config.xml` preference would look like:

```xml
<platform name="browser">
    <preference name="SplashScreen" value="/res/screen/mysplash.png" />
</platform>
```

Alternatively, you could place it directly under `projectRoot/img/browser/splashscreen.jpg` as suggested in the example above.

## Contributing

We welcome contributions! If you are interested in contributing to Apache Cordova, please start by reading the [contribution overview](http://cordova.apache.org/contribute/).

You can find detailed contribution guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file within this repository. Please make sure to check for existing GitHub issues or create new ones, and run the tests to ensure your changes don't introduce regressions.

## License

This project is licensed under the **Apache-2.0 License**. See the [LICENSE](LICENSE) file for full details.

```
Apache Cordova
Copyright 2012 The Apache Software Foundation

This product includes software developed at
The Apache Software Foundation (http://www.apache.org/).