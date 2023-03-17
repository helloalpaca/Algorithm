def solution(N, meetings):
    answer = 0

    meetings.sort(key=lambda x: x[0])
    meetings.sort(key=lambda x: x[1])

    endTime = 0
    for start, end in meetings:
        if endTime <= start:
            endTime = end
            answer += 1

    return answer

if __name__ == '__main__':
    N = int(input())
    meetings = []

    for _ in range(N):
        meetings.append(list(map(int, input().split())))

    print(solution(N, meetings))