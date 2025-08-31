# What I Did for RTL (Right-to-Left)

> Last time, I shared my research on how to support RTL in mobile apps. This time, I’ll share what I actually implemented for RTL.
>
> Our company’s app was originally built for LTR (Left-to-Right) languages, so we had to check which layouts break when the OS language is set to RTL languages like Arabic or Hebrew. Fortunately, most layouts worked fine, but a few needed fixes.

---

## Setting RTL Support by Platform

### Android

Add the following to the `<application>` tag in `AndroidManifest.xml`:

```xml
android/app/src/main/AndroidManifest.xml

<application
  ...
  android:supportsRtl="true"
  ...
```

If you support multiple languages, you can add RTL-specific resources like `values-ar/strings.xml`. This isn’t required—it depends on your service.

---

### iOS

You need to add the language in Xcode:

1. Open Xcode.
2. Select your project in the Project Navigator (left sidebar).
3. Select the project in the main panel.
4. Go to the **Info** tab.
5. Click the **+** button at the bottom of the **Localizations** section.

---

### React Native

No special setup is needed for RTL in React Native. Just use `I18nManager.isRTL`.
If the user’s language is RTL, the native OS will handle it automatically.
However, changing the language **while the app is running** won’t update the layout unless manually handled. You can learn more in my [RTL article](https://yeoung004.github.io/rtl/).

To make layout logic simpler, define a constant:

```ts
import { I18nManager } from 'react-native';

export const isRTL = I18nManager.isRTL;
```

---

## Layout Fixes for RTL

### Calendar

Calendars are typically LTR, but in RTL they should be reversed.
So we had to update the logic for rendering the calendar grid:

| Sat | Fri | Thu | Wed | Tue | Mon | Sun |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  7  |  6  |  5  |  4  |  3  |  2  |  1  |

---

### Carousel

In RTL, carousels should move right to left.
We reversed the data and adjusted the default index accordingly:

```tsx
import Carousel from 'react-native-reanimated-carousel';

const data = useMemo(() => res.data.reverse(), [res.data]);

<>
  <Carousel
    renderItem={renderItem}
    autoPlayReverse
    data={data}
    defaultIndex={data.length - 1}
  />

  {data.map((v, index) => (
    <Dot
      key={v}
      activeIndex={activityIndex}
      index={isRTL ? data.length - 1 - index : index}
    />
  ))}
</>

const Dot = ({
  activeIndex,
  index,
}: {
  index: number;
  activeIndex: SharedValue<number>;
}) => {
  const {
    theme: {
      palette: { gray500, gray800 },
    },
  } = useStyles();

  const backgroundColor = useAnimatedStyle(() => {
    return {
      backgroundColor:
        activeIndex.value === index ? gray800 : gray500,
    };
  }, [index]);

  return (
    <Animated.View
      key={`dot.${index}`}
      style={[
        {
          width: 6,
          height: 6,
          borderRadius: 4,
        },
        backgroundColor,
      ]}
    />
  );
};
```

---

### Coordinate Systems

Absolute layouts flip automatically in RTL.
However, Skia and Canvas components do **not**, so you’ll need to manually flip the drawing or adjust coordinates accordingly.

---

### Masonry Layout (FlashList)

FlashList v1’s masonry layout doesn’t work in RTL.
In v2, it works with a simple prop:

```tsx
<FlashList 
  ...
  masonry // or masonry={true}
  ...
/>
```

---

### Icons

Arrow icons must point the opposite direction in RTL.

You have two options:

**Option 1: Use `transform` (less recommended)**

```tsx
const arrowIcons = ['left-arrow', 'right-arrow'];

<Icon
  style={% raw %}{{
    transform:
      isRTL && arrowIcons.includes(name)
        ? [{ rotate: '180deg' }]
        : undefined,
  }}{% endraw %}
/>
```

**Option 2: Use separate icons (recommended)**

```tsx
const LeftIcon = require('./leftArrow.svg');
const RightIcon = require('./rightArrow.svg');

const arrowIcons = {
  'left-arrow': RightIcon,
  'right-arrow': LeftIcon,
};

{arrowIcons[name]}
```

---

### Animations

Animation directions must also be flipped.
For example, change positive `translateX` to negative in RTL:

```ts
const translateX = animatedValue.interpolate({
  inputRange: [0, 1],
  outputRange: isRTL ? [-3, -21] : [3, 21],
});
```


## Conclusion
Supporting RTL might seem simple at first, but real-world implementation often reveals hidden layout issues—especially in custom components like carousels, calendars, animations, and canvas-based drawings.

By understanding how each platform and library handles RTL, and applying consistent checks with isRTL, you can create a seamless experience for RTL users without maintaining two separate layouts.

If your app aims to serve a global audience, adding solid RTL support is not just a nice-to-have—it’s a necessity. I hope this post helps you avoid common pitfalls and gives you a clear starting point for implementing RTL in your own projects.