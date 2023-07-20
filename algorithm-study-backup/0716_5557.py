"""
11
8 3 2 4 8 7 2 4 0 8 8
"""
# D[i][j] = i까지 수를 활용해서 j를 만드는 방법의 개수
# D[i][j] = D[i-1][j-A[i]] + D[i-1][j+A[i]]
# j는 0~20사이의 값일 수 있다.

N = int(input())
K = 21 #j는 0~20사이의 값일 수 있다.
arr = list(map(int, input().split()))
answer = [[0]*K for _ in range(N)]
target = arr[N-1] #목표
arr = arr[:N-1] #arr에서 target값 제외
answer[0][arr[0]] = 1

for i in range(N-1):
    # print("i:", i)
    for j in range(K):
        if 0<=j-arr[i]<=20:
            answer[i][j] += answer[i-1][j-arr[i]]
        if 0<=j+arr[i]<=20:
            answer[i][j] += answer[i-1][j+arr[i]]
        # print(j, j - arr[i], j + arr[i], answer[i][j])

print(answer[N-2][target])