import math

N, K = map(int, input().split())
answer = 0

if K<0 or K>N:
    print(answer)
else:
    answer = math.factorial(N)/math.factorial(K)/math.factorial(N-K)
    print(int(answer))