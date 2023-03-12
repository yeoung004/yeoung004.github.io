# SOAP & REST 프로토콜 
![network](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2234&q=80)
> 프로토콜은 통신규약 즉 기기 간의 소통 방식을 미리 정해 놨습니다. 데이터를 보내고 받는 방법, 데이터의 내용과 구조, 데이터 전송 시 사용되는 주소 등을 미리 정의해 놨죠. 예시로 HTTP / HTTPS / FTP / SFTP / SSH / Telnet / SOAP 등등 각 목적에 맞게 정해저 있는 방식을 사용하면 됩니다.

## 📌SOAP(Simple Object Access Protocol)

### 📌SOAP?
![SOAP](https://user-images.githubusercontent.com/22961251/154504754-413e3c8b-f689-4d6b-a730-63b6f255655a.png)
- 웹상에 있는 객체(형식화된 데이터)를 접근하기 위한 방식
- SOAP은 네트워크 통신에서 데이터의 송수신을 관리하는 기술
- 클라이언트와 서버 간에 통신할 때 XML 형식으로 데이터를 교환
- 웹에서 구조화된 데이터를 교환하는 데 사용되는 메시징 프로토콜
- http / https를 통해서 XML 메세지를 교환

### 📌용어정리
---
#### WSDL(Web Service Description Language)
간단하게 말하자면 보내는 데이터 양식, 받는 데이터 양식 등등을 기술한 설명서이다.

WSDL 예시
```
<?xml version="1.0" encoding="UTF-8"?>
<description xmlns="http://www.w3.org/ns/wsdl"
             xmlns:tns="http://www.example.com/wsdl20sample"
             xmlns:whttp="http://www.w3.org/ns/wsdl/http"
             xmlns:wsoap="http://www.w3.org/ns/wsdl/soap"
             targetNamespace="http://www.example.com/wsdl20sample">


<!-- Abstract types -->
   <types>
      <xs:schema xmlns="http://www.example.com/wsdl20sample"
                 xmlns:xs="http://www.w3.org/2001/XMLSchema"
                 targetNamespace="http://www.example.com/wsdl20sample">

         <xs:element name="request">
            <xs:complexType>
               <xs:sequence>
                  <xs:element name="header" maxOc
                  ...
```

#### UDDI
개발자들이 만든 WSDL를 올려놓은 클라우드 저장소(창구)

### 📌SOAP 프로세스
프로세스는 간단하다 물론 상세하게 들어간다면 더 복잡해 지겠지만 보내고 받고 또 보내고 받고다.
요청 메세지 작성 => 요청 메세지 전송 (HTTP)=> 요청 메세지 수신 => 응답 메세지 작성 => 응답 메세지 전송 (HTTP)=> 응답 메세지 수신

SOAP 프로토콜을 사용하기 위해선 WSDL(양식) UDDI에 등록 후 통신을 할떄마다 무조건 거처야 한다. 이는 성능 및 속도가 떨어진다. 또 기술적으로도 상당히 복잡하다 위 WSDL 예시와 같이 복잡한 양식을 작성해야한다. 위 단점을 극복하기 위해 REST 통신이 나왔다.

---

## 📌REST(Representational State Transfer)
- URI(Uniform Resource Identifier)를 통해 모든 경로를 지정
- HTTP 메서드(GET, POST, PUT, DELETE 등)를 이용하여 자원에 대한 요청과 응답을 처리
- 서버와 직접 통신하지만 SOAP처럼 중간에 단계를 추가가능
- 캐시를 통해 자주 사용하는 데이터를 저장하여 서버부하 및 처리속도 향상

### 📌REST 메소드 정리
자주사용
- GET: 데이터 조회(데이터 생성, 추가 불가)
- POST: 데이터를 생성
- PUT: 전체 데이터를 업데이트
- DELETE: 데이터를 삭제하기
- PATCH: 리소스의 일부를 수정

자주 사용x
- HEAD: 데이터 조회 (응답 본문 미포함) / 서버의 응답 상태를 확인용
- OPTIONS: 서버에서 지원하는 메소드의 종류, 지원하는 헤더, CORS 같은 추가 정보를 얻을 때 사용
- CONNECT: 클라이언트와 서버 간의 연결을 설정하기 위해 사용하(주로 프록시와 같은 중개 서버)
- TRACE: 요청이 서버에 도달할 때까지 경로를 따라 메시지를 반복해서 돌려주는 메소드(디버깅용)


### 📌RESTful
아래 특징을 가진 서비스를 RESTful한 서비스라고 정의한다.
- 자원(Resource) 중심적인 URI 설계
- HTTP Method를 이용한 자원 처리
- Stateless(상태를 유지하지 않음)
- Self-descriptive message(메시지 스스로를 설명할 수 있는 자체 표현 구조)
- HATEOAS(Hypermedia As The Engine Of Application State)를 만족하는 하이퍼미디어 제공

### 📌결론
두 방식중에 어떤 방식이 정답이라고 할수 없다 아키텍쳐는 새로운 시장의 요구가 달라 졌기 때문에 그것에 반응하기 위해 만들어지는 경우도 더러 있다.
속도를 얻되 보안성과 표준화를 놓을 것인가 보안성와 표준화를 얻되 속도와 편리함을 놓을 것인가는 어떤 서비스를 제공하는지 또 어떤 부분을 중심으로 서비스를 만들건지에 초첨을 맞춰야된다고 생각한다.