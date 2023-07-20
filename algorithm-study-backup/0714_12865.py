# D[n] = max(D[j], D[j-w[i]]+v[i])
N, K = map(int,input().split())
arr = [[0,0]]+[list(map(int,input().split())) for _ in range(N)]
d = [0]*(K+1)
for i in range(1, N+1):
    # print("i: ", i,", arr[i]: ", arr[i])
    for j in range(K, 0, -1):
        if j-arr[i][0] >= 0:
            d[j] = max(d[j],d[j-arr[i][0]]+arr[i][1])
            # print("j: ", j,", d[j]: ", d[j])
    # print()
print(d[K])