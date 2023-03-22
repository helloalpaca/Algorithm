import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
cmds = list(map(int, sys.stdin.readline().split()))
d = deque([i for i in range(1, N+1)])

answer = 0

for cmd in cmds:
    while True:
        if d[0] == cmd:
            d.popleft()
            break
        else:
            if d.index(cmd) <= len(d)//2:
                d.rotate(-1)
            else:
                d.rotate(1)
            answer+=1
print(answer)
