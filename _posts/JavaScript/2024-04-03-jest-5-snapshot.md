# jest 5 - snapshot

> snapshot은 React 컴포넌트 테스트에서 가장 중요한 개념이다. toMatchSnapShot함수를 이용해서 컴포넌트를 개발자가 원하는 스냅샷으로 만들어 예상대로 생성되는지 아닌지를 비교하는 방법이다.

#### 사용법
##### 테스트 하고자 하는 컴포넌트를 toMatchSnapshot로 snapshot을 만들면 __snapshots__이라는 폴더가 생기고 안에 파일이 들어간다
```js
import React from 'react';
import renderer from 'react-test-renderer';
import SomeComponent from './SomeComponent';

it('renders correctly', () => {
  // new Date().getTime()을 바로 사용하면 테스트를 실행 할때 마다 달라진다
  jest.spyOn(Date.prototype, 'getTime').mockReturnValue(1234567890);

  const some = {
    user: 'tester',
    name: 'tester',
    age: 14,
    createdDt: new Date().getTime()
  };

  const tree = renderer
    .create(<SomeComponent someProp={some}/>)
    .toJSON(); // 가독성을 위해 추가
  expect(tree).toMatchSnapshot();
});
```
#### 주의 사항
> 스냅샷이 찍은 시점에 잘못 됐을 경우 Jest cli에서 u 또는 jest --updateSnapshot 또는 특정 컴포넌트만 jest SomeComponent.test.js --updateSnapshot 명령어를 통해 업데이트가 가능하다. 스냅샷도 테스트의 일부 이기 때문에 함부러 업데이트를 할경우 에러인 상태의 스냅샷으로 저장하게 된다.
