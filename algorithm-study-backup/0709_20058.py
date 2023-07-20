from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def rotate(a):
    n = len(a)
    ans = [[a[n - j - 1][i] for j in range(n)] for i in range(n)]
    return ans


def firestorm(a, sx, sy, size):
    b = [[a[sx + i][sy + j] for j in range(size)] for i in range(size)]
    b = rotate(b)
    for i in range(size):
        for j in range(size):
            a[sx + i][sy + j] = b[i][j]


n, q = map(int, input().split())
m = (1 << n)
a = [list(map(int, input().split())) for _ in range(m)]
for l in map(int, input().split()):
    if l > 0:
        size = (1 << l)
        for sx in range(0, m, size):
            for sy in range(0, m, size):
                firestorm(a, sx, sy, size)

    b = [row[:] for row in a]
    for i in range(m):
        for j in range(m):
            if a[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < m and 0 <= ny < m:
                    if b[nx][ny] > 0:
                        cnt += 1
            if cnt >= 3:
                pass
            else:
                if a[i][j] > 0:
                    a[i][j] -= 1

ans = sum(sum(row) for row in a)
print(ans)

# BFS로 가장 큰 덩어리가 차지하는 개수 구하기
check = [[False] * m for _ in range(m)]
ans = 0
for i in range(m):
    for j in range(m):
        if a[i][j] == 0:
            continue
        if check[i][j] == True:
            continue
        q = deque()
        q.append((i, j))
        cnt = 1
        check[i][j] = True
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < m and 0 <= ny < m:
                    if a[nx][ny] != 0 and check[nx][ny] == False:
                        check[nx][ny] = True
                        q.append((nx, ny))
                        cnt += 1
        if ans < cnt:
            ans = cnt
print(ans)