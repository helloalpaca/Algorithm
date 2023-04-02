import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
S = {}
answer = 0

for _ in range(N):
    S[sys.stdin.readline().rstrip()] = 1

for _ in range(M):
    inp = sys.stdin.readline().rstrip()
    if inp in S:
        answer += 1

print(answer)