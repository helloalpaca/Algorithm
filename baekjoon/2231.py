def digits(num):
    cnt = 0  # N의 자리수
    temp = num
    while temp > 0:
        cnt += 1
        temp //= 10
    return cnt

N = int(input())
answer = 0

for i in range(1, N):
    dig = digits(i)
    result = i
    temp = i
    for j in range(1, dig+1):
        now = temp // (10 ** (dig - j))
        temp = temp - now * (10 ** (dig - j))
        result += now
    if result == N:
        answer = i
        break

print(answer)
