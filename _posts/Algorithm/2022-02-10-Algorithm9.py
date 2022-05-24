T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    num = [i for i in range(1, n + 1)]
    for _ in range(k):
        for i in range(1, n):
            num[i] += num[i - 1]
    print(num[-1])