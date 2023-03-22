import sys

M, N = map(int, sys.stdin.readline().split())
board = []
answer = 10000000

for _ in range(M):
    board.append(list(sys.stdin.readline().rstrip()))

for i in range(M-7):
    for j in range(N-7):
        cnt1 = 0
        cnt2 = 0
        start = board[i][j]
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k-i+l-j)%2==0:
                    if board[k][l]!=start:
                        cnt1 += 1
                    else:
                        cnt2 += 1
                elif (k-i+l-j)%2==1:
                    if board[k][l]==start:
                        cnt1 += 1
                    else:
                        cnt2 += 1
        if cnt1 < answer:
            answer = cnt1
        if cnt2 < answer:
            answer = cnt2
print(answer)
