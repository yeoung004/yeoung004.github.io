# 네트워크



### IPv4 Protocol

> 네트워크 상에서 데이터를 교환하기 위한 프로토콜이지만, 
>
> 데이터가 정확하게 전달될것을 보장해주지 않는다.
>
> 위의 문제점은 이보다 더 상위 프로토콜인 TCP에서 보장한다.



![image-20210930232650336](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/2021-09-30-About-Network4-IPv4.assets/image-20210930232650336.png?raw=true)

- Source IP, Destination IP 각각 4 Bytes씩 총 8바이트를 사용
- IP Flags : 3 bits이며 D는 Don't fragmentation, M은 More fragementation이다 데이터를 허용 범위 내에서 보내면 아무런 오류가 없지만, 범위를 초과 했을 경우 M option을 이용해 Fragment Offset에다가 잘게 쪼갠 데이터의 위치를 알려줌
- TTL : 최적의 경로를 찾아주는 3계층에서는 패킷의 전송 성공 유무를 확신시켜 주지 않음 그래서 TTL을 이용해 잘못된 경로로 간 패킷이 무한적으로 발생하는 것을 방지하기 위해 일정 경로를 지날경우 자동으로 삭제됨
  - 하나의 라우터를 지날 경우 1씩 감소되며, OS마다 숫자 값이 다름
    - Window :128
    - Linux : 64



### ICMP

> 운영체제에서 오류 메세지를 전송하는데 주로 쓰이며, 
>
> 주로 상대방과 통신 사용 가능 유무를 확인할때 사용한다.

![image-20210930234803117](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Network/image-20210930234803117.png?raw=true)

#### ICMP message types

![image](https://mk0resourcesinf5fwsf.kinstacdn.com/wp-content/uploads/1-319.png)

- Type : 대문류 (0 ~ 30까지 여러가지 코드와 이름이 존재)
  - 0,8 : 기본적인것
    - 8(Echo Request) : 통신 요청
    - 0(Echo Reply) : 요청에 대한 응답
  - 3, 11 : 오류 발생
    - 3(Destination Unreachable) : 목적지까지 도착 X -> 경로상에 문제(주로 라우터 문제)
    - 11(Time Exceeded ) : 도착은 했지만, 응답을 못받음 -> 상대방에 문제가 발생(주로 방화벽)
  - 5 : 보안상 문제
    - 5(Redirect Message) : 라우팅 테이블을 임의적으로 수정할 경우
- Code : 소분류









### 약어

- **ICMP** : Internet Control Message Protocol