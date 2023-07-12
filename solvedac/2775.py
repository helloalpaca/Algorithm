"""
2
1
3
2
3
"""

T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    arr = [[0]*N for _ in range(K)]

    for i in range(N):
        arr[0][i] = i+1

    for i in range(1, K):
        for j in range(N):
            for k in range(j+1):
                arr[i][j] += arr[i-1][k]

    print(sum(arr[K-1]))