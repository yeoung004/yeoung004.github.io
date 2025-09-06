# How I Set Up Automated Testing for a React Native App with Maestro 2

In my previous post, I explained why I chose Maestro for automated testing. This time, I’ll walk you through how I set up the tests.

## Setting Up Tests on macOS Runners

Unless you’re using Maestro Cloud, you’ll need a machine to run your test scripts for iOS and Android apps. Fortunately, my company already had two GitHub Action runners that we typically use for tasks like building the app and running checks. I asked my manager if I could also use them for automated testing, and he agreed—though there was one caveat: the laptops didn’t have great performance.

At first, I planned to run multiple tests in parallel. But I quickly realized that even running a single test at a time maxed out the laptops. In the end, I decided to run one test at a time.

If you’ve got a high-performance machine, though, I definitely recommend trying parallel testing.

## The Testing Workflow

To test an app with Maestro on both iOS and Android, you’ll need the following build files:

1. **.apk** – for the Android Emulator
2. **.app** – for the iOS Simulator

I updated our GitHub Action workflow to generate a universal **.apk** and **.app**, then upload them to an S3 bucket. Thankfully, the necessary secret keys were already stored in GitHub, so all I had to do was add a step to upload the files and send the S3 link to Slack. That’s it!

## Locale Setup

If you want to test different locales, Maestro makes this straightforward. If your app doesn’t use locales, you can skip this step.

### Android

1. Open **Android Studio**
2. Go to **Settings → Languages & Frameworks → Android SDK → SDK Tools**
3. Install **Android SDK Command-line Tools**
4. Choose the API version you want to test. I went with **Android API 33**, the latest version supported by Maestro.

Then, add these environment variables to your `.zshrc` file:

```bash
export ANDROID_HOME="$HOME/Library/Android/sdk"
path+=("$HOME/Library/Android/sdk/platform-tools")
path+=("$HOME/Library/Android/sdk/cmdline-tools/latest/bin")
export PATH
```

Once the emulator and APK were set up, I could run automated tests with Maestro. Some useful commands:

```bash
# List installed packages
adb shell pm list packages

# Uninstall your app if already installed
adb uninstall com.my.app

# Install the test build
adb install -r "./test/myapp.apk"
```

To run with a specific locale:

```bash
maestro start-device --device-locale ko_KR --os-version 33 --platform android
```

### iOS

Setting up iOS is simpler.

1. Open **Xcode**
2. Go to **Xcode → Settings → Components**
3. Click the **+** button
4. Install the iOS version you want to test

Then, install the `.app` on your simulator:

```bash
# Get the UUID of your running simulator
UDID=$(xcrun simctl list devices | grep '(Booted)' | head -n 1 | awk -F '[()]' '{print $2}')

# Uninstall your app
xcrun simctl uninstall "$UDID" com.your.app >/dev/null 2>&1 || true

# Install your app
xcrun simctl install "$UDID" ./app/myapp.app
```

To run with a specific locale:

```bash
maestro start-device --device-locale ko_KR --os-version 18 --platform ios
```

## Running Tests

Here’s an example `main.yaml` I wrote for pre-testing:

```yaml
appId: com.my.app
name: My app main flow
onFlowStart:
  # Preload your script
  - runScript: utils.js

# For the latest JS version, I use this engine
jsEngine: graaljs

---
# Main.yaml
# Reset app state before each automated test
- launchApp:
    clearState: true
    permissions:
      all: allow

- runFlow:
    when:
      visible: 'Hello world'
      platform: iOS
    commands:
      - tapOn: Open
```

Run the tests with:

```bash
maestro test main.yaml --debug-output ./debug
```

---

Since I work on macOS, the setup instructions above are macOS-specific.

If you want to see the supported specs, just run:

```bash
maestro start-device --help
```