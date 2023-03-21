import sys
from collections import deque

N = int(input())
d = deque([])

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        d.append(cmd[1])
    else:
        if cmd[0] == "pop":
            if len(d) == 0:
                print(-1)
            else:
                print(d.popleft())
        elif cmd[0] == "size":
            print(len(d))
        elif cmd[0] == "empty":
            if len(d) == 0:
                print(1)
            else:
                print(0)
        elif cmd[0] == "front":
            if len(d) == 0:
                print(-1)
            else:
                print(d[0])
        elif cmd[0] == "back":
            if len(d) == 0:
                print(-1)
            else:
                print(d[-1])