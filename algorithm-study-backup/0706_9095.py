# D[n] = D[n-1] + D[n-2] + D[n-3]

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0 for _ in range(N+1)]
    if N == 0:
        print(1)
    elif N==1:
        print(1)
    elif N==2:
        print(2)
    elif N==3:
        print(4)
    else:
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        arr[3] = 4
        for i in range(4, N+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        print(arr[N])
