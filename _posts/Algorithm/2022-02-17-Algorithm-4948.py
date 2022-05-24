# 베르트랑 공준 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	57769	23046	18747	40.220%
# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

################################# 차집합 방법

# prime = {2, 3, 5, 7}
# for i in range(11, 123456 * 2 + 1):
#     if i % 2:
#         isPrime = True
#         for j in range(3, int(i ** 0.5) + 2, 2):
#             if i % j == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             prime.add(i)

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     result = {i for i in range(n+1, n*2+1)}
#     result = prime - result
#     print(len(prime) - len(result))

################################# true false 비교 방법

# n = 123456 * 2 + 1

# prime = [False] * n
# for i in [2, 3, 5, 7]:
#     prime[i] = True
# for i in range(11, n, 2):
#     isPrime = True
#     for j in range(3, int(i ** 0.5) + 1, 2):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime:prime[i] = True

# while True:
#     n = int(input())
#     if n == 0:break
#     elif n == 1:print(1)
#     else:
#         cnt=0
#         result = [i for i in range(n+1, n*2+1, (n+1)%2+1)]
#         for i in result:
#             if prime[i]:cnt+=1
#         print(cnt)

################################# true false 비교 방법 2
# N = 246913
# prime = [True] * N

# for i in range(3, int(N**0.5)+1, 2):
#     for j in range(i*3, N, i*2):
#       prime[j] = False

# while True:
#     n = int(input())
#     if n == 0:break
#     elif n == 1:print(1)
#     else:
#         cnt = 0
#         for i in range(n+(n%2)+1, n*2+1, 2):
#             if prime[i]:cnt+=1
#         print(cnt)
  
################################# true false 비교 방법 3
N = 246913
prime = [True] * N
for i in [3, 5, 7]:
    for j in range(i*3, N, i*2):
      prime[j] = False
for i in range(11, int(N**0.5)+1, 2):
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        for j in range(i*3, N, i*2):
            prime[j] = False
        

while True:
    n = int(input())
    if n == 0:break
    elif n == 1:print(1)
    else:
        cnt = 0
        for i in range(n+(n%2)+1, n*2+1, 2):
            if prime[i]:cnt+=1
        print(cnt)  