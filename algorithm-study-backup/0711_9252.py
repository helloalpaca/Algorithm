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
arr = [['']*(LB+1) for _ in range(LA+1)]

for i in range(1, LA+1):
    for j in range(1, LB+1):
        if A[i] == B[j]:
            arr[i][j] = arr[i-1][j-1]+A[i]
        else:
            if len(arr[i][j-1]) <= len(arr[i-1][j]):
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i][j-1]

print(len(arr[LA][LB]))
print(arr[LA][LB])