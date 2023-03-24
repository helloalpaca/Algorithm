import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    inp = int(sys.stdin.readline().rstrip())
    if inp == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -inp)