# D[N] = 카드 N개를 구매하는 최대 금액
# 맨 마지막 카드팩은 몇개? 몇번째? -> 모른다. 그러면 모든 방법을 다 해봐야한다.
# D[N] = D[i-j]+P[j]

N = int(input())
P = [0]+list(map(int, input().split()))
answer = [0 for _ in range(N+1)]

for i in range(1, N+1):
    temp = []
    for j in range(1, i+1):
        temp.append(answer[i-j]+P[j])
    # print(temp)
    answer[i] = max(temp)
print(answer[N])