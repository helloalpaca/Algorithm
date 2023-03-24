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
            val = heapq.heappop(arr)
            if val[1]:
                print(val[0])
            else:
                print(-val[0])
    else:
        if inp>=0:
            heapq.heappush(arr, (inp, 1))
        else:
            heapq.heappush(arr, (-inp, 0))