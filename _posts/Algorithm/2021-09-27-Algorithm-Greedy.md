# 알고리즘



### 그리디(탐욕법) 알고리즘

> 현재 상황에서 당장 좋은 것만 고르는 방법

### <동전 거슬러주는 프로그램>

#### Input(거슬러 줘야하는 금액), Out(총 동전의 갯수)

```
n = 1260
coins = [500, 100, 50, 10]
count = 0

for coin in coins:
    print(str(int(coin)) + "원: " + str(int(n / coin)) + "개")
    count+=int(n / coin)
    n %= coin
print(count)
500원: 2개
100원: 2개
50원: 1개
10원: 1개
6
```

화폐의 종류 만큼 반복문을 수행하기 때문에 시간 복잡도는 O(K)이다

### <1이 될 때까지>

#### 어떠한 수 N이 1이 될 때까지 다른의 두 과정 중 하나를 반복적으로 수행하려함

#### 1. N에서 1을 뺌

#### 2. N을 K로 나눔

#### 2번 쨰 연산을 사용할 경우는 0으로 나누어 떨어질때만 사용 가능

#### In(N: 어떠한 수, K: 나눠야할 수) Out(M: 과정을 수행한 최솟값)

```
n,k = map(int, input().split())

count = 0

while n > 1:
    if(n % k == 0):
        n //= k
    else:
        n -= 1
    count += 1
    
print(count)
 25 5
2
```

반복문 초반, n을 먼저 나누기 때문에 시간 복잡도는 log가 된다.

