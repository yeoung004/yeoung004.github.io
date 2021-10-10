## LINUX



### 아카이브

> 여러 파일을 하나의 묶음으로 보관할때 사용한다. (압축 파일명.tar.gz)



#### 아카이브 관련 명령어

- tar [기능] [아카이브 파일] [묶을 파일1] [묶을 파일2] [묶을 파일3] ...

  - c : 새로운 아카이브 파일을 생성
  - x : 아카이브 파일에서 여러 파일을 해제
  - t : 아카이브 파일에서 안의 내용을 조회
  - v : verbose, 명령어 수행과정을 자세히 출력
  - f : 아카이브 장치 지정
  - z : 압축해제

  - tar cvf test.tar exam simulation training : 아카이브 생성
  - tar xvf : 아카이브 해제
    - tar zxvf : .zip압축 해제 후 아카이브 해제
    - tar jxvf : bzip2압축 해제 후 아카이브 해제



#### 압축 관련 명령어

- zip [압축할 파일 이름] [압축할 파일 이름] : 압축(windows호환) .zip
  - unzip [압축 파일 이름] : 압축 해제
- gzip [압축할 파일 이름] : 가장 빠르고 사용을 많이 함, 아카이브로 파일을 모은 다음 이 명령어를 실행 .gz
  - gunzip[압축 파일 이름] : 압축 해제
- bzip2 [압축할 파일 이름] [압축할 파일 이름] :  .bz2
  - bunzip2 [압축 파일 이름] : 압축 해제
