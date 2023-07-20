"""
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
"""
import sys
from collections import deque

N = int(input())
sx, sy = 0, 0
size = 2
num_eat = 0
board = [[] for _ in range(N)]
fishes = []
answer = 0

for i in range(N):
    inputs = list(map(int, sys.stdin.readline().split()))
    board[i] = inputs
    for j in range(N):
        if inputs[j] == 9:
            sx, sy = i, j
        if inputs[j] == 1:
            fishes.append([0, i, j])

if not fishes:
    print(0)

else:
    while fishes:
        fishes = list(fishes)
        for fish in fishes:
            fish[0] = abs(sx - fish[1]) + abs(sy - fish[2])
        fishes.sort(key=lambda x: (x[0], x[1], x[2])) # 우선순위에 따라 sort
        fishes = deque(fishes)
        dist, x, y = fishes.popleft() # 물고기 위치 하나 꺼내기
        print(dist, x, y)
        board[x][y] = 0
        answer += dist
        sx, sy = x, y #상어 위치 변경
        num_eat += 1
        if num_eat == size:
            size += 1
            num_eat = 0
            for i in range(N):
                for j in range(N):
                    if board[i][j] < size:
                        fishes.append([abs(sx-i)+abs(sy-j), i,j])

    print(answer)