# Form

### 1.Coding Standards

> 별도의 문서에 coding standards를 작성하는 것은 추천하지 않는다.
>
> 코드 자체가 coding standards가 되어야 한다.

커멘트는 코드에 나와있는 내용을 적으면 결국 의미가 없는 커멘트라 생각하고 독자들은 읽지 않게된다. 

정작 필요한 커멘트를 작성했는데도 아무도 보지않게되는 불상사가 일어나게 된다.



### 2.Comments are Failures

즉 커멘트를 꼭 필요한 내용에서만 작성해야하는데 과거 Assembly언어들은 표현력이 다소 떨어졌던 언어들이였다 지금은 대부분의 언어가 뛰어나게 코드를 작성할 수 있기 때문에 좋은 코드를 작성하는데 노력을 더 하는것이 바람직하다.



### 3.Good Comments

꼭 작성해야하는 커멘트 종류

- Legal Comments(법적)
- informative Comments(정보)
  - 입력해야되는 날짜 포멧스트링, 형식등
- Warning of Consequences(경고문)
  - 테스트를 하는데 너무 오래 걸리면, 커멘트로 경고를 줌
- TODO Comments(해야할일, 관리할일)
- Public API DOC(공개적인 문서들)

위의 공통적인 것들은 사용자들이 알면 작성자에게 감사할 것들이다. 이런 내용들을 커멘트로 작성해야 한다.



### 4.Bad Comments

반대로 적으면 안되는 코멘트도 있다.

- Mumbling
  - 말이 계속 이어지는 필요없는 정보들
- Redundant Explanations
  - 코드만 봐도 알수 있는 내용들
- Mandated Redundancy
  - 함수에대해(입출력) 다시 커멘트로 알려줌
- Journal Comments
  - 작성, 변경 정보(형상관리)
- Noways Comments
  - 예시로 아무것도 없는 생성자에 default constructor라고 다시 알려주는 커멘트
- Big Banner Comments
  - 광고같이 잘보이라고 작성하는 커멘트
- Closing Brace Comments
  - 범위의 시작과 끝을 작성(기본 IDE에서 제공)
- Attribution Comments
  - 작성자 커멘트
- HTML in Comments
- Non-Local In Information
  - 관련있는 코드와 동떨어진곳에 작성



### 5.Vertical Formatting

공란을 마구잡이 식으로 사용하여 독자들에게 혼란을 주는 경우가 많이 존재한다.

아래는 저자가 코드에서 공란 표기를 추천하는 부분이다.

- 메소드 사이
- private, public 변수들 사이
- 변수 선언, 메소드 실행의 나머지 부분사이
- if, while 블록과 다른 코드 사이

관련된 부분들을 한곳에 같이 놔두는 것도 중요한 포인트이다.



### 6.Classes

앞서 계속 말했던 것처럼 객체간의 의존성을 낮춰야한다.

클래스는 private 변수들을 public 함수로 조작하고, private 변수는 외부에서 존재하는지 조차 몰라야한다.

그렇기에 getter, setter, property등을 제공하는 것은 나쁜 설계다.

객체지향에서 가장 중요한 개념인 "의존성은 낮되, 결합도는 높아한다"를 지키려면 getter, setter는 좋지 않은 코드다. getter, setter는 10개의 변수가 있다면 1개씩 밖에 사용하지 않는다.

그렇다고 getter를 사용하지 않을 수는 없기에, 추상화 개념을 사용하는 것이다.

![image-20211015224622509](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Clean_Code/image-20211015224622509.png?raw=true)

gallonsOfGas변수를 getPercentFuelRemaining()함수가 접근하지만 사용자의 입장에서는 알수가 없다. 이것이 다형성을 지원하는 좋은 코드이다.























## 참조

- 백명석의 클린코드 Youtube 강좌

