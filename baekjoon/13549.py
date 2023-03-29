import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize

def BFS(N, K):
    d = deque([])
    d.append((0, N))
    board = [INF] * 100001
    board[N] = 0
    while d:
        dist, now = d.popleft()
        for x in [(1, now+1), (1, now-1), (0, now*2)]:
            if 0<=x[1]<100001:
                if board[x[1]] > dist+x[0]:
                    board[x[1]] = dist+x[0]
                    d.append((board[x[1]], x[1]))
    return board[K]

print(BFS(N, K))