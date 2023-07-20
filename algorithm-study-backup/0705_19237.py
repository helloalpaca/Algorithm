N, M, k = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(N)]
board_next = [[0 for _ in range(N)] for _ in range(N)]
smell = [[0 for _ in range(N)] for _ in range(N)]
smell_who = [[0 for _ in range(N)] for _ in range(N)]
direction = [0 for _ in range(M+1)]
priority = [[[0]*4 for _ in range(4)] for _ in range(M+1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    inp = list(map(int, input().split()))
    for j in range(N):
        board[i][j] = inp[j]
        if board[i][j] > 0:
            smell[i][j] = k
            smell_who[i][j] = board[i][j]

direction = [0] + [d-1 for d in map(int, input().split())]

for i in range(1, M+1):
    for j in range(4):
        priority[i][j] = [d-1 for d in map(int, input().split())]

def left_one():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def sharks():
    global smell_who
    # 상어 위치 전부 구하기
    q = []
    for i in range(N):
        for j in range(N):
            board_next[i][j] = 0
            if board[i][j] > 0:
                q.append((board[i][j], i, j)) #no, i, j
    q.sort(key=lambda x: x[0], reverse=True)

    # 상어마다 다음 방향 구하기
    for shark in q:
        no, x, y = shark
        d = direction[no]
        flag = False
        # 냄새 없
        for i in range(4):
            nd = priority[no][d][i]
            nx = x+dx[nd]
            ny = y+dy[nd]
            if 0 <= nx < N and 0 <= ny < N:
                if smell[nx][ny] == 0:
                    if board_next[nx][ny] == 0:
                        board_next[nx][ny] = no
                        direction[no] =nd
                    else:
                        if board_next[nx][ny] > no:
                            board_next[nx][ny] = no
                            direction[no] = nd

                    flag = True
                    break

        # smell이 없는 곳이 없어서, 이동하지 못했을 때 -> 내 냄새가 있는 곳으로 이동
        if not flag:
            for i in range(4):
                nd = priority[no][d][i]
                nx = x+dx[nd]
                ny = y+dy[nd]
                if 0<=nx<N and 0<=ny<N:
                    if smell[nx][ny]>0 and smell_who[nx][ny] == no:
                        board_next[nx][ny] = no
                        direction[no] = nd
                        break


    # 이동시키기, 냄새들-1
    for i in range(N):
        for j in range(N):
            board[i][j] = board_next[i][j]
            if smell[i][j] > 0:
                smell[i][j] -= 1
            if smell[i][j] == 0:
                smell_who[i][j] = 0
            if board_next[i][j] > 0:
                smell[i][j] = k
                smell_who[i][j] = board_next[i][j]

answer = -1

for t in range(1, 1001):
    sharks()
    if left_one():
        answer = t
        break
print(answer)