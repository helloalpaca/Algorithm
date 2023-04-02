import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
H = set()
S = set()

for _ in range(N):
    H.add(sys.stdin.readline().rstrip())

for _ in range(M):
    S.add(sys.stdin.readline().rstrip())

temp = H - S
answer = sorted(list(H - temp))

print(len(answer))
for ans in answer:
    print(ans)