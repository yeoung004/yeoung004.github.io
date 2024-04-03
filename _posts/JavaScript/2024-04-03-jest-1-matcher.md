# Jest 1 - Matcher

> 과제전형을 준비하면서 겸사겸사 test library에 대해 복습하고 정리하기로 한다<br />Jest에서는 간단하게 비교하며 값이 예상한 결과가 맞는지 확인할수 있도록 기능을 제공한다 이를 Matcher라고 부르며 다양한 타입의 Matcher를 제공한다.
테스트 함수는 it, test 둘중 한개를 사용한다. 두개의 함수의 기능은 동일하고 개발자가 원하는데에 초점을 둘경우 다르게 사용할수 있다 예를 들어 it should ... 처럼 특정 조건에 부합한지 테스트할때 it을 쓰거나 동작, 기능에 테스트를 할경우 test를 사용하는 것처럼 사용이 가능하다.

사용 방법은 아래와 같다
```js
test('설명', () => {
  // 테스트 코드
});

// 또는
it('설명', () => {
  // 테스트 코드
});
```

## Matcher
<hr />

#### toBe
##### 가장 기본적인 비교함수 js에서 == 연산자와 동일
```js
test('기본 비교함수 ==', () => {
  expect(1).toBe(1);
});
```

#### toEqual
##### 참조가 아닌 값을 비교, 주로 2개의 객체나 배열을 비교 전혀 다른 객체 및 인스턴스라도 값으로 비교하기 때문에 같다고 인식
```js
test('비교함수', () => {
  const data = { one: 1 };
  data['two'] = 2;
  expect(data).toEqual({ one: 1, two: 2 });

  // js는 객체를 비교할때 값이 아닌 참조로 비교하기 때문에 다르다고 나옴 => 콘솔에서는 false로 나온다
  console.log(data === { one: 1, two: 2 });

  // 아래도 false로 나온다
  test('기본 비교함수 ===', () => {
  expect({ one: 1, two: 2 }).toBe({ one: 1, two: 2 });
});
});
```

#### toStrictEqual
##### 객체 내의 값의 깊은 비교를 진행 하기 때문에 아래와 같을 경우 false를 return
- 객체 내의 undefined 속성이 있거나 배열의 길이가 다른 경우
- 객체의 속성에 undefined가 있는 경우
- 배열의 길이가 다른 경우
- 객체의 속성 순서가 다를 때
```js
test('객체가 가진 속성의 정확성까지 검사', () => {
  const data = { one: 1, three: undefined };
  data['two'] = 2;
  expect(data).toStrictEqual({ one: 1, two: 2 });
});
```

#### toBeDefined
##### 비교하고자 하는 값이 undefined인지 검사
```js
test('변수의 값이 undefined 인지 확인', () => {
  let test = undefined;
  expect(test).toBeDefined();
});
```

#### toBeTruthy / toBeFalsy
##### false, true 값 검사
```js
test('bool값 확인', () => {
  expect(true).toBeTruthy();
  expect(false).toBeFalsy();
});
```
#### toMatch
##### 정규 표현식 검사
```js
test('정규 표현식', () => {
  expect('test@naver.com').toMatch(/.naver.com/);
});
```
#### toHaveProperty
##### key, value값 검사
```js
test('객체의 키, 값 검사', () => {
  const test = {
    test1: 1,
    test2: 2,
  };

  expect(test).toHaveProperty('test1', 1);
});
```