def solution(N, distances, towns):
    answer = distances[0] * towns[0]

    min_town = towns[0]
    for i in range(1, N-1):
        if towns[i] < min_town:
            min_town = towns[i]
        answer += min_town * distances[i]

    return answer

if __name__ == '__main__':
    N = int(input())
    distances = list(map(int, input().split(" ")))
    towns = list(map(int, input().split(" ")))

    print(solution(N, distances, towns))