# 소인수분해
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	49519	26551	20741	52.382%
# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

N = int(input())
result = []

while N > 1:
    root = int(N ** 0.5) + 1
    if N % 2 == 0:
        N //= 2
        print(2)
    else:
        j = 3
        while N % j != 0 and j <= root:
            j+=2
        if j >= root:
            result.append(N)
            N = 1
        else:
            N //= j
            result.append(j)
for i in sorted(result):
    print(i)