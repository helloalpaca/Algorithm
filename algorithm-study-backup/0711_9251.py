"""
ACAYKP
CAPCAK
"""

A = input()
B = input()
LA = len(A)
LB = len(B)
A = " "+A
B = " "+B
arr = [[0]*(LB+1) for _ in range(LA+1)]

for i in range(1, LA+1):
    for j in range(1, LB+1):
        if A[i] == B[j]:
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])
print(arr[LA][LB])