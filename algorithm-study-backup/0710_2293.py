"""
3 10
1
2
5
"""

N, K = map(int, input().split())
arr = [0 for _ in range(K+1)]
coins = []
for _ in range(N):
    coins.append(int(input()))
arr[0] = 1

for coin in coins:
    for i in range(coin, K+1):
        arr[i] += arr[i - coin]

print(arr[K])