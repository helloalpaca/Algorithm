"""
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2
"""
import sys
read = sys.stdin.readline
N, L = map(int, read().rstrip().split())
board = [[0]*N for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, read().rstrip().split()))
targets = []

def get_target():
    for i in range(N):
        targets.append(board[i])
    for i in range(N):
        target = []
        for j in range(N):
            target.append(board[j][i])
        targets.append(target)

get_target()
answer = 0
# targets.append([3,2,2,1,1,1])

for target in targets:
    curve = [False for _ in range(N)]
    flag = True

    for i in range(1, N):
        # 차이가 2이상이면 False
        # 차이가 1이면 -> 경사로를 놓을 수 있는지에 따라서 True, False
        # 차이가 0이면 continue
        if target[i] == target[i-1]:
            continue
        elif target[i]+1 == target[i-1]: #왼쪽이 높을 때
            # print(i, ": 왼쪽이 높다")
            for k in range(L):
                if i+k >= N:
                    flag = False
                    break
                if curve[i+k]:
                    flag = False
                    break
                if target[i] != target[i+k]:
                    flag = False
                    break
                curve[i+k] = True
        elif target[i] == target[i-1] + 1: #오른쪽이 높을 때
            for k in range(1, L+1):
                if i - k < 0:
                    flag = False
                    break
                if curve[i - k]:
                    flag = False
                    break
                if target[i - 1] != target[i - k]:
                    flag = False
                    break
                curve[i - k] = True
        else:
            flag = False
            break
    if flag:
        answer += 1
print(answer)

