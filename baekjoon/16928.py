from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
ladders = []
snakes = []
for _ in range(N):
    ladders.append(tuple(map(int, sys.stdin.readline().split())))
for _ in range(M):
    snakes.append(tuple(map(int, sys.stdin.readline().split())))
ladders = dict(ladders)
snakes = dict(snakes)

board = [0] * 101
visited = [False] * 101

q = deque([1])

while q:
    now = q.popleft()
    visited[now] = True
    for dice in range(1, 7):
        next = now+dice
        if next > 100:
            continue
        if board[next]==0:
            if next in ladders:
                next = ladders[next]
            if next in snakes:
                next = snakes[next]
            if not visited[next]:
                visited[next]=True
                board[next]=board[now]+1
                q.append(next)

print(board[100])