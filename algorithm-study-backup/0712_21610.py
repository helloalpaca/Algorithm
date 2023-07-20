import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud_now = [(0, N-1), (1, N-1), (0, N-2), (1, N-2)]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

for _ in range(M):
    path, dist = map(int, input().split())

    # 1. 구름 위치 구하기
    cloud_next = []
    for x, y in cloud_now:
        nx = (x+dx[path]*dist)%N
        ny = (y+dy[path]*dist)%N
        cloud_next.append((nx, ny))

    # 2. 물 증가
    for x, y in cloud_next:
        board[y][x] += 1

    # 3. 물 복사 버그
    for x, y in cloud_next:
        count = 0
        for i in (2, 4, 6, 8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[ny][nx] > 0:
                count += 1
        board[y][x] += count

    # 4. 구름생성
    cloud_next = set(cloud_next)
    cloud_now = []
    for y in range(N):
        for x in range(N):
            if (x, y) not in cloud_next and board[y][x] >= 2:
                board[y][x] -= 2
                cloud_now.append((x, y))

answer = 0
for i in board:
    answer += sum(i)
print(answer)