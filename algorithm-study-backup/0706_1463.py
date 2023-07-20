# 10

INF = int(1e9)
N = int(input())
arr = [INF for _ in range(N+1)]
arr[0], arr[1] = 0, 0

for i in range(1, N):
    if i+1<=N and arr[i+1]> arr[i]+1: arr[i+1] = arr[i]+1
    if 2*i<=N and arr[2*i]> arr[i]+1: arr[2*i] = arr[i]+1
    if 3*i<=N and arr[3*i]> arr[i]+1: arr[3*i] = arr[i]+1
print(arr[N])