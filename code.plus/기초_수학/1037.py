"""
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 1
for i in range(N):
    answer *= arr[i]
print(answer)
"""