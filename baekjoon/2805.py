def isTargetTrue(N, target, trees, mid):
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree-mid
        if cnt > target:
            break
    if cnt >= target:
        return True
    return False

def solution(N, target, trees):
    answer = 0
    start = 0
    end = max(trees)

    while start <= end:
        mid = (start+end)//2
        if isTargetTrue(N, target, trees, mid):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


if __name__ == '__main__':
    N, target = map(int, input().split())
    trees = list(map(int, input().split()))

    print(solution(N, target, trees))