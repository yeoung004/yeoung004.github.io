## Javascript



### async/defer

#### 기존방식

html코드를 parsing html하다가 script코드를 fetching해야하면 잠시  parsing html를 block시켜 script를 fetching, executing후 parsing html을 재개 했다. 이런 방식은 script 용량이 너무 크거나, fetching 할 js가 많을 경우 page loading을 사용자가 하염없이 기다리기만 하는데...



#### async

```html
<script async src="index.js"></script>
```

parsing html을 하던중에 script를 fetching 할 때, script fetching하면서 parsing html을 동시에 수행하게 된다. parsing html이 전부 끝났을 경우, executing을 수행한다. 이 방식은 사용자가 기다리지 않아도 되는 장점이 있지만, html이 js에 의존하게 될 경우 페이지가 정상작동하지 않을 수 있다.



#### defer

```html
<script defer src="index.js"></script>
```

parsing html을 하던중 script를 fetching해야하는 경우 parsing html과 fetching js를 동시에 하면서 executing은 작업자가 명시한 순서대로 작업을 하게 된다. 가장 이상적이며 header안에서 fetching js를 하게 될경우가 가장 이상적이다.



### use strict

js소스 가장 위에 

```javascript
'use strict';
```

입력하고 코드를 작성할 시 초창기 flexible한 언어라는 개념으로 만들어진 javascript의 위험성을 보다 안전하게 작성할 수 있다. 

예를 들어

```javascript
variable = 6;
console.log(variable);
```

선언도 하지 않은 변수에 값을 할당하고 출력까지 해도 아무런 문제없이 정상작동하는 말도 안되는 일은 일어나지 않는다.



### NaN/null/undefined

위 값들은 얼핏보면 같다고 생각이 들지만 전부 다른 값이다.



#### NaN

Not a Number의 약자로 사용자가 number type의 값을 기대하고 사용할때 number type외의 값이 반환되면 return 되는 값이다.

```javascript
> 18 - "String";
< NaN
```



#### null

선언, 할당은 되었지만, 아무런 값도 가지지 않은 변수값 이다.



#### undefined

선언은 되었지만, 할당이 안 된 변수를 사용 할 때 반환되는 값이다.



### ==/===

```javascript
const coercionaryVariable = true + 4;
console.log(coercionaryVariable);
<5
```

위와 같이 javascript는 기본적으로 강제적으로 타입을 바꾼다. 



#### ==

무언가를 비교 할 때 사용하는 == 연산자는 타입변환에 강제성을 띠우고 있다.



#### ===

==와 반대되는 성격으로 type이 같은지 비교를 할 때 가장 이상적인 선택이다.



### typeof/instanceof

변수의 자료형을 알고 싶다면 사용하는 명령어



#### typeof

```javascript
const num = 123;
typeof num
< number
```

어떠한 자료형이던 사용가능 하지만 null은 Object형으로 값이 반환 되는 이상한 오류가 있다.



#### instanceof

```javascript
const myCellPhone = {
	brand:'Samsung',
	version:'note20',
	color:'black'
};
console.log(myCellPhone instanceof Object);
< true
```

왼쪽의 인스턴스가 오른쪽 클래스의 인스턴스인지를 안려주는 명령어

*null instanceof Obejct;는 false를 반환*



### parameter

#### default parameter

```javascript
function profile(name, age=24) {
	console.log(name, age)
}
profile(최영성);
```

파라미터의 값을 default로 지정해버려서 undefined가 반환되지 않도록 방지



#### rest parameter

```javascript
function skillStacks(...args) {
	for(let i = 0; i < args.length; i++) {
		console.log(args[i]);
	}
}

skillStacks("Spring", "React.js", "Javascript", "java", "node.js", "React Native");
```

parameter값을 배열로 받는다는 것을 명시한다.



### for

```javascript
args.forEach((arg) => console.log(arg));
```

배열의 값을 하나씩 뽑아옴



```javascript
for(cosnt arg of args) {
	console.log(arg);
}
```

위 기능과 동일



### hoisting

자바스크립트는 hoisting이라는 개념을 지원한다.

```javascript
log();
const log = function () {
	console.log("writing...");
}
```

var타입 변수, **function declaration**을 선언, 할당 전에 호출해도 실행이 가능한데 javascript가 앞에서 말한 두가지를 가장 위에 자동으로 올려준다.



### callback function

```javascript
console.log(1);
setTimeout(() => console.log(2), 1000);
console.log(3);
```

![image-20211021235008706](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/JavaScript/image-20211021235008706.png?raw=true)

javascript는 stack에서 함수를 호출한다. 만약 setTimeout같은 API를 호출 할 경우 webAPI에 무조건 가게 되어서 Message Queue를 거처 stack에 다시 가게 되는데 stack이 비어있어야 출력을 할 수 있다.

그래서 출력순서는 1,3,2이다.





















