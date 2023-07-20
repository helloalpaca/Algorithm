"""
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4
"""
# 1. 비어 있는 칸 중에서, 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러개면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 간다.
# 3. 2를 만족하는 칸도 여러개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러개면
#    열의 번호가 가장 작은 칸으로 자리를 정한다.
import sys
read = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(read().rstrip())
num = N ** 2
arr = [list(map(int, read().rstrip().split())) for _ in range(num)]
board = [[0] * N for _ in range(N)]

def sit(idx, likes):
    tmp = []
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                like = 0
                empty = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if board[nx][ny] == 0:
                            empty += 1
                        if board[nx][ny] in likes:
                            like += 1
                tmp.append((i, j, like, empty))

    tmp.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))
    # 이중 for문을 순회하면서 비어있는 자리를 찾는다.
    # 비어있는 자리에서 인접한 칸에 내가 좋아하는 학생이 몇명 앉아있는지 찾는다.
    # 인접한 칸 중에서 비어있는 칸의 개수를 찾는다.
    # sort해서 행,열 번호가 가장 작은 걸로 선택한다.
    board[tmp[0][0]][tmp[0][1]] = idx

likes = [[0]*4 for _ in range(num+1)]
for i in range(num):
    n, l1, l2, l3, l4 = arr[i]
    likes[n] = [l1, l2, l3, l4]
    sit(n, likes[n])

# for bo in board:
#     print(bo)

answer = 0
for i in range(N):
    for j in range(N):
        idx = board[i][j]
        like = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] in likes[idx]:
                    like += 1
        if like > 0:
            answer += 10 ** (like-1)
print(answer)