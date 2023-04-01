import sys

N = int(input())
SG = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
problem = list(map(int, sys.stdin.readline().rstrip().split()))

dic = {i: 1 for i in SG}
answer = []
for pro in problem:
    if pro in dic:
        answer.append("1")
    else:
        answer.append("0")

print(" ".join(answer))