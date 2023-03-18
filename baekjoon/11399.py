def solution(N, P):
    answer = 0
    P.sort()

    for i in range(N):
        answer += P[i]*(N-i)
    return answer


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    print(solution(N, P))