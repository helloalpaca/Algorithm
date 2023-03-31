import sys

N = int(input())
answer = set()

for _ in range(N):
    answer.add(sys.stdin.readline().rstrip())

answer = list(answer)
answer.sort(key=lambda x: (len(x), x))


for ans in answer:
    print(ans)