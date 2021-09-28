# 네트워크



### 3계층

> 2계층은 단거리 네트워크였지만, 3계층은 멀리 떨어져있는 컴퓨터까지 
>
> 어떻게 데이터를 전달할지 제어하는 계층(패킷의 경로를 제어)
>
> LAN - WAN - LAN



#### 3계층 주요 프로토콜

- **IPv4** 

  ![IPv4 - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/IPv4_Packet-en.svg/1200px-IPv4_Packet-en.svg.png)

  - 4 Bytes(32 bits)

-  **IPv6**

  <img src="https://lh3.googleusercontent.com/proxy/9xE7Im_nkcYqQbr3SbYDQewQ1q66n0Oba1vQWGUaLIX--nx55gwQlLVZES7EyjeVqSFEorP28XyIK5jJjIAUXaMJ" alt="IPv6 Packet Security | IPv6 Now" style="zoom:150%;" />

  - 16 Bytes(128 bits)



#### 일반적인 IP 주소

|       **클래스**       |     **네트워크 구분**      | **시작 주소** | **마지막 주소** |
| :--------------------: | :------------------------: | :-----------: | :-------------: |
|        A 클래스        | 0XXXXXXX   (첫 번째 필드)  |    0.0.0.0    | 127.255.255.255 |
|        B 클래스        | 10XXXXXX   (두 번째 필드)  |   128.0.0.0   | 191.255.255.255 |
|        C 클래스        |  110XXXXX   (세번째 필드)  |   192.0.0.0   | 223.255.255.255 |
| D 클래스  (멀티캐스트) | 1110XXXX   (네 번째 필드)  |   224.0.0.0   | 239.255.255.255 |
|    E 클래스  (예약)    | 1111XXXX  (다섯 번째 필드) |   240.0.0.0   | 255.255.255.255 |

네트워크 구분에서 앞자리는 상수며, 나머지 뒷자리 부터는(X표시) 1로 채워짐

**EX) A클래스** 

**0** *000 0000.0000 0000.0000 0000.0000 0000* ~ **0** *111 1111.1111 1111.1111 1111.1111 1111*



> 위 방식은 IP낭비가 너무 심한 방식이여서, 지금은 서브넷 마스크를 이용해 낭비를 줄인다.



#### 서브넷 마스크(Subnet Mask)

- 네트워크 대역을 나눠주어 과거방식에서 일어나는 IP 낭비를 방지
- 4 Bytes(32 Bits)
- 2진수로 표기 했을 때 1로 시작, 1과 1사이에는 0이 올수 없음(1까지는 네트워크 대역대, 0은 이 대역대에 속해 있는 호스트의 갯수)



#### 사설IP / 공인IP

> IP주소 자원이 빠르게 소모 되었기 때문에 같은 네트워크 대역에서 사용하는 컴퓨터는 IP공유기에서 하나의 공인IP를 통해 여러개의 사설 IP로 나눠 사용하게 해준다.
>
> EX)아마존 쇼핑물에 찜목록을 상품 목록을 클릭 했을 때 공인 IP로 데이터가 들어오고 사설IP로 구분 되어서 요청(사용중인 기기)한 곳으로 데이터가 들어온다.

- 공인IP : 실제 네트워크에서 사용하는 주소
- 사설IP : 같은 네트워크 대역대에서 사용하는 주소

<img src="C:\Users\Choi\yeoung004.github.io\_posts\Network\image-20210928194145994.png" alt="image-20210928194145994" style="zoom:80%;" />



> NAT장비는 패킷을 요청할 때 기록을 한다, 만약 요청하지 않은 패킷이 들어왔을 경우 NAT까지만 받고 받은 패킷은 전달되지 않는다.

*localhost = 127.0.0.1 : 나 자신의 주소*

*IP주소, 서브넷 마스크, 게이트웨이 주소가 설정 되어있지 않을 경우 네트워크 사용 불가능*



#### 게이트웨이(GateWay)

> 이종 프로토콜간에 통신을 가능하게 하며, 다른 네트워크로 들어가는 문의 역활이다.
>
> 게이트웨이가 설정되지 않았을 경우, 같은 대역대에 있는 컴퓨터끼리(사설IP)는 통신이 가능하지만 (공인IP)에서는 통신이 불가능 하다.



#### ARP

<img src="https://lh3.googleusercontent.com/proxy/AW3ZKdx6Xs2ayuXZ_d4s_5VfCdL6ICR7owB3q6RoyLcvecSr-P3ep4UBhV-oIiW-aAMWHoKN43CakDIVF6o4kmnmkqIK24u4vpd2bHU" alt="The TCP/IP Guide - ARP Message Format" style="zoom:150%;" />

> 같은 네트워크 대역대에서 통신 하기 위한  IP Address를 통해서 MAC Address를 알려주는 프로토콜이다.

- 28 Bytes
- Destonation MAC Address를 모를 경우 전부 0으로 먼저 채운다음 해당 IP를 가진 기기의 MAC Address를 보내달라고 브로드 캐스팅(같은 네트워크 대역대에 연결된 모든 호스트에 전송)

- 같은 네트워크 대역에서만 사용



### 약어

- IPv4 : Internet Protocol Version 4
- IPv6 : Internet Protocol Version 6
- ICMP : Internet Control Message Protocol
- ARP : Address Resolution Protocol