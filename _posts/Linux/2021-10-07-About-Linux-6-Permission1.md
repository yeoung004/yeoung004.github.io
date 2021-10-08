## LINUX



### 권한

> 리눅스 OS에서는 모든 파일, 디렉토리가 접근권한을 가지고 있다.
>
> ls -l 명령어로 확인이 가능하며, -rwxrwxrwx 이런식으로 표기 된다.(r:읽기, w:쓰기, x:실행, -:권한x)
>
> -/rwx/rwx/rwx : 종류(파일, 디렉토리)/소유자/관리자/나머지

*(파일을 실행하기 위해서는 최소한 읽기 권한이 있어야만 실행이 가능함)*



- chmod [권한] [파일 또는 디렉토리 이름] : 권한 설정

- [권한] : 옥텟(8진수), 심볼릭 모드

  



#### 심볼릭 모드

![Linux Part 5. 리눅스의 권한 (특수 권한) : 네이버 블로그](https://mblogthumb-phinf.pstatic.net/MjAyMDAxMTVfMTIx/MDAxNTc5MDQ5MjgxNDEy.BxtkqSbHMdaKnYaBSUl86vR18HPIr_6a3ym72VUvd3Mg.4AMs47VpmeJWHNuTK6HoHdnL72h9WrIlzihvA3YMQpQg.PNG.hyun0524e/%EA%B6%8C%ED%95%9C_%EC%84%A4%EC%A0%95%EC%9D%98_%EC%8B%AC%EB%B3%BC%EB%A6%AD_%EB%AA%A8%EB%93%9C.PNG?type=w800)



#### 옥텟모드

![Linux Part 4. 리눅스의 권한 (특수 권한)](https://t1.daumcdn.net/cfile/tistory/99C662335EB173002F)

#### umask

> 리눅스에서 파일, 디렉토리를 생성할 때 and연산을 해서 기본 권한으로 설정해주는 값이다.
>
> (022 & 777)
>
> (022 & 666)

- 파일 기본 권한
  - 644 / rw-r--r--
- 디렉토리 기본 권한
  - 755 / rwxr-xr-x

![image-20211007185744299](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Linux/image-20211007185744299.png?raw=true)

