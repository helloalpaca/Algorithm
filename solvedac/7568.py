"""
5
55 185
58 183
88 186
60 175
46 155
"""
import sys
read = sys.stdin.readline
N = int(input())
arr = [[0]*2 for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, read().split()))

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                rank += 1
    print(rank, end=' ')
