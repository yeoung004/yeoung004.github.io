# 네트워크



## 4계층

> 전송계층(Transport Layer)은 송, 수신자의 프로세스를 연결하는 통신 서비스를 제공한다.
>
> 스트림 지원, 신뢰성, 흐름제어, 다중화같은 서비스를 제공하며, 
>
> TCP, UDP프로토콜이 4계층에 속해있다.

 

### 포트번호

> 특정 프로세스와 다른 프로세스 끼리 통신을 하기위한 번호이다.
>
> 하나의 프로세스는 하나의 포트번호만 사용이 가능하다.



- **Well - Known Port Number**
  - 이름 그대로 잘 알려진 서비스별로 정해진(약속한) 포트 번호

| 서비스 이름 | 포트번호 |
| :---------: | :------: |
|     FTP     |  20, 21  |
|     SSH     |    22    |
|   TELNET    |    23    |
|     DNS     |    53    |
|    DHCP     |  67, 68  |
|    TFTP     |    69    |
|    HTTP     |    80    |
|    HTTPS    |   443    |



- **Dynamic Port**
  - 서버가 아닌 일반 사용자들이 사용하는 포트 번호 범위(약 15000개)

| 시작 포트 번호 | 마지막 포트 번호 |
| :------------: | :--------------: |
|     49152      |      65535       |



- **Registered Port**
  - Well known정도는 아니지만 어느정도 공신력 있는 서비스

|   서비스 이름    | 포트 번호 |
| :--------------: | :-------: |
|  오라클 DB 서버  |   1521    |
|    MySQL 서버    |   3306    |
| MS 원격 데스크탑 |   3389    |



(cmd창에서 netstat -ano 명령어를 이용할 경우 어떤 프로그램들이 연결 되어 있는지 확인가능)



### UDP

> 전송방식이 너무 단 순 해서 서비스의 신뢰성이 낮고, 순서가 바뀌거나, 중복, 누락이 되기도 한다.
>
> 오류의 검사 수정이 필요 없는 프로그램에 주로 사용된다.

![image-20211002192444851](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20211002192444851.png?raw=true)

- DNS서버에서 사용됨(도메인 -> IP)
- TFTP 서버
- RIP 프로토콜
  - 라우팅 정보를 공유



### TCP

> 안정적, 순서대로, 에러없이 교환할 수 있는 프로토콜
>
> TCP는 UDP와 다르게 안정성, 신뢰성을 중요시 하기 때문에, 전송속도는 느리다.

![image-20211002194254429](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20211002194254429.png?raw=true)

- Offset : Header 길이
- Window : 송신할 데이터의 크기를 요청



#### TCP Flags

> 데이터의 형태를 나타내는 값들이다.

- U (Urgent Flag) : 이 값이 설정됐으면, 이 데이터를 처리하는 우선순위가  높아짐
  - Urgent Pointer와 짝궁이며, 어디서 부터가 긴급데이터 인지 알려줌

- A (Ack) : 송신자가 요청할 때 승인이라는 것을 알려줄 때 사용
- P(Push) : TCP버퍼가 일정 크기가 쌓이지 않고도 데이터를 보냄
- R(Reset) : 지금까지 연결된 관계를 다시 초기화
- S(Sync) : 상대방과 연결을 시작할 때 사용 
- F(Fin) : 데이터를 다 주고 받고 마지막에 종료 



#### TCP 통신 과정

- 3 Way HandShake

![What is a TCP 3-way handshake process?](https://s3.ap-south-1.amazonaws.com/afteracademy-server-uploads/what-is-a-tcp-3-way-handshake-process-three-way-handshaking-terminating-connection-6ea4a4c72d165361.jpg)

1. 클라이언트가 서버에게 요청 패킷을 보냄
2. 서버가 클라이언트의 요청을 받아들이는 패킷을 보냄
3. 클라이언트는 이를 최종적으로 수락하는 패킷을 보냄























### 약어

- TCP : Transimission Control Protocol
- UDP : User Datagram Protocol