def solution(N, C, homes):
    answer = 0
    homes.sort()
    start = 1
    end = homes[-1] - homes[0]

    while start <= end:
        mid = (start + end) // 2
        cur = homes[0]
        cnt = 1
        for i in range(1, N):
            if homes[i] >= cur + mid:
                cnt += 1
                cur = homes[i]
        if cnt >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer

if __name__ == '__main__':
    N, C = map(int, input().split())
    homes = []
    for _ in range(N):
        homes.append(int(input()))

    print(solution(N, C, homes))

