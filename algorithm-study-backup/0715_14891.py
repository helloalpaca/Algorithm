from collections import deque
import sys
read = sys.stdin.readline
arr = [deque(list(map(int, list(read().rstrip())))) for _ in range(4)]

K = int(read())
for _ in range(K):
    d = [0] * 4  # 각 톱니의 회전방향을 정할 array
    num, direction = map(int, read().split())
    # print(num, direction)
    num -= 1 #index화
    d[num] = direction

    #왼쪽 톱니들 회전 방향 구하기
    for i in range(num-1, -1, -1):
        if arr[i][2] != arr[i+1][6]:
            d[i] = -d[i+1]
        else:
            break

    #오른쪽 톱니들 회전 방향 구하기
    for i in range(num+1, 4):
        if arr[i-1][2] != arr[i][6]:
            d[i] = -d[i-1]
        else:
            break
    #회전하기
    for i in range(4):
        if d[i] == 0:
            continue
        elif d[i] == 1:
            arr[i].appendleft(arr[i].pop())
        elif d[i] == -1:
            arr[i].append(arr[i].popleft())

answer = 0
for i in range(4):
    # print(i, arr[i][0])
    if arr[i][0] == 1:
        answer += 1*(2**i)
print(answer)
