# How I Set Up Automated Testing for a React Native App with Maestro

> Everyone in my company knew that automated testing could save us a lot of time and headaches. The problem was that setting it up and writing scripts for every scenario always felt time-consuming and overwhelming. But this time, we finally decided to do it — because testing the same parts over and over again before every build and release was just wasting too much time.

---

## What is Maestro?

> *“Maestro is the simplest and most effective UI testing framework.” – Maestro*

Maestro is a UI testing tool. Its **Maestro Cloud** service makes writing test scripts easy, even for non-developers like QA or PMs. There are many testing tools out there, but here’s why we chose Maestro over others.

---

## Why We Chose Maestro

Most mobile UI testing tools require a **test ID** for every element you want to check (like buttons, text inputs, or labels).
But Maestro works differently — it loads the **UI tree directly from native platforms** (iOS and Android).
That means we don’t have to attach test IDs to every element (only a few special cases). Instead, we can simply target elements by their text, without worrying about IDs. Huge time saver!

---

## How I Got Started

First, someone had to set things up for the project. Since automating boring problems is my favorite thing as a developer, I volunteered.

Together with QA, we discussed how to structure the automated process. I needed to configure it so that we could run tests in two ways:

* **Manually**
* **Automatically**

Maestro provides two main options for running automated UI tests:

1. **On Maestro Cloud** – convenient, but paid
2. **Locally** – free

The ideal choice was Cloud because it lets you run tests without needing your own machine. But my manager wasn’t keen on spending money for testing, so I had to make the local setup work most of the time.

Luckily, our company already had two MacBook Pros dedicated as runners. Thanks to them, we didn’t need to rely on the Cloud service.

⚠️ If you don’t have a machine that can run 24/7, you’ll either need to use Maestro Cloud or run tests manually on your computer each time.

---

## Android Works, but iOS...

Maestro builds its UI tree from each OS platform (iOS and Android) when selecting elements.
Here’s the catch: **iOS groups child elements together under one accessibility group**, meaning you can’t directly select child elements inside a parent.

To solve this, I set `accessible={false}` on every element for iOS using a custom Babel plugin.

```js
// babel.config.js
...
plugins: [
  ...(process.env.APPLY_BABEL_DISABLE_ACCESSIBLE === 'true'
    ? ['./tools/babel-plugin-disable-accessible']
    : []),
]
```

```js
// ./tools/babel-plugin-disable-accessible.js
module.exports = function (babel) {
  const { types: t } = babel;
  return {
    visitor: {
      JSXOpeningElement(path) {
        const componentName = path.node.name.name;
        const excludeList = [];

        if (excludeList.includes(componentName)) {
          return;
        }

        const attrs = path.node.attributes;
        const exists = attrs.some(
          (attr) =>
            t.isJSXAttribute(attr) &&
            t.isJSXIdentifier(attr.name, { name: 'accessible' })
        );

        if (!exists) {
          attrs.push(
            t.jsxAttribute(
              t.jsxIdentifier('accessible'),
              t.jsxExpressionContainer(t.booleanLiteral(false))
            )
          );
        }
      },
    },
  };
};
```