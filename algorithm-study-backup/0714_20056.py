"""
N(board크기), M(파이어볼 개수), K(이동 횟수)
r, c, m, s, d
(r, c): 위치, m: 질량, s:속력, d:방향
4 2 1
1 1 5 2 2
1 4 7 1 6
"""

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 값 받기
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])

def move(board, board_next):
    for i in range(N):
        for j in range(N):
            for k in range(len(board[i][j])):
                m, s, d = board[i][j][k][0], board[i][j][k][1], board[i][j][k][2]
                nx = (i+dx[d]*s + N) % N
                ny = (j+dy[d]*s + N) % N
                board_next[nx][ny].append(board[i][j][k])
    return board_next

def divide_fireball():
    for i in range(N):
        for j in range(N):
            if len(board[i][j])>1:
                m, s, isOdd, isEven = 0, 0, False, False
                for k in range(len(board[i][j])):
                    m += board[i][j][k][0]
                    s += board[i][j][k][1]
                    d = board[i][j][k][2]
                    if d%2==0: isEven = True
                    else: isOdd = True
                if (not isEven and isOdd) or (not isOdd and isEven):
                    nd=[0, 2, 4, 6]
                else:
                    nd=[1, 3, 5, 7]
                m //= 5
                s //= len(board[i][j])
                board[i][j] = [] #기존 애들 삭제
                if m > 0:
                    for k in range(4):
                        board[i][j].append([m, s, nd[k]])


# K번 이동하는 동안
for i in range(K):
    board_next = [[[] for _ in range(N)] for _ in range(N)]
    board = move(board, board_next)
    divide_fireball()

answer = 0
# for bo in board:
#     print(bo)
for i in range(N):
    for j in range(N):
        for k in range(len(board[i][j])):
            answer += board[i][j][k][0]
print(answer)