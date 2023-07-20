N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

# 0: 오른쪽, 1: 오른대각아래, 2:아래
# 0일때는 0, 1만 가능, 1일때는 0, 1, 2가능, 2일때는 1, 2만 가능
def DFS(x, y, direction):
    if x == N-1 and y == N-1:
        return 1
    ans = 0

    if direction == 0: # 오른쪽
        if y+1 < N and board[x][y+1] == 0:
            ans += DFS(x, y+1, 0)
        if x+1 < N and y+1 < N and board[x][y+1] == 0 and board[x+1][y] == 0 and board[x+1][y+1] == 0:
            ans += DFS(x+1, y+1, 1)

    elif direction == 1:
        if y+1 < N and board[x][y+1] == 0:
            ans += DFS(x, y+1, 0)
        if x+1 < N and board[x+1][y] == 0:
            ans += DFS(x+1, y, 2)
        if x+1 < N and y+1 < N and board[x][y+1] == 0 and board[x+1][y] == 0 and board[x+1][y+1] == 0:
            ans += DFS(x+1, y+1, 1)

    elif direction == 2:
        if x+1 < N and board[x+1][y] == 0:
            ans += DFS(x+1, y, 2)
        if x+1 < N and y+1 < N and board[x][y+1] == 0 and board[x+1][y] == 0 and board[x+1][y+1] == 0:
            ans += DFS(x+1, y+1, 1)

    return ans

print(DFS(0, 1, 0))