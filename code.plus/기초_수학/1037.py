"""
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 1
for i in range(N):
    answer *= arr[i]
print(answer)
"""

while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    while True:
        num = num * 10 + 1;
        num %= n
        if num == 0:
            print(i)
            break
        i += 1