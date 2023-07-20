# 물고기 -> 위치, 크기
# 상어 -> 위치, 크기, 지금까지 먹은 물고기의 개수
# 공간 -> 물고기, 상어
# 1. 상어가 먹을 수 있는 물고기를 찾는다. (BFS)
# 2. 이동해서 먹는다.

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(board, x, y, size):
    n = len(board)
    d = [[-1]*N for _ in range(n)]
    d[x][y] = 0
    q = deque([(x, y)])
    ans = []
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                ok = False
                eat = False
                if board[nx][ny] == 0:
                    ok = True
                elif board[nx][ny] < size:
                    ok = True
                    eat = True
                elif board[nx][ny] == size:
                    ok = True
                if ok:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y]+1
                    if eat:
                        ans.append((d[nx][ny], nx, ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]


answer = 0
babyshark = 2
exp = 0
bx, by = 0, 0

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            bx, by = i, j
            board[i][j] = 0

while True:
    fishes = BFS(board, bx, by, babyshark)
    if fishes is None:
        break
    dist, x, y = fishes
    board[x][y] = 0
    bx, by = x, y
    answer += dist
    exp += 1
    if exp == babyshark:
        babyshark += 1
        exp = 0
print(answer)
