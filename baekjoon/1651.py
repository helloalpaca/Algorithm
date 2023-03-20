def isDivided(target, lengths, mid):
    cnt = 0
    for len in lengths:
        cnt += len // mid

    if target <= cnt:
        return True
    return False

def solution(N, target, lengths):
    answer = 0
    start = 1
    end = max(lengths)

    while start <= end:
        mid = (start+end)//2
        if isDivided(target, lengths, mid):
            answer = mid
            start = mid+1
        else:
            end = mid-1

    return answer


if __name__ == '__main__':
    N, target = map(int, input().split())

    lengths = []
    for _ in range(N):
        lengths.append(int(input()))

    print(solution(N, target, lengths))