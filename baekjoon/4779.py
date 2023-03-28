import sys

def solution(n, num):
    if n==0:
        return
    else:
        for i in range(1, ((num//n)//3)+1):
            for j in range(3*n*i-2*n, 3*n*i-n):
                arr[j]=" "
        solution(n//3, num)

while True:
    N = sys.stdin.readline().rstrip()
    if N=="":
        break
    num = 3**int(N)
    arr = ["-" for _ in range(num)]
    solution(num//3, num)
    print(''.join(arr))
