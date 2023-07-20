# 다 입력 받아서 BFS 돌리면 메모리 초과 에러가 난다.
# 그때그때 점화식 + 슬라이딩 윈도우로 풀어야 함.
# 한 줄에 무조건 세개씩만 들어온다는 조건을 처음에 인지하지 못함 <- 문제 잘 읽자!!

import sys
read = sys.stdin.readline

N = int(input())
arr = list(map(int, read().split()))
min_arr = arr
max_arr = arr
for _ in range(N-1):
    arr = list(map(int, read().split()))
    max_arr = [arr[0]+max(max_arr[0], max_arr[1]), arr[1]+max(max_arr), arr[2]+max(max_arr[1], max_arr[2])]
    min_arr = [arr[0]+min(min_arr[0], min_arr[1]), arr[1]+min(min_arr), arr[2]+min(min_arr[1], min_arr[2])]

print(max(max_arr), min(min_arr))

"""
from collections import deque
import sys
read = sys.stdin.readline

dx = [1, 1, 1]
dy = [-1, 0, 1]
def BFS(x, y, cnt):
    q = deque([(x, y, cnt)])
    max_count = 0
    min_count = int(1e9)
    while q:
        x, y, cnt = q.popleft()
        for k in range(3):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                q.append((nx, ny, cnt+board[nx][ny]))
                # print("BFS: ",nx, ny, cnt+board[nx][ny])
                if nx == N-1:
                    if cnt+board[nx][ny] > max_count:
                        max_count = cnt+board[nx][ny]
                    if cnt+board[nx][ny] < min_count:
                        min_count = cnt+board[nx][ny]
    return max_count, min_count

N = int(input())
board = [[0]*N for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, read().split()))

min_answer = int(1e9)
max_answer = 0
for i in range(N):
    max_cnt, min_cnt = BFS(0, i, board[0][i])
    min_answer = min(min_cnt, min_answer)
    max_answer = max(max_cnt, max_answer)
print(max_answer, min_answer)
"""