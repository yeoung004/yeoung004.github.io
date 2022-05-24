## Why I pick this tech tree



### Server:floppy_disk:

#### < MySQL or MongoDB >

**MongoDB**는 **NoSQL**(Not Only Sql)중 가장 대표적인 한가지이다.

기존 RDB(Relational Data Base)의 데이터 처리 속도로는 대량의 데이터를 처리하는 무리가 있기에 NoSQL의 장점이 더욱 크게 부각이 되었다.

MongoDB는 관계를 설정하지 않고 Key-value 형태의 json을 사용하기 때문에 기존 RDB에서 사용하는 Join을 사용할 수 없다. 

또 메모리자원에 의존적이기 때문에 고성능의 하드웨어 성능을 요구한다.

하지만 가장 큰 단점으로 스키마를 설정하지 않아도 되기 때문에 데이터 손실, 중복들에 위험이 있다. 계정, 계산등의 DB 서버 구축으로는 적합하지 않다.



**MySQL**은 open source이기 때문에 누구나 무료로 이용이 가능하다. 또한 RDB의 대표중 한가지 이기 때문에 규모가 상대적으로 작거나 큰 app에 매우 적합하다.

**그렇기에 DB는 Mysql로 결정**



#### < REST API vs GraphQL >

과거 스마트폰의 출현으로 RESTful라는 개념이 새로 도입되었다. client에서 uri로 쿼리를 요청하면   server API에서 요청한 정보를 주는 형식의 방법론이다.

과거에는 한명의 백엔드 개발자가 Server, DB등을 모두 조작을 했지만, 현재는 한명의 개발자가 감당하기에는 서비스 규모가 커졌다. 그렇기에 RESTful이라는 방법론이 필요했지만, 나날이 새로 생기는 수 많은 기기에 맞는 정보를 처리하자니 호환이 잘되지 않아 정보를 과하게 넘겨 자원을 낭비하게 되고 필요없는 정보를 넘겨주게 돼서 속도도 느려지는 문제가 발생했다.

GraphQL은 정보를 원하는 만큼만 요청할수 있다는 RESTful의 단점을 보완하여 만들어진 Query Language이다. 즉 server에 정보를 요청하는 횟수를 줄이기 때문에 속도를 향상시키고, 자원을 보다 효율적이게 사용할 수 있게 되었다.

**그렇기에 Data요청은 GraphQL로 결정**



### Express

Express는 Node.js를 위한 빠르고 간결한 서버사이드 웹프레임워크이다.

기존 Node.js의 코드를 더욱 간단하고 빠르게 사용할 수 있게 해주며, request, response를 간단히 설계 할 수 있다.

최근 전세계 개발자들로 부터 사랑받고 있는 중이라 커뮤니티 활동이 활발하고, 많은 npm패키지를 제공하기 때문에 서버를 만들때 필요한 기본 기능들은 불러와서 사용이 가능하다

#### 출처

MongoDB

- https://elky84.github.io/2018/09/26/mongodb/

- https://blckchainetc.tistory.com/350