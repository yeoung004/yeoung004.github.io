# 소수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	75559	29042	24846	38.814%
# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

M = int(input())
N = int(input())
result = 0
least = 0

for i in range(M, N + 1):
    if i < 10:
        if i in [2, 3, 5, 7] :
            result.append(i)
    elif i % 2 != 0:
        maxPrimeSeek = int(i ** 0.5) + 1
        isPrime = True
        for j in range(3, maxPrimeSeek + 1, 2):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)
            
if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)