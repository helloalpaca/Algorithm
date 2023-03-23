import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
d = deque([i for i in range(1, N+1)])
answer = []

for i in range(N):
    for _ in range(K-1):
        d.append(d.popleft())
    answer.append(d.popleft())

print('<'+', '.join(map(str, answer))+'>')