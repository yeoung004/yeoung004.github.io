# 네트워크



### HTTP

> www에서 쓰이는 핵심 프로토콜, 문서의 전송을 위해 쓰이며, 음성, 화상 등 여러 종류의 데이터를 MIME로 정의 하여 전송 가능 하다.
>
> HTTP는 Request / Resoponse 동작에 기반하여 서비스 제공한다.

- 초기 버전 1.0
  - 초기의 간단한 웹 페이지에서는 3 Way Handshake를 한뒤, HTTP를 요청, 응답을 받고 연결 종료 후 다시 위 내용을 반복을 함 -> 서버의 부하

- 현재 버전 1.1
  - 전 버전의 문제점을 간단하게 연결이 되었으면, 모든 요청, 응답이 끝날때 까지 계속 연결을 시켜놨다가 마지막에 끊는 방식으로 변경

- HTTP 프로토콜의 구조는 사람이 이해할 수 있는 언어로 사용

  | 요청 프로토콜 구조 |
  | :----------------: |
  |  **REQUEST LINE**  |
  |    **HEADERS**     |
  |     **EMPTY**      |
  |      **BODY**      |









#### REQUEST

- (  **요청타입**	|	공백	|	**URI**	|	공백	|	**HTTP버전**	)

![image-20211003220511916.png](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20211003220511916.png?raw=true)

- GET은 데이터를 요청 할 때 데이터를 전송하면서 요청 할 수 있음
  - URI로 (?뒤에 쿼리로 요청)
  - 데이터가 노출되기 때문에 중요한 데이터는 GET으로 사용하지 않음

- POST 방식은 중요 데이터를 BODY에 숨겨서 보냄
  - 패킷을 캡쳐하면 확인 할 수 있기 때문에 요즘 HTTPS를 사용

- URI는 자원을 나타내는 주소값(전체 값)
  - ex)https://www.naver.com/webtoon/list.ngn?titleId=1111111&weekday=thursday
  - scheme ://host :port /path ?query
- URL은 쿼리를 제외한 앞의 값들
  - ex)https://www.naver.com/webtoon/list.ngn



| 응답 프로토콜 구조 |
| :----------------: |
|  **STATUS LINE**   |
|    **HEADERS**     |
|     **EMPTY**      |
|  **BODY**(데이터)  |







#### RESPONSE

-  (	**HTTP버전**	|	공백	|	**상태코드**	|	공백	|	**상태문구**	)

![image-20211003223339695.png](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20211003223339695.png?raw=true)

- 200번 대: 정상적인 상태
  - 200 : 정상
- 400번 대 : Client측의 에러
  - 403  Forbidden : Client가 권한이 없는 페이지를 요청했을 때
  - 404  Not Found : Client가 서버에 없는 페이지를 요청했을 때
- 500번 대 : Server측의 에러
  - 500 Internal Server Error : Server의 일부가 멈췄거나 설정 오류가 발생
  - 503 Service Unavaildable : 최대 Session수를 초과했을 때







### HEADER

- Content-Length : 메시지 바디 길이를 나타낼 때 쓰임
- Content-Type : 메시지 바디에 들어있는 컨텐츠 종류(HTML문서는 text/html)

- HEADER TYPES
  - Cookie : 서버로 부터 받은 쿠키를 다시 서버에게 보내주는 역활
  - Host : 요청된 URL에 나타난 호스트명을 상세하게 표시
  - User-Agent : Client Program에 대한 식별 가능 정보를 제공

- 응답헤더 : 서버의 정보을 담고 있음
  - Server : 사용하고 있는 웹서버의 소프트웨어에 대한 정보
  - Set-Cookie : 쿠키를 생성하고 브라우저에 보낼 떄 사용, 해당 쿠키 값을 브라우저가 서버에게 다시 보낼 때 사용









### 약어

- HTTP : Hypertext Transfer Protocol
- HTTPS : Hypertext Transfer Protocol over Secure Sockets Layer
- URI : Uniform Resource Identifier

