import sys
from collections import deque

N = int(input())

for _ in range(N):
    M, target = map(int, sys.stdin.readline().rstrip().split())
    d = deque(list(map(int, sys.stdin.readline().rstrip().split())))

    answer = 0
    value = d[target]

    while d:
        largest = max(d)
        front = d.popleft()
        target -= 1

        if front >= largest:
            answer += 1
            if target < 0:
                break
        else:
            d.append(front)
            if target < 0:
                target = len(d)-1

    print(answer)