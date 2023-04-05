from collections import deque
import sys

MAX = 100001
N, K = map(int, sys.stdin.readline().split())
d = deque([0 for _ in range(MAX)])

def BFS(start):
    q = deque([start])
    d[start] = 0
    while q:
        now = q.popleft()
        if now == K:
            return d[K]
        for n in [now+1, now-1, 2*now]:
            if n >= 0 and n < MAX and d[n]==0:
                d[n] = d[now]+1
                q.append(n)


print(BFS(N))