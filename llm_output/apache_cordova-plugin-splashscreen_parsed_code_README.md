` is generated based on the provided repository structure and contents.

---

# cordova-plugin-splashscreen

[![Chrome Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml)
[![Lint Test](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml)

## Description

The Cordova Splashscreen Plugin allows you to control and manage a splash screen for your Cordova applications. It displays a customizable splash screen while your web application is launching and provides methods to manually show or hide it. This can improve the perceived loading time and provide a branded experience to users.

## Features

*   **Automatic Splash Screen Display**: Configures a splash screen to automatically show when the application starts.
*   **Manual Control**: Provides JavaScript API (`navigator.splashscreen.show()` and `navigator.splashscreen.hide()`) to programmatically control the splash screen's visibility.
*   **Customizable Appearance**: Allows configuration of the splash screen image, background color, and dimensions.
*   **Configurable Delay**: Set a duration for how long the splash screen remains visible before automatically hiding.
*   **Fade Effects**: Options to enable/disable and configure the duration of fade-in/out effects for the splash screen.
*   **Browser Platform Support**: Dedicated implementation for displaying splash screens in browser-based Cordova applications.

## Supported Platforms

*   **Browser**

_Note: While previous versions of this plugin supported other platforms like iOS and Android, the platform-specific code for those implementations has been moved or removed from this repository. This plugin now primarily focuses on the Browser platform._

## Installation

To add this plugin to your Cordova project, use the following commands:

```bash
# npm hosted (new) id
cordova plugin add cordova-plugin-splashscreen

# You may also install directly from this repository
cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git
```

## Usage

The plugin's behavior is configured primarily through preferences in your project's top-level `config.xml` file.

### Configuration (`config.xml`)

In your project's `config.xml` file, you can define various preferences to customize the splash screen. The values for image sources are relative to the project root directory, not the `www` directory.

**Example `config.xml` Structure for Browser Platform:**

```xml
<?xml version='1.0' encoding='utf-8'?>
<widget id="com.example.app" version="1.0.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
    <name>MyApp</name>
    <description>
        A sample Apache Cordova application.
    </description>
    <author email="dev@cordova.apache.org" href="http://cordova.io">
        Apache Cordova Team
    </author>
    <content src="index.html" />
    <access origin="*" />

    <!-- General Splash Screen Preferences -->
    <preference name="AutoHideSplashScreen" value="true" />
    <preference name="SplashScreenDelay" value="3000" />
    <preference name="FadeSplashScreen" value="true"/>
    <preference name="FadeSplashScreenDuration" value="500"/>

    <!-- Browser Platform Specific Preferences (Quirks) -->
    <platform name="browser">
        <preference name="SplashScreen" value="/images/browser/splashscreen.jpg" /> <!-- defaults to "/img/logo.png" -->
        <!-- <preference name="AutoHideSplashScreen" value="true" /> --> <!-- defaults to "true", can override global -->
        <!-- <preference name="SplashScreenDelay" value="3000" /> --> <!-- defaults to "3000", can override global -->
        <preference name="SplashScreenBackgroundColor" value="#1a202c" /> <!-- defaults to "#464646" -->
        <preference name="ShowSplashScreen" value="true" /> <!-- defaults to "true" -->
        <preference name="SplashScreenWidth" value="600" /> <!-- defaults to "170" -->
        <preference name="SplashScreenHeight" value="300" /> <!-- defaults to "200" -->
    </platform>
</widget>
```

#### Preferences Details

*   **`AutoHideSplashScreen`** (boolean, defaults to `true`)
    *   Determines whether the splash screen should automatically hide after the `SplashScreenDelay`.
    *   Example: `<preference name="AutoHideSplashScreen" value="false" />`

*   **`SplashScreenDelay`** (number, defaults to `3000`)
    *   The amount of time in **milliseconds** to wait before automatically hiding the splash screen.
    *   **Important**: This value used to be in seconds. For backward compatibility, values less than `30` will continue to be treated as seconds. It is recommended to use millisecond values (e.g., `3000` for 3 seconds).
    *   To disable the splash screen entirely, set this preference to `0`: `<preference name="SplashScreenDelay" value="0"/>`
    *   Example: `<preference name="SplashScreenDelay" value="5000" />` (for 5 seconds)

*   **`FadeSplashScreen`** (boolean, defaults to `true`)
    *   Set to `false` to prevent the splash screen from fading in and out when its display state changes.
    *   Example: `<preference name="FadeSplashScreen" value="false"/>`

*   **`FadeSplashScreenDuration`** (float, defaults to `500`)
    *   Specifies the number of **milliseconds** for the splash screen fade effect to execute.
    *   **Note**: `FadeSplashScreenDuration` is included into `SplashScreenDelay`. For example, if you have `<preference name="SplashScreenDelay" value="3000" />` and `<preference name="FadeSplashScreenDuration" value="1000"/>` defined:
        *   00:00 - splash screen is shown
        *   00:02 - fading has started
        *   00:03 - splash screen is hidden
    *   Turning fading off via `<preference name="FadeSplashScreen" value="false"/>` technically means the fading duration is `0`, so the overall splash screen delay will still be `SplashScreenDelay`.
    *   Example: `<preference name="FadeSplashScreenDuration" value="750"/>`

#### Browser-Specific Preferences (Quirks)

These preferences are typically defined within a `<platform name="browser">` tag in `config.xml` to apply only to the browser platform.

*   **`SplashScreen`** (string, defaults to `/img/logo.png`)
    *   The path to the splash screen image. The path is relative to the project root directory.
    *   **Note**: The value should be an absolute path (e.g., `/images/browser/splashscreen.jpg`) for it to work correctly in sub-pages.
    *   Example: `<preference name="SplashScreen" value="/res/screen/my_splash.png" />`

*   **`SplashScreenBackgroundColor`** (string, defaults to `#464646`)
    *   The background color of the splash screen, in CSS color format (e.g., hexadecimal, RGB, color name).
    *   Example: `<preference name="SplashScreenBackgroundColor" value="green" />`

*   **`ShowSplashScreen`** (boolean, defaults to `true`)
    *   A browser-specific preference to explicitly enable or disable the splash screen display.
    *   Example: `<preference name="ShowSplashScreen" value="false" />`

*   **`SplashScreenWidth`** (number, defaults to `170`)
    *   The intrinsic width of the splash screen image in pixels. Used for initial sizing and aspect ratio calculations.
    *   Example: `<preference name="SplashScreenWidth" value="600" />`

*   **`SplashScreenHeight`** (number, defaults to `200`)
    *   The intrinsic height of the splash screen image in pixels. Used for initial sizing and aspect ratio calculations.
    *   Example: `<preference name="SplashScreenHeight" value="300" />`

### JavaScript API

The plugin exposes two global JavaScript methods under `navigator.splashscreen` to control the splash screen manually.

#### `splashscreen.hide()`

Dismiss the splash screen.

```javascript
navigator.splashscreen.hide();
```

#### `splashscreen.show()`

Displays the splash screen.

```javascript
navigator.splashscreen.show();
```

**Important Considerations for `splashscreen.show()`:**

Your application cannot call `navigator.splashscreen.show()` until the application has started and the `deviceready` event has fired.

However, typically the splash screen is intended to be visible *before* your application has fully started. If you provide any of the relevant splash screen parameters in `config.xml` (e.g., `SplashScreenDelay`), the splash screen will automatically be `show()`n immediately after your application is launched and before the `deviceready` event fires. For this reason, it is generally not necessary to call `navigator.splashscreen.show()` explicitly for application startup.

If you have `AutoHideSplashScreen` set to `false`, you would typically hide the splash screen manually once your application is ready:

```javascript
document.addEventListener("deviceready", function() {
    // Perform any app initialization here
    // ...

    // Hide the splash screen when your app is ready
    navigator.splashscreen.hide();
}, false);
```

When manually showing/hiding with `FadeSplashScreen` enabled, remember to account for the `FadeSplashScreenDuration` in your timeouts:

```javascript
var splashDuration = 3000; // total time to show splash
var fadeDuration = 500;    // fade effect duration

navigator.splashscreen.show();
window.setTimeout(function () {
    navigator.splashscreen.hide();
}, splashDuration - fadeDuration);
```

## Contributing

Anyone can contribute to Cordova. We need your contributions!

There are multiple ways to contribute: report bugs, improve the docs, and contribute code.

For instructions on this, start with the [contribution overview on the Apache Cordova website](http://cordova.apache.org/contribute/).

The details are explained there, but the important items are:
*   Check for Github issues that correspond to your contribution and link or create them if necessary.
*   Run the tests so your patch doesn't break existing functionality.

We look forward to your contributions!

You can also find issue and pull request templates in the `.github` directory for guidance.

## License

This plugin is licensed under the Apache 2.0 License.

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## Further Information

*   **Repository**: [https://github.com/apache/cordova-plugin-splashscreen](https://github.com/apache/cordova-plugin-splashscreen)
*   **Issue Tracker**: [https://github.com/apache/cordova-plugin-splashscreen/issues](https://github.com/apache/cordova-plugin-splashscreen/issues)
*   **Apache Cordova Website**: [http://cordova.apache.org/](http://cordova.apache.org/)