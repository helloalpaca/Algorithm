import math

def binary_search(li, target):
    start = 0
    end = len(li)-1

    while start <= end:
        mid = math.floor((start+end)/2)
        if li[mid] == target:
            return 1
        elif li[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return 0

def solution(N, li_n, M, li_m):
    answer = [0 for i in range(M)]
    li_n.sort()

    for i in range(M):
        answer[i] = binary_search(li_n, li_m[i])

    return answer


if __name__ == '__main__':
    N = int(input())
    li_n = list(map(int, input().split()))

    M = int(input())
    li_m = list(map(int, input().split()))

    answer = solution(N, li_n, M, li_m)

    for ans in answer:
        print(ans)