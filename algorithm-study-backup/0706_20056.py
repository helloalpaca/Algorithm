"""
N(board크기), M(파이어볼 개수), K(이동 횟수)
r, c, m, s, d
(r, c): 위치, m: 질량, s:속력, d:방향
4 2 1
1 1 5 2 2
1 4 7 1 6
"""
"""
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
#initialize
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
board_next = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])

# K번 이동하는 동안
for _ in range(K):
    for i in range(N):
        for j in range(N):
            board_next[i][j] = []
    for i in range(N):
        for j in range(N):
            for k in range(len(board[i][j])):
                m, s, d = board[i][j][k][0], board[i][j][k][1], board[i][j][k][2]
                nx = i+dx[d]*s
                ny = j+dy[d]*s
                if nx >= N: nx %= N
                if ny >= N: ny %= N
                if nx < 0: nx += N
                if ny < 0: ny += N
                board_next[nx][ny].append(board[i][j][k])
    for i in range(N):
        for j in range(N):
            if len(board_next[i][j])>1:
                board[i][j] = []
                m, s, isOdd, isEven = 0, 0, False, False
                nd = []
                for k in range(len(board_next[i][j])):
                    m += board_next[i][j][k][0]
                    s += board_next[i][j][k][1]
                    d = board_next[i][j][k][2]
                    if d%2==0: isEven = True
                    else: isOdd = True
                if (not isEven and isOdd) or (not isOdd and isEven):
                    nd=[0, 2, 4, 6]
                else:
                    nd=[1, 3, 5, 7]
                m //= 5
                s //= len(board_next[i][j])
                if m > 0:
                    for k in range(4):
                        board[i][j].append([m, s, nd[k]])
            else:
                board[i][j] = board_next[i][j]
    # print("=================K: "+str(K)+"==================")
    # for bo in board:
    #     print(bo)
    # print("===========================================")

answer = 0
# for bo in board:
#     print(bo)
for i in range(N):
    for j in range(N):
        for k in range(len(board[i][j])):
            answer += board[i][j][k][0]
print(answer)
"""

class Shark:
    def __init__(self, m, s, d):
        self.m = m
        self.s = s
        self.d = d
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
board = [[[] for j in range(N)] for i in range(N)]
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c].append(Shark(m,s,d))

for _ in range(K):
    board_next = [[[] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for shark in board[i][j]:
                nx = i+dx[shark.d]*shark.s
                ny = j+dy[shark.d]*shark.s
                nx = (nx % N + N) % N
                ny = (ny % N + N) % N
                board_next[nx][ny].append(shark)
    board = board_next
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                total_m = 0
                total_s = 0
                cnt = len(board[i][j])
                compare_d = board[i][j][0].d % 2
                result_d = 0
                for shark in board[i][j]:
                    if shark.d % 2 != compare_d:
                        result_d = 1
                    total_m += shark.m
                    total_s += shark.s
                board[i][j].clear()
                shark_m = total_m // 5
                shark_s = total_s // cnt
                if shark_m > 0:
                    for direction in range(4):
                        board[i][j].append(Shark(shark_m, shark_s, direction*2+result_d))

# for b in a:
#     for j in range(len(b)):
#         if b[j] != []:
#             print(b[j][0].m, b[j][0].s, b[j][0].d, end=' ')
#         else:
#             print("N", end=' ')
#     print()
ans = 0
for i in range(N):
    for j in range(N):
        for shark in board[i][j]:
            ans += shark.m
print(ans)