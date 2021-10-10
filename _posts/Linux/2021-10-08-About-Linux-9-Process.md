## LINUX



### 프로세스

> 사용자가 사용을 해서 **메모리**에 올라가있는 프로그램을 프로세스라고 한다.

<img src="https://www.tecmint.com/wp-content/uploads/2017/09/Watch-Processes-Nice-Values.png" alt="How to Set Linux Process Priority Using nice and renice Commands" style="zoom: 80%;" />



#### 프로세스 종류

- 부모 프로세스 : 다른 프로세스를 생성할 수 있는 프로세스
- 자식 프로세스 : 부모 프로세스로부터 만들어지는 프로세스,
  - 정상적인 동작은 자식 프로세스를 종료 후 부모 프로세스를 종료

- 데몬 프로세스 : 커널에의해 구동하며, **백그라운드**로 동작하는 서비스
  - 파일 이름 끝에 'd'를 붙여서 사용

- 고아 프로세스 : 부모 프로세스가 자식 프로세스보다 먼저 종료돼버린 프로세스
  - init 프로세스가 이런 프로세스를 관리
    - init, systemd은 서비스를 리눅스를 사용하는데 필요한 서비스들을 실행 및 관리 해주며, 요즘은 systemd프로세스가 관리, PID는 항상 1번
- 좀비 프로세스 : 정상적으로 프로세스를 종료했지만, 자원을 반납하지 않은 상태로 계속 남아있는 상태



#### 프로세스 관련 명령어

- ps : 현재 사용자가 사용중인 프로세스를 보여줌
  - ef : 내용을 더 자세히 알려줌
- pstree : 프로세스 트리를 보여줌
- pgrep : 한 번에 pid만 보여줌
- top : 프로세스 목록 + cpu 사용률을 같이 보여줌
  - q로 종료



#### 프로세스 제어 명령어

- 시그널 번호
  - 1 : 프로세스 종료 없이 프로그램 새로 초기화
  - 2 : Ctrl + C명령어 실행 중 중단
  - **9 : 강제 종료**
  - 15 : 종료하되 강제x

- kill : 프로세서에게 시그널 번호를 전송해서 프로세스를 종료시키는 명령어
  - pid로 프로세스를 제어
- pkill :  프로세서에게 시그널 번호를 전송해서 프로세스를 종료시키는 명령어
  - 프로세스 이름으로 제어
