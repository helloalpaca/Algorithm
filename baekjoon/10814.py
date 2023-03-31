import sys

N = int(input())
answer = []

for _ in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    answer.append([int(age), name])

answer.sort(key=lambda x: x[0])

for ans in answer:
    print(ans[0], ans[1])