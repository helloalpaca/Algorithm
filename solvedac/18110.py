def my_round(n):
    if n-int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

if N == 0:
    print(0)
else:
    start = my_round(N * 0.15)
    end = N-start
    print(my_round(sum(arr[start:end])/(end-start)))