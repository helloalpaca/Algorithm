N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
d = [[[-1]*3 for j in range(N)] for i in range(N)]

def DFS(x, y, direction):
    if x == N-1 and y == N-1:
        return 1
    ans = d[x][y][direction]
    if ans != -1:
        return ans
    ans = 0
    if direction == 0:
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
    d[x][y][direction] = ans
    return ans

print(DFS(0, 1, 0))