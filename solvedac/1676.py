N = int(input())
v = 1
for i in range(2, N+1):
    v *= i

answer = 0
v = str(v)
l = len(v)
for i in range(l):
    if v[l-1-i] == '0':
        answer += 1
    else:
        print(answer)
        break