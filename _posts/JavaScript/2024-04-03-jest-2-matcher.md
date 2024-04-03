# Jest 2 - Matcher

> 주로 함수를 검사하거나 모니터링 할때 사용하는 Matcher다. 함수를 검사할때 또 React, React Native에서 자주 사용하는 테스 기법인 snapshot을 사용할때 꼭 필요한 기능이 있는데 jest에서 제공하는 mock함수다.

사용법

```js
// 아래와 같이 jest.fn()으로 주면 된다.
const mockFunction = jest.fn();

// 아래처럼 return값을 지정해 줄수 있다
const hasReturn = jest.fn(() => 1);
```

## Matcher
<hr />

#### toBeCalled & toHaveBeenCalled
##### 호출 여부
```js
const mockFunction = jest.fn();
mockFunction();

test('함수 호출 여부', () => {
  // 이름만 다르고 기능은 동일
  expect(mockFunction).toBeCalled();
  expect(mockFunction).toHaveBeenCalled();
});
```

#### toBeCalledTimes & toBeCalledWith
##### 호출 횟수, 호출시 인자값 확인
```js
const mockFunction = jest.fn();
mockFunction();

test('함수 호출 여부', () => {
  // 몇번 호출
  expect(mockFunction).toBeCalledTimes(1);
  // 어떤 인자 값과 호출
  expect(mockFunction).toBeCalledWith();
});
```

#### toReturn & toHaveReturned
##### return 값 확인
```js
test('함수 반환 여부', () => {
  const hasReturn = jest.fn(() => 1);

  hasReturn();
  // 이름만 다르고 기능을 동일
  expect(hasReturn).toReturn();
  expect(hasReturn).toHaveReturned();
});
```

#### toReturnTimes & toHaveReturnedTimes
##### return 호출 여부
```js
test('함수 반환 여부', () => {
  const hasReturn = jest.fn(() => 1);

  hasReturn();

  // 비교 값을 몇번을 반환했는지, 이름만 다르고 기능은 동일
  expect(hasReturn).toReturnTimes(1);
  expect(hasReturn).toHaveReturnedTimes(1);
});
```

#### 비동기 함수 테스트
##### promise, async & await, callback을 검사하기
```js
test('done을 이용해 검사하기', done => {
  function callback(data) {
    try {
      expect(data).toBe('peanut butter');
      done();
    } catch (error) {
      done(error);
    }
  }

  fetchData(callback);
});

test('Promise에서 검사하기', () => {
  return fetchData().then(data => {
    expect(data).toBe('peanut butter');
  });
});

test('Promise에서 검사하기', () => {
  return expect(fetchData()).resolves.toBe('peanut butter')
});

test('async & await 검사하기', async () => {
  const data = await fetchData();
  expect(data).toBe('peanut butter');
});

test('async & await 검사하기', async () => {
  await expect(fetchData()).resolves.toBe('peanut butter');
});

```