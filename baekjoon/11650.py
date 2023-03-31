import sys

N = int(input())
answer = []

for _ in range(N):
    answer.append(tuple(map(int, sys.stdin.readline().split())))

answer.sort(key=lambda x: (x[0], x[1]))

for ans in answer:
    print(ans[0], ans[1])