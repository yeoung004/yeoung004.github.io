# React Native error: Element type is invalid: expected a string or a class/function but got: object

> I received an error message from React Native and I tried to fix it. The message said, "There is an issue on the main page, so please find out what it is." However, I found the issue from the Expo setting code.

If you want to import SVG in React Native, you need to add this code to Expo code metro.config.js:

```
const { getDefaultConfig } = require("expo/metro-config");

module.exports = (() => {
  const config = getDefaultConfig(__dirname);

  const { transformer, resolver } = config;

  config.transformer = {
    ...transformer,
    babelTransformerPath: require.resolve("react-native-svg-transformer"),
  };
  config.resolver = {
    ...resolver,
    assetExts: resolver.assetExts.filter((ext) => ext !== "svg"),
    sourceExts: [...resolver.sourceExts, "svg"],
  };

  return config;
})();
```
