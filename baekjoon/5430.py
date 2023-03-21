from collections import deque

N = int(input())

for i in range(N):
    result = ""
    p = list(input())
    n = int(input())
    arr = input()[1:-1].split(',')
    d = deque(arr)
    flag = 0

    if n == 0:
        d = []

    for j in p:
        if j == "R":
            flag += 1
        else:
            if len(d) == 0:
                result = "error"
                break
            else:
                if flag % 2 == 0:
                    d.popleft()
                else:
                    d.pop()

    if result == "error":
        print(result)
    else:
        if flag % 2 == 0:
            print("[" + ",".join(d) + "]")
        else:
            d.reverse()
            print("[" + ",".join(d) + "]")


for j in p:
    if j == "R":
        flag += 1
    else:
        if len(d) == 0:
            result = "error"
            break
        else:
            if flag % 2 == 0:
                d.popleft()
            else:
                d.pop()