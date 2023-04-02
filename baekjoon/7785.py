import sys
from collections import deque

N = int(input())
log = []

for _ in range(N):
    name, stat = sys.stdin.readline().rstrip().split()
    if stat == "enter":
        log.append(name)
    else:
        log.pop(log.index(name))

log.sort(reverse=True)
for name in log:
    print(name)