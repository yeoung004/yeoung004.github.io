# Jest 4 - mock function

> Jest에서 가장 유용한 함수라고 생각합니다. snapshot에서 지속 적으로 바뀌는 값을 고정시킬수도 있고 가상 함수로 만들어 db를 테스트하거나 필요한 값을 지정할수 있어서, 테스트하면서 불필요한 시간을 아낄수 있습니다.

## Mock
<hr />

#### fn()
##### 직접 함수를 만들어 사용이 가능함

```js
  const test = jest.fn(() => '이 함수는 해당 스트링을 return 합니다.')

  test('return test', () => {
    expect(test).toReturn("이 함수는 해당 스트링을 return 합니다.")

    test.mockImplementation(() => '이렇게 mockImplementation를 이용해 수정도 가능')
    expect(test).toReturn("이렇게 mockImplementation를 이용해 수정도 가능")
    test.mockImplementationOnce(() => '이렇게 js에 yield처럼')
    .mockImplementationOnce(() => '한번 호출 할때 마다')
    .mockImplementationOnce(() => '다음 다음으로 넘기게 할수도 있다.')

    test.mockReturnValue('이렇게 지정해도 모두 동일한 값이다')

    // 1,2,3 호출할때매다 실행 되다가 마지막 값이 저장됨
  })
```

#### mock()
##### 모듈에 있는 모든 함수를 mock함수로 만들어줌

```js
  // users.js
  // class Users {
  //   static all() {
  //     return axios.get('/users.json').then(resp => resp.data);
  //   }
  // }
  // export default Users;

  import axios from 'axios';
  import Users from './users';

  jest.mock('axios');

  test('return test', () => {
    // resolve시 해당 값으로 설정
    const resp = { data: users };
    axios.get.mockResolvedValue(resp);

    // users.js에 있는 함수 all에서 실행 중인 axios의 함수를 직접 지정해서 검사
    // axios.get을 실행하지 않아도 돼서 server를 붙여서 일일히 테스트 하지 않아도 됨
    return Users.all().then(data => expect(data).toEqual(users));
  })
```

#### mock prop
```js
  const mockFn = jest.fn()

  // 호출 시 전달된 인자 값
  mockFn.mock.calls()
  // 호출의 반환값, throw 오류
  mockFn.mock.results()
  // mock함수의 instance 값
  mockFn.mock.instance()

  // 함수가 호출될 때마다 특정 값으로 반환되도록 설정
  mockFn.mockReturnValue(value)
  // promise resolve값을 설정
  mockFn.mockResolvedValue(value)
  // promise reject값을 설정
  mockFn.mockRejectedValue(error)

  // mock함수 초기화
  mockFn.mockImplementation(fn)
  // mock함수 초기화(호출 할때 마다 다른 값이 나오게 체이닝을 할수 있음 yield와 비슷)
  mockFn.mockImplementationOnce(fn)

  // 호출 기록을 초기화
  mockFn.mockClear() 
  // 호출 기록,mock 구현을 초기화
  mockFn.mockReset()
  // mock 초기값으로 복원 (주로 jest.spyOn으로 생성된 mock 함수에서 사용)
  mockFn.mockRestore()
```

#### spyOn
##### 기존 mock함수는 mock함수로 test를 위해 만들어 변형되어 실제함수가 아닌 mock함수로 검사를 한다, 실제 함수를 수정 없이 테스트 하고 싶을때 사용하는게 spyOn이다.
```js
const video = {
  play() {
    return true;
  },
};
// spy없이 직접 함수를 호출하면 Matcher error: received value must be a mock or spy function 에러가 나온다
expect(video.play).toHaveBeenCalled();
expect(video.play()).toBe(true);

const spy = jest.spyOn(video, 'play');
const isPlaying = video.play();

expect(spy).toHaveBeenCalled();
expect(isPlaying).toBe(true);

spy.mockRestore(); // 스파이를 제거하고 원래 메서드로 복원
```