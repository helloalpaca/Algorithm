answer = [0, 0]


def compress(x, y, n, arr):
    first = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != first:
                n //= 2
                compress(x, y, n, arr)
                compress(x, y + n, n, arr)
                compress(x + n, y, n, arr)
                compress(x + n, y + n, n, arr)
                return
    answer[first] += 1


def solution(arr):
    compress(0, 0, len(arr), arr)
    return answer