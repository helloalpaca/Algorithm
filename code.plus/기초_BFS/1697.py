import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

def BFS():
    q = deque([(N, 0)])
    v = [False] * (100001)
    while q:
        now, time = q.popleft()
        for x in [now-1, now+1, 2*now]:
            if 0<=x<=100000 and not v[x]:
                if v[x] == K:
                    print(time)
                    sys.exit()
                v[x] = True
                q.append((x, time+1))

BFS()