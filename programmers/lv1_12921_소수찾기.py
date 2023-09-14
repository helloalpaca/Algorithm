import math

def solution(n):
    arr = [1] * (n+1)
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i] == 1:
            for j in range(2, n//i+1):
                arr[i*j] = 0
    return sum(arr)-2