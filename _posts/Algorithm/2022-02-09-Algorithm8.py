# 2022.02.09 알고리즘
### 10757	큰 수 A+B
# print(sum(list(map(int,input().split()))))

### 1011	Fly me to the Alpha Centauri
T = int(input())

for _ in range(T):
    switch = False
    base = 2
    cnt = 2
    x,y = map(int, input().split())
    case = y - x
    plus = 2
    
    if case <= 1:
        print(case)
    else:
        while base < case:
            base += plus
            cnt += 1
            if switch:
                plus += 1
            switch = not switch
        print(cnt)