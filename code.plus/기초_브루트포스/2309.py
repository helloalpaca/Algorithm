# 방법1. 9명 중에 7명 찾기
# 방법2. 9명 중에 2명 찾기 = 9C2 = 36 (O(N2))
import sys

N = 9
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
total = sum(arr)

for i in range(N):
    for j in range(i+1, N):
        if total - arr[i] - arr[j] == 100:
            for k in range(N):
                if i == k or j == k:
                    continue
                print(arr[k])
            sys.exit(0)


