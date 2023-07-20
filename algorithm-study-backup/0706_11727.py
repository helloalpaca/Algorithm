# D[n-1]일 때 경우의 수 : 1가지
# D[n-2]일 때 경우의 수 : 2가지
# D[n] = D[n-1] + 2*D[n-2]

N = int(input())
arr = [0 for _ in range(N+1)]
arr[0] = 1
arr[1] = 1

for i in range(2, N+1):
    arr[i] = arr[i-1] + 2*arr[i-2]
    arr[i] %= 10007
print(arr[N])