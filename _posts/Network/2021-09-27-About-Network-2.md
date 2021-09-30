# 네트워크



### OSI 7 Layers

> 데이터를 주고 받을 때 데이터 자체의 흐름을 각 구간별로 나눠 놓은 것이다.

![image-20210927213741200.png](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20210927213741200.png?raw=true)



### TCP/IP

> 컴퓨터 끼리 정보를 주고 받을 때 사용하는 통신 규약이다.

![image-20210927214948839.png](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20210927214948839.png?raw=true)

### 패킷(Packet)

> 네트워크상에서 전달되는 데이터를 통칭하는 말, 데이터의 형식화된 블록(Block)이다.
>
> 패킷은 제어 정보 + 사용자 데이터로 이루어지며, 사용자 데이터는 페이로드(Payload)라고 한다.



#### 캡슐화(Encapsulation)

- 프로토콜을 이용해서 데이터를 보낼 때 패킷을 만드는 과정이다.
- 이 과정중에는 첫 번째것이 마지막이 될 수 없고, 마지막이 첫번째가 될수 없다.

*(역캡슐화(Decapsulation)는 수신할 때는 역순)*



![image-20210927222002231.png](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20210927222002231.png?raw=true)



### 2 계층

- LAN에서 통신할 때 주소체계는 MAC 이다. EX)D5-5E-45-12-05-EB-A1
- 16진수를 사용하며, 12개로 이루어져 있다.
- OUI(6 Bytes) : IEEE가 부여한 제조회사 식별 ID + 고유번호(6 Bytes) : 제조사에서 부여한 고유 번호

https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/996700395E199B6B0E.png?raw=true

- Destination Address(6 bytes) + Source Address(6 Bytes) + Ethernet Type(2 bytes) = 14 bytes
- Ethernet (Protocal) Type : Payload(상위 프로토콜)에 어떤 프로토콜이 들어가  있는지 알려주기 위함 





### 약어

- **OSI**(Open Systems Interconnection)

- **TCP/IP**(Transmission Control Protocol/Internet Protocol)

- **MAC**(A Media Access Control)
- **캡슐화**(Encapsulation)

- **OUI**(Organizationally Unique Identifier)
- **IEEE**(Institute of Electrical and Electronics Engineers)