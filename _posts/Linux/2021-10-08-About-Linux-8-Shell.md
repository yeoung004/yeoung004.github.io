## LINUX



### Shell

> 터미널에서 입력한 명령을 해석하고 관리하는 프로그램을 쉘(Shell)이라고 한다.
>
> 쉘은 사용자, 커널 사이의 연결 역활을 담당하며, 사용자가 입력한 명령어를 해석하여 Linux가 명령어를 이해하도록 변역해준다.
>
> 여러개의 쉘 중에 Bash쉘을 가장 많이 사용한다.



#### 인용 메타문자

- \`\` :  \`\`안에 있는 문자를 명령어로 인식하여 실행
- ' ' : ' ' 안에 있는 메타 문자를 일반 문자로 취급
- " " : " " 안에 있는 $,\,` 특수 문자들을 제외한 나머지 문자만 일반 문자로 취급

*($는 쉘에서* 변수사용 할 때 사용)*



#### 방향 메타 문자

- < : 표준 입력 재지정

- \> : 표준 출력, 에러 출력을 파일로 저장, 네트워크로 전송

  - echo test > ./file : echo 명령어로 화면에 다시 출력시키고 텍스트를 현재 디렉토리의 file 이라는 곳에 텍스트를 저장(이어쓰기)
  - echo test >> ./file : >>는 기존 내용을 새로운 내용으로 덮어 씌우기
  - find / -perm -4000 2> /dev/null : 정상적인 결과만 출력
  - find / -perm -4000 1> /dev/null : 에러결과만 출력

  *(/dev/null는 리눅스에서 복원할 수 없는 휴지통)*

- | : 파이프 문자, [명령어1] | [명령어2]
  - ls /etc | grep rc : ls 명령어의 결과중에서 특정 문자를 포함한 라인만 뽑아 볼 때



### 사용자 초기화 파일

> 사용자 별로 적용되는 범위가 다른 설정 파일이 존재한다.
>
> 아래의 설정 파일에서는 환경 변수, 쉘 프롬프트 모양, 별명(Alias), 쉘옵션 정의등을 설정 가능하다.

- /etc/profile : 시스템 전역에 걸쳐 환경을 설정하는 파일, 모든 사용자에게 적용됨
- ~/.profile : 개별 사용자의 홈 디렉토리에 있는 파일, 해당 사용자의 설정을 변결 할 때
- ~/.bashrc : 개별 사용자의 홈 디렉토리에 있는 파일, 해당 사용자의 쉘 관련 설정을 변경 할 때



#### 환경변수

> 시스템 환경에 대한 정보를 가지고 있는 변수이다.

- HOME : 사용자의 홈 디렉토리
- **PATH** : 실행파일을 찾는 경로
- LANG : 프로그램 사용시 기본 지원되는 언어
- SHELL : 로그인해서 사용하는 쉘
- EDITOR : 기본 편집기의 이름
- **PS1** : 명령프롬프트 변수

