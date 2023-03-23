from collections import deque

N = int(input())
d = deque([i for i in range(1, N+1)])
cnt = 0

while len(d) > 1:
    if cnt%2 == 0:
        d.popleft()
    else:
        d.append(d.popleft())
    cnt += 1

print(d[0])