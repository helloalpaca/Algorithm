n=3
v = [[0]*n for _ in range(n)]
x, y = 0, 0
cnt = 2
v[x][y] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
length = n

for _ in range(n*n-1):
    nx, ny = x+dx[d], y+dy[d]
    if nx<0 or nx>=n or ny<0 or ny>=n or v[nx][ny] !=0:
        d += 1
        d %= 4
    nx, ny = x+dx[d], y+dy[d]

    print(nx, ny)
    v[nx][ny] = cnt
    cnt+=1
    x = nx
    y = ny

    for va in v:
        print(va)