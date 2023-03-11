![expovsreact](./expovsreact.png)
# React Native vs Expo

> 회사에 입사해서 가장 먼저 결정 해야했던건 순수 React Native를 쓸지 Expo 사용해서 크로스 플랫폼 앱을 만들지 였다. 반년이 넘는 시간동안 개발 및 유지보수를 통한 경험을 회고한다.

### 📌차이점
> Expo와 순수 React Native의 가장 큰 차이점은 JS만 쓰냐 Native와 같이 쓰나 인것 같다. 이는 스타트업이나 소규모로 빠르게 서비스를 제공하길 원하는 곳에서 사용하기엔 뭔가 React Native를 사용하기엔 맞지 않다고도 생각이 든다. 결국 Native를 건든다는건 두 언어 및 아키텍쳐를 다룰수 있는 개발자라는 건데 이런 개발자가 흔하다고 생각이 들지 않는다.

1. 개발환경
- Expo
  - VScode와 같은 에디터만 있으면 되고, Expo Go앱을 통해서 미리 빌드한 앱을 실행해 볼수 있다.
  - Expo에서 제공하지 않는 기능을 수정하거나 추가하려면 React Native랑 차이가 없다.
  (예시로 Android에서는 2000px정도 넘는 이미지를 보여주려하면 자동으로 다운그래이드 시켜서 보여준다. 이부분을 해결하기 위해선 Native코드를 건들어야 했었다. 결국 이미지를 잘라서 올리는 기능을 추가하고 자른 이미지를 보여주는 식으로 이슈를 해결했다.)
  - windows에서도 아이폰만 있으면 IOS개발이 가능
- React Native
  - Android Studio, Xcode와 같은 툴이 필수 이며, JAVA(or Kotlin), Swit(or Objective-C), JS총 3가지 언어 및 툴을 다룰줄 알아야한다.
  - 위 3가지를 잘 다룰줄 안다면 문제가 없다.
  - macOS가 아닐 경우 IOS 개발이 불가능하다.

2. 라이브러리 및 모듈
- Expo
  - Push Notification, Facebook Login, Google Maps 등과 같은 기본 모듈을 제공
  - 제공하지 않는 모듈은 개발자가 직접 개발해야 하지만 기술의 한계가 있을 경우 X
- React Native
  - Expo에서는 제공하지 않는 기술 제공하는 경우가 몇몇 있음(Kakao Login, FastImage => Expo sdk 48.0.0전에는 지원x, masonry list 등)
 
3. 성능
- 둘의 차이는 거의 나지 않는다 결국 Expo는 React Native 확장인데 큰차이가 날수가 없다. 하지만 React Native에서는 결국 Native를 건들기 때문에 코드를 빌드하거나 로딩시 약간에 찾이가 난다.

 ### 📌결론
 결국은 항상 모든 개발자가 말하지만 정답은 없다. 크래스 플랫폼이 아무리 좋다해도 결국 한계점은 항상 마주한다. 그렇다고 모든곳에 단점만 있는게 아니라 장점도 있다. 하물며 Flutter도 좋은 코드 경험으로 많은 개발자들이 좋아하지만 React Native의 CodePush라던지 Dart라는 신생 언어라던지의 한계가 존재한다. 반년이 넘는 시간동안 라이브 커머스를 운영하고 있지만 크게 불편한 점을 느끼지는 못했다. 결국 해결점은 찾게 되어있고 그 부분은 개발자의 역량에 달렸다고 생각한다.