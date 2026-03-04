` is generated based on the provided repository structure and file contents, focusing on clarity, accuracy, and comprehensiveness for the current state of the plugin (primarily targeting the Browser platform).

```markdown
---
title: Cordova Splashscreen Plugin for Browser
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

This plugin displays and hides a splash screen while your web application is launching on the **Browser** platform. Using its methods, you can also show and hide the splash screen manually.

## Supported Platforms

*   **Browser**

This version of the plugin focuses exclusively on providing splash screen functionality for the Cordova Browser platform. Older versions of this plugin supported other platforms (e.g., iOS, Android, Windows), but their platform-specific code has been moved or removed in version 6.0.0 and later.

## Installation

To add this plugin to your Cordova project, use the following command:

```bash
# npm hosted (new) id
cordova plugin add cordova-plugin-splashscreen

# You may also install directly from this repository
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

## Usage

Once installed, the plugin provides `navigator.splashscreen.show()` and `navigator.splashscreen.hide()` methods in your JavaScript code:

```javascript
// Show the splash screen
navigator.splashscreen.show();

// Hide the splash screen
navigator.splashscreen.hide();
```

## Browser Platform Configuration (`config.xml`)

You can customize the splash screen's behavior and appearance for the Browser platform by adding preferences within the `<platform name="browser">` tag in your project's top-level `config.xml` file.

The `config.xml` file is located in the root directory of your Cordova project (not in `platforms/browser/`).

Here are the available preferences and an example configuration:

```xml
<platform name="browser">
    <preference name="SplashScreen" value="/images/browser/splashscreen.jpg" />
    <preference name="AutoHideSplashScreen" value="true" />
    <preference name="SplashScreenDelay" value="3000" />
    <preference name="SplashScreenBackgroundColor" value="green" />
    <preference name="ShowSplashScreen" value="true" />
    <preference name="SplashScreenWidth" value="600" />
    <preference name="SplashScreenHeight" value="300" />
</platform>
```

### Preference Details

*   `SplashScreen` (string, default to `"/img/logo.png"`): Specifies the path to the splash screen image. The path should be **relative to your `www` directory** (the web root of your application).
    *   Example: `value="/images/browser/splashscreen.jpg"` will look for `projectRoot/www/images/browser/splashscreen.jpg`.
*   `AutoHideSplashScreen` (boolean, default to `true`): Determines whether the splash screen should be automatically hidden after `SplashScreenDelay` milliseconds.
    *   `value="true"`: Automatically hides the splash screen.
    *   `value="false"`: You must manually call `navigator.splashscreen.hide()`.
*   `SplashScreenDelay` (number, default to `3000`): The amount of time in **milliseconds** to wait before automatically hiding the splash screen (if `AutoHideSplashScreen` is `true`).
    *   To disable the splash screen entirely, set `SplashScreenDelay` to `0`.
*   `SplashScreenBackgroundColor` (string, default to `"#464646"`): Sets the CSS background color for the splash screen container. Can be a color name (e.g., "green"), hex code (e.g., "#FF0000"), or other valid CSS color values.
*   `ShowSplashScreen` (boolean, default to `true`): If set to `false`, the splash screen will not be shown at all during startup, even if other preferences are configured. This can be used as a quick toggle.
*   `SplashScreenWidth` (number, default to `170`): The default width in pixels for the splash screen image. The image will be scaled proportionally to fit within `window.innerWidth` while maintaining its aspect ratio.
*   `SplashScreenHeight` (number, default to `200`): The default height in pixels for the splash screen image. Used in conjunction with `SplashScreenWidth` to calculate the aspect ratio for scaling.

**Important Note on Fading:**
The browser platform implementation uses a hardcoded 1-second fade-out effect when hiding the splash screen. The preferences `FadeSplashScreen` and `FadeSplashScreenDuration`, which might be found in documentation for other platforms, are **not supported** by the browser platform implementation in this plugin.

## Methods

The `splashscreen` object is globally available under `navigator.splashscreen` after the `deviceready` event fires.

### `splashscreen.hide()`

Dismiss the splash screen.

```javascript
navigator.splashscreen.hide();
```

### `splashscreen.show()`

Displays the splash screen.

```javascript
navigator.splashscreen.show();
```

Your application cannot call `navigator.splashscreen.show()` until the application has started and the `deviceready` event has fired. However, typically the splash screen is meant to be visible *before* your application has fully started. If you have configured any `SplashScreen` related preferences in `config.xml` (e.g., `SplashScreen`, `ShowSplashScreen`), the splash screen will automatically be displayed immediately after your application is launched and before the `deviceready` event. For this reason, it is unlikely you will need to call `navigator.splashscreen.show()` to make the splash screen visible for application startup. You would typically use `show()` manually if you need to display a splash screen during other operations within your running app.

## TypeScript Support

This plugin includes TypeScript definitions in `types/index.d.ts`, providing type-checking and autocompletion for `navigator.splashscreen.hide()` and `navigator.splashscreen.show()` in TypeScript projects.

```typescript
interface Navigator {
    splashscreen: {
        hide(): void;
        show(): void;
    }
}
```

## Contributing

Apache Cordova is an open-source project, and contributions are welcome!

For detailed guidelines on how to contribute, including reporting bugs, suggesting features, improving documentation, or contributing code, please refer to the main [Apache Cordova Contribution Overview](http://cordova.apache.org/contribute/) and the specific [CONTRIBUTING.md](CONTRIBUTING.md) file in this repository.

Before submitting a Pull Request, please ensure you:
*   Check for existing GitHub issues or create new ones if necessary.
*   Run the tests to ensure your changes don't break existing functionality.

We look forward to your contributions!

## License

This project is licensed under the **Apache License, Version 2.0**.
A full copy of the license is available in the [LICENSE](LICENSE) file.

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/
```

## Release Notes

For a detailed history of changes, bug fixes, and new features across different versions, please refer to the [RELEASENOTES.md](RELEASENOTES.md) file.

## Maintainers

This plugin is maintained by The Apache Software Foundation.

## Additional Resources

*   **Source Code**: [https://github.com/apache/cordova-plugin-splashscreen](https://github.com/apache/cordova-plugin-splashscreen)
*   **Issue Tracker**: [https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)
*   **Apache Cordova Website**: [https://cordova.apache.org/](https://cordova.apache.org/)