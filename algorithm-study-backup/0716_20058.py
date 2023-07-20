"""
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1
"""

# 1. 배열을 시계 방향으로 90도 회전
# 2. 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
import sys
from copy import deepcopy
from collections import deque

read = sys.stdin.readline
N, Q = map(int, read().rstrip().split())
ll = 2**N
board = [list(map(int, read().rstrip().split())) for _ in range(ll)]
arrL = list(map(int, read().rstrip().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotateL(L):
    LL = 2**L
    num = ll//LL
    for i in range(num):
        for j in range(num):
            sub_board = []
            for k in range(LL):
                sub_board.append(board[i*LL+k][j*LL:j*LL+LL])
            sub_board = rotate(sub_board)
            for k in range(LL):
                board[i*LL+k][j*LL:j*LL+LL] = sub_board[k]

def rotate(arr):
    arr_next = deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            x = j
            y = (len(arr)-1-i + len(arr)) % len(arr)
            arr_next[x][y] = arr[i][j]
    return arr_next
    # for bo in board:
    #     print(bo)

def calc_ice():
    global board
    board_next = deepcopy(board)
    for i in range(ll):
        for j in range(ll):
            cnt = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<ll and 0<=ny<ll:
                    if board[nx][ny] > 0:
                        cnt += 1
            if cnt < 3: #인접한 칸 중 3개 이상 얼음이 있지 않으면, 해당 칸의 얼음이 1 줄어든다.
                if board[i][j]>0:
                    board_next[i][j] -= 1
    board = board_next

def bfs(x, y):
    q = deque([(x, y)])
    v = [[False]*ll for _ in range(ll)]
    v[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<ll and 0<=ny<ll and not v[nx][ny] and board[nx][ny]>0:
                q.append((nx, ny))
                v[nx][ny] = True
                cnt += 1
    return cnt, v

for L in arrL:
    # print("L:",L)
    rotateL(L)
    calc_ice()
    # for bo in board:
    #     print(bo)

answer = 0
for bo in board:
    # print(bo)
    answer += sum(bo)
print(answer)

biggest = 0
visited = [[False]*ll for _ in range(ll)]
for i in range(ll):
    for j in range(ll):
        if board[i][j] > 0:
            cnt, v = bfs(i, j)
            for m in range(ll):
                for n in range(ll):
                    if v[m][n]:
                        visited[i][j]=True
            if cnt > biggest:
                biggest = cnt
print(biggest)
