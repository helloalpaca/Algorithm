def solution(N, K, coins):
    answer = 0
    for i in range(N):
        if(coins[i]<K):
            K = K%coins
            answer+=1
    return answer

if __name__ == '__main__':
    N, K = map(int, input().split())

    coins = []
    for _ in range(N):
        coins.append(int(input()))
    coins.sort(reverse=True)

    inp = "10 4790" \
          "1" \
          "5" \
          "10" \
          "50" \
          "100" \
          "500" \
          "1000" \
          "5000" \
          "10000" \
          "50000"
    solution(N,K,coins)