# 달팽이와 비슷한 방식으로 칸의 위치를 구할 수 있다.
# = 회전해서 이동한 칸이 이미 처리한 칸이면, 회전을 처리하지 않는 방식으로.
# 방향 순서는 왼, 아래, 오른, 위

from collections import deque
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dd = []
arr = []
answer = 0

def rotate(wind):
    ans = []
    for w in wind:
        nx = -w[1]
        ny = w[0]
        ans.append((nx, ny, w[2]))
    return ans

def make_dd():
    wind = []
    wind.append((0, -2, 5))
    wind.append((-1,-1,10))
    wind.append((1,-1,10))
    wind.append((-1,0,7))
    wind.append((-2,0,2))
    wind.append((1,0,7))
    wind.append((2,0,2))
    wind.append((-1,1,1))
    wind.append((1,1,1))
    dd.append(wind)

    for i in range(3):
        wind = rotate(wind)
        dd.append(wind)

# def get_board_arr(N):
#     x, y = N//2, N//2
#     d = 0
#     #arr.append((x, y, d))
#     v = [[False]*N for _ in range(N)]
#     v[x][y] = True
#     for _ in range(N*N - 1):
#         nx, ny = x+dx[d], y+dy[d]
#         if v[nx][ny]:
#             d -= 1
#             nx, ny = x+dx[d], y+dy[d]
#         v[nx][ny] = True
#         # d = (d + 1) % 4
#         arr.append((nx, ny, d))
#         d = (d+1)%4
#         x, y = nx, ny
#
# def sand(board, x, y, d):
#     global answer
#     used = 0
#     for i in range(9):
#         nx = x + dd[d][i][0]
#         ny = y + dd[d][i][1]
#         cur = (board[x][y]*dd[d][i][2])//100
#         used += cur
#         if 0<=nx<N and 0<=ny<N:
#             # print(nx, ny, dd[d][i][2],board[x][y],  board[x][y]*dd[d][i][2]//100)
#             board[nx][ny] += cur
#         else:
#             answer += cur
#         # print(board)
#     board[x][y] -= used
#     print(x, y, d, answer)
#     for bo in board:
#         print(bo)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
v = [[False]*N for _ in range(N)]
make_dd()
# get_board_arr(N)
# # print(arr)
#
# for ar in arr:
#     x, y, d = ar[0], ar[1], ar[2]
#     sand(board, x, y, d)



def go(a, nx, ny, cur):
    n = len(a)
    if 0 <= nx < n and 0 <= ny < n:
        a[nx][ny] += cur
    else:
        return cur
    return 0

x, y = (N-1)//2, (N-1)//2
d = 0
v[x][y] = True
cnt = 2
ans = 0

while True:
    print(x, y, d)
    for bo in board:
        print(bo)
    nx = x+dx[d]
    ny = y+dy[d]
    cnt += 1
    v[nx][ny] = True
    # (x, y) -> (nx, ny)
    sand = board[nx][ny]
    used = 0
    board[nx][ny] = 0
    x = nx
    y = ny

    for t in dd[d]:
        nx = x+t[0]
        ny = y+t[1]
        cur = sand * t[2] // 100
        used += cur
        ans += go(board, nx, ny, cur)
    print(used, ans)

    sand -= used
    nx = x+dx[d]
    ny = y+dy[d]
    ans += go(board, nx, ny, sand)
    if x == 0 and y == 0:
        break

    # next
    nd = (d+1) % 4
    nx = x+dx[nd]
    ny = y+dy[nd]
    if v[nx][ny] == False:
        d = nd

print(ans)
