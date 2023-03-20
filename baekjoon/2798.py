def solution(N, target, cards):
    answer = 0

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                cnt = cards[i]+cards[j]+cards[k]
                if cnt <= target and answer < cnt:
                    answer = cnt

    return answer

if __name__ == '__main__':
    N, target = map(int, input().split())
    cards = list(map(int, input().split()))

    print(solution(N, target, cards))