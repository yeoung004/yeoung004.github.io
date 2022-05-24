# 소수 구하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	148792	41749	29456	26.782%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
M, N = map(int, input().split())
for i in range(M, N+1):
    if i in [2, 3, 5, 7] :
            print(i)
    elif i % 2:
        isPrime = True
        for j in range(3, int(i ** 0.5) + 2, 2):
            if i % j == 0:
                isPrime = False
                break
        if isPrime and i != 1:
            print(i)