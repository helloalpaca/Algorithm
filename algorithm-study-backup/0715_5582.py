"""
ABRACADABRA
ECADADABRBCRDARA
"""
import sys

A = " "+sys.stdin.readline().rstrip()
B = " "+sys.stdin.readline().rstrip()
lenA = len(A)
lenB = len(B)

arr = [[0]*(lenB) for _ in range(lenA)]

answer = 0
for i in range(1, lenA):
    for j in range(1, lenB):
        if A[i] == B[j]:
            arr[i][j] = arr[i-1][j-1]+1
            if arr[i][j] > answer:
                answer = arr[i][j]
        # else:
        #     arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(answer)
