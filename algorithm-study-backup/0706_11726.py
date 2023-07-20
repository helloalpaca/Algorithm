# DP
# n-1만큼 적절히 채운 상태라고 가정 -> 1만큼에 놓을 수 있는 경우의 수 : 1개
# n-2만큼 적절히 채운 상태라고 가정 -> 2만큼에 놓을 수 있는 경우의 수 : 1개
# D[n] = D[n-1] + D[n-2]

N = int(input())
arr = [0 for _ in range(N+1)]
arr[0] = 1
arr[1] = 1

for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]
    arr[i] %= 10007
print(arr[N])