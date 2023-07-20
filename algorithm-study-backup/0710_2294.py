"""
3 15
1
5
12
"""

INF = int(1e9)
N, K = map(int, input().split())
arr = [INF for _ in range(K+1)]
coins = []
for _ in range(N):
    coins.append(int(input()))
arr[0] = 0
for coin in coins:
   for i in range(coin, K+1):
       arr[i] = min(arr[i], arr[i-coin]+1)
if arr[K] == INF:
    print(-1)
else:
    print(arr[K])