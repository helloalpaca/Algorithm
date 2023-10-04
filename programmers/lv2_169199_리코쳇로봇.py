from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxInt = int(1e9)


def solution(board):
    answer = 0
    m = len(board)
    n = len(board[0])
    v = [[maxInt] * n for _ in range(m)]

    q = deque()
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                v[i][j] = 0

    while q:
        # print(q)
        x, y, dist = q.popleft()

        if board[x][y] == 'G':
            return dist

        for i in range(4):
            nx, ny = x, y
            while 0 <= nx+dx[i] < m and 0 <= ny+dy[i] < n and board[nx+dx[i]][ny+dy[i]] != 'D':
                # print(nx, ny, board[nx][ny])
                nx += dx[i]
                ny += dy[i]

            if 0 <= nx < m and 0 <= ny < n and v[nx][ny] > dist + 1:
                # print(nx, ny)
                v[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))

    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))