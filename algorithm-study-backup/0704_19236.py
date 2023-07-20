# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# 모든 물고기 방향 변경하기
# 상어가 잡아 먹기
from copy import deepcopy

N = 4
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def start(num, direction, x, y, d):
    for who in range(1, N*N+1):
        f = False
        for i in range(N):
            for j in range(N):
                if num[i][j] == who:
                    for k in range(8):
                        nx = i+dx[direction[i][j]]
                        ny = j+dy[direction[i][j]]
                        if 0 <= nx < N and 0 <= ny < N and num[nx][ny] >= 0 and (not (nx == x and ny == y)):
                            num[i][j], num[nx][ny] = num[nx][ny], num[i][j]
                            direction[i][j], direction[nx][ny] = direction[nx][ny], direction[i][j]
                            f = True
                            break
                        else:
                            direction[i][j] += 1
                            direction[i][j] %= 8
                if f:
                    break
            if f:
                break
    ans = 0
    sx = x+dx[d]
    sy = y+dy[d]
    while 0 <= sx < N and 0 <= sy < N:
        if num[sx][sy] != 0:
            temp = num[sx][sy]
            num[sx][sy] = 0
            cur = temp + start(deepcopy(num), deepcopy(direction), sx, sy, direction[sx][sy])
            if ans < cur:
                ans = cur
            num[sx][sy] = temp
        sx += dx[d]
        sy += dy[d]

    return ans


board = [[0]*N for _ in range(N)]
direction = [[0]*N for _ in range(N)]

for i in range(N):
    inp = list(map(int, input().split()))
    for j in range(N):
        board[i][j] = inp[2 * j]
        direction[i][j] = inp[2 * j + 1]
        direction[i][j] -= 1

answer = board[0][0]
board[0][0] = 0
answer += start(board, direction, 0, 0, direction[0][0])
print(answer)