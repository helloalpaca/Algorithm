from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(board, m, n, start, goal):
    v = [[0] * n for _ in range(m)]
    q = deque([start])
    v[start[0]][start[1]] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and v[nx][ny] == 0 and board[nx][ny] != 'X':
                if nx == goal[0] and ny == goal[1]:
                    return v[x][y]
                v[nx][ny] = v[x][y]+1
                q.append((nx, ny))
    return -1


def solution(maps):
    board = []
    m = len(maps)  # x
    n = len(maps[0])  # y
    x, y = 0, 0  # 시작
    lx, ly = 0, 0  # 레버
    ex, ey = 0, 0  # 출구

    for i in range(m):
        li = list(maps[i])
        for j in range(n):
            if li[j] == 'S':
                x, y = i, j
            elif li[j] == 'L':
                lx, ly = i, j
            elif li[j] == 'E':
                ex, ey = i, j
        board.append(li)

    s_to_l = dfs(board, m, n, (x, y), (lx, ly))
    l_to_e = dfs(board, m, n, (lx, ly), (ex, ey))

    if s_to_l == -1 or l_to_e == -1:
        return -1

    return s_to_l+l_to_e


# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"]))