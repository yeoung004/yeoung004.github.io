# 직사각형에서 탈출
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	52623	31739	28118	60.461%
# 문제
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 x, y, w, h가 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.
geo=list(map(int,input().split()))
for i in range(2,4):geo[i]-=geo[i-2]
print(min(geo))
