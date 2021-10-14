# Function

> 함수는 한가지일만 해야한다.
>
> 함수는 잘지어진, 서술적인, 긴 이름을  갖는 많은/작은 함수들로 유지 해야한다.
>
> 큰 함수는 클래스로 추출해야한다.
>
> 함수는 더이상 작아질 수 없을 만큼 작아야한다.

함수로 추출하는 과정중에 약간의 규칙이 있다

- 함수는 작아질 수 있는한 최대한 작아야함

  - 함수 선언문에 들어가지 않고도 어떤함수인지 알 수 있게 작성

- if, else, while 문장등의 내부 블록은 한 줄

  - 괄호가 없어야 함

- 들여쓰기가 적어야함

  - 함수는 중첩 구조를 가질 만큼 크면 안됨


- 함수는 1가지일만 한다는 것은 독자 입장이 아닌 caller입장에서 한가지



결국 함수 추상화가 개발자가 해야할 일이다. 하지만 추상화라는 개념은 정말 쉽지 않다. 더더욱 개발 경험이 부족하거나, 소프트웨어공학에 대한 전반적인 지식이 부족하면 말이다... 

유명한 책을 쓴 저자도, 강의자도 추상화는 내가 포기 할 때까지 해야한다고 말한다. 

특히 if, while이 보이면, extract할 대상이라고 의심을 해야한다.



포인트

1. 함수의 규모는 작아야한다.
2. 위 함수보다 작아야한다.
3. 이름을 잘지어야한다.
4. 함수는 한 가지 일만 해야한다.
5. 더이상 추출 할 수 없을 때까지(바꿀게 이름 말고 없을 때까지) 해야한다.



### Function Structure

#### 1. Arguments

1. 함수의 파라미터는 3개 이하를 지향한다.(그 이상가면 작성자 조차도 뭐였는지 알 수가 없다.)

   만일 시작, 끝을 파라미터로 받아 온다면 범위 값을 줘서 파라미터의 숫자를 줄일 수가있다.

   ex) amountInvoicedIn(start: Data, end: Data) 	**=>** 	amountInvoicedIn(DataRange)

   이렇게 되면 가독성도 좋아지고 파라미터값이 정확히 어떤건지 알기도 쉽다.

```java
package function_structure;

public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int sodium;
    private final int carbohydrate;

    public NutritionFacts(int servingSize, int servings) {
        this.servingSize = servingSize;
        this.servings = servings;
    }

    public NutritionFacts(int servingSize, int servings, int calories) {
        this.servingSize = servingSize;
        this.servings = servings;
        this.calories = calories;
    }

    public NutritionFacts(int servingSize, int servings, int calories, int fat) {
        this.servingSize = servingSize;
        this.servings = servings;
        this.calories = calories;
        this.fat = fat;
    }

    public NutritionFacts(int servingSize, int servings, int calories, int fat, int sodium) {
        this.servingSize = servingSize;
        this.servings = servings;
        this.calories = calories;
        this.fat = fat;
        this.sodium = sodium;
    }

    public NutritionFacts(int servingSize, int servings, int calories, int fat, int sodium, int carbohydrate) {
        this.servingSize = servingSize;
        this.servings = servings;
        this.calories = calories;
        this.fat = fat;
        this.sodium = sodium;
        this.carbohydrate = carbohydrate;
    }

}
```

식품에 대한 데이터를 저장하는 Class가 있다.

여기서 마지막 생성자를 호출해서 파라미터의 값들을 넘겨 줄때

```java
package function_structure;

import org.junit.Test;

public class NutritionFactsTest {
    @Test
    public void canCreate() {
        NutritionFacts cocacola =
                new NutritionFacts(240, 8, 100, 0, 35, 27);
    }
}
```

이런식으로 숫자만 넘겨주게 되는데 작성자 조차도 파라미터가 많아질수록 어떤 값을 넘기는지 어려워 진다.

여기서 Java Bean Pattern을 사용해서 해결할 수 있다.

```java
package function_structure;

public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int sodium;
    private final int carbohydrate;

    public static class Builder {
        // Required parameters
        private final int servingSize;
        private final int servings;
        // Optional parameters
        private final int calories = 0;
        private final int fat = 0;
        private final int sodium = 0;
        private final int carbohydrate = 0;

        public Builder(int servingSize, int servings) {
            this.servingSize = servingSize;
            this.servings = servings;
        }

        public Builder calories(int val) {
            calories = val;
            return this;
        }

        public Builder fat(int val) {
            fat = val;
            return this;
        }

        public Builder sodium(int val) {
            sodium = val;
            return this;
        }

        public Builder carbohydrate(int val) {
            carbohydrate = val;
            return this;
        }

        public NutritionFacts build() {
            return new NutritionFacts(this);
        }
    }

    private NutritionFacts(Builder builder) {
        servingSize = builder.servingSize;
        servings = builder.servings;
        calories = builder.calories;
        fat = builder.fat;
        sodium = builder.sodium;
        carbohydrate = builder.carbohydrate;
    }
}
```

이런식으로 Builder class를 만들어서 getter를 만들어 자기 자신을 return한다.

이렇게 만들면

```java
package function_structure;

import org.junit.Test;

public class NutritionFactsTest {
    @Test
    public void canCreate() {
        NutritionFacts cocacola =
                new NutritionFacts.Builder(240, 8).
                        calories(100).
                        sodium(35).
                        carbohydrate(27).
                        build();
    }
}
```

이렇게 가독성이 올라간다. 

각 파라미터값이 어떤것을 의미하는지 한눈에 알아보기 쉽다.



2. Boolean 인자는 가급적 사용하지 말자

함수를 만들 때 해야할 것은 최대한을 쪼갤수 있을 때까지 쪼개는 것이다.

값이 들어와서 **true**일 경우와 **false**일 경우라는 2가지 동작이 함수에 들어가 있으면 extract를 해서 행위을 나누고 또 공통된 점이 있다면 다시 쪼개는 이런식으로 하면 코드가 단순해지고 복잡도는 줄어들게 된다.



3. output인자를 사용하지 말자

인자 값을 받아서 그 변수를 재사용하는 개발자도 있다.

이 코드를 작성한 작성자는 이해할지 몰라도 다른 팀원들이나 유지보수를 하는 개발자는 이해하기 어려운 코드가된다. 이럴 경우는 로컬변수를 만들어서 사용하는 것이 효율적이다.



4. null값을 함수의 return 값으로 사용하지 말자

null값도 결국 null인값과 아닌 값으로 나뉘어진다. 이러면 앞에서 말했던 boolean값과 마찬가지로 2가지의 행위가 생기는 것이다.



5. 코드에 null체크, 에러체크로 더럽히지 말자

코드에 null체크, 에러체크가 있다는 것은 개선의 여지가 있다는 의미이기도하다.

또 위 의미는 팀원들이나, 단위 테스트를 못믿어서 작성한 것이라는 의미도 있다.

null여부에 대해서는 지속적으로 체크하지 말고, TDD 즉, 단위 테스트를 해서 검증을 해야한다.



### 2. The Stepdown Rule

> 모든 public은 위에, 모든 private는 아래에

중요한 부분은 위로, 상세한 부분은 밑으로 해서 public part만 사용자에게 전달하면 된다.

잡지를 예시로 들면, 헤드라인을 먼저 보여주는 것과 같다.



위 방법에 대한 이점은 다음과 같다.

- 편집자들은 오해가 없이 디테일한 부분을 제거하고 필수 적인 요소들만 전달 할 수 있다.
- 독자들은 위에서 부터 읽기 시작하고, 이해를 할 것 같다면 그만 읽으면 된다.

```java
public void serve(socket s) {
    try {
        tryProcessInsertructions(s);
    } catch(Throwable e) {
        slimFactory.stop();
        close();
        closeEnclosingServiceInseperateThread();
    }
}

private void tryProcessInsertructions(socket s) throws Exception {...}
```

이런식으로 함수가 있다면 바로 **아래**에 있어야 가독성이 증가한다.



### 3.Switches And Cases

Switch문을 사용하면 case문에서 의존성문제가 있기 때문에 되도록이면 사용하지 않는 것이 좋다.

의존성을 최대한 줄여야 독립적으로 분리가 되는 객체지향적인 코드가 된다.

switch문의 문제점은 case문에서 변경이 일어나면 switch를 수정해야한다.



### 4.Temporal Coupling

함수들이 순서를 지키며 호출되어야한다.

예시를 들면,

```java
//file should be opend before processing
fileCommand.process(file);
//file should be closed after processing
```

이런식으로 파일을 처리하기 전에 파일은 열려있어야 하고, 파일을 처리한 후에 파일이 닫혀 있어햐한다.

만약, 사용자가 이런형식을 지키지 않고 실행할 경우 에러는 날수 밖에 없다.



```java
fileCommandTemplate.process(myfile, new FileCommand() {
    public void process(File f) {
        // file processing codes here
    }
});

class FileCommandTemplate{
    public void process(File file, FileComand command) {
        file.open();
        command.process(file);
        file.close();
    }
}
```

개발자는 이런식으로 실행하는 부분이 복잡하면 따로 빼거나 해서 사용자가 에러를 낼수 있는 여지를 제거한다.



### 5.CQS

Command(명령)함수와 Query(질의)함수를 각각 함수명대로 동작, 기능 해야한다. 만일 Query함수인데, 내부의 데이터를 조작하거나, Command함수인데 return값이 있거나하면, 개발자에 대한 신뢰가 떨어져서 코드를 읽을 때 내용을 전부 봐야되는 경우가 발생한다.



가장 이상적인 Side effect(예상외의 반응)관리 방법

1. 상태를 변경하는 삼수는 값을 반환하면 안됨
2. 값을 반환하는 함수는 상태를 변경하면 안됨

- Command
  - 시스템의 상태 변경 가능
  - return값 X
  - side effect를 가지고 있음(변화)
- Query
  - 계산값이나, 상태를 반환
  - side effect가 없음

```java
User u = authorizer.login(userName, password);
```

로그인을 할 때마다 값을 반환 받는다. 로그인한 유저 정보를 받고 싶지 않는데도 받아야한다.

```java
authorizer.login(userName, password);
User u = authorizer.getUser(userName);
```

이런식으로 사용자가 예상 가능한 코드를 짜야 다른 동료 개발자나, 독자에게 개발자에 대한 신뢰성 생긴다.



### 6.Tell, Don't ask

함수를 만들 때 중요한것 중 하나가 말하는 것이다.

무언가에게 물어보게 되면, 함수는 엮은 그물이나, 체인같은 구조가 된다.

```java
o.getX()
    .getY()
	    .getZ()
    		.doSomething();
```

이러식으로...

어떤 사람이 봐도 이런것은 이해하기 힘들고, 결국 의존성만 높아지게 된다.

```java
o.doSomething();
```

이렇게 바꿔서 doSomething이 다른 함수를 또 부르는 식으로 처리를 해야한다.



### 7.Law of Demeter

위의 사태를 방지하기 위해 Tell, Don't ask의 몇가지 규칙이 있다.

객체는 아래의 메소드만 호출할 수 있다.

- 인자로 전달된 객체
- localy 생성한 객체
- 필드로 선언된 객체
- 전역 객체

위 규칙을 잘 지키면, 코드의 가독성을 높아지고 복잡한 의존성은 끊어 질수 밖에 없다.

객체는 최종 목적지까지 알필요 없이 최종 목적지까지 가는 과정중 다음 목적지만 알면 테스트코드를 짜는 것도 간단해 진다.



### 8.early returns

```java
private boolean nameIsValxxxx () {
    if(name.euqls(""))
        return true;
    if(!wikiWordWidget.xxx)
        return true;
    return false;
}
```

early return이나, guarded return은 허용되만 가급적 읽기 쉬운 코드를 만들기 위해서는 무엇이 독자에게 더 나은 코드인지를 생각하며 짜야한다.

하지만 early return이 문제인 것은 loop에서 발생한다.

loop에서 return이 발생할 경우 독자도 읽기 어려워지고 테스트도 하기 어려워 진다. **동작 < 이해**





## 약어

- CQS : Command Query Separation



## 참조

- 백명석의 클린코드 Youtube 강좌

