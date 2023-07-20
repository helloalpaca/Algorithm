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
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N*N)]

for order in range(N*N):
    student = arr[order]
    like_list = student[1:]
    tmp = [] # 앉을수 있는 모든 자리를 구하고, 우선순위가 제일 높은 자리를 구한다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in like_list:
                            like += 1
                        if board[nx][ny] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3])) #like와 blank는 클수록, i와 j는 작을수록 우선순위가 높다.
    board[tmp[0][2]][tmp[0][3]] = student[0] #우선순위가 제일 높은 위치에 넣는다.

result = 0
arr.sort()

for i in range(N):
    for j in range(N):
        answer = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] in arr[board[i][j]-1]:
                    answer += 1
        if answer != 0:
            result += 10 ** (answer-1)
print(result)
