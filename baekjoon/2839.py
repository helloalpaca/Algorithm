N = int(input())

answer = -1
max_five = N//5

for five in range(max_five+1):
    left = N - 5*five
    if left % 3 == 0:
        cnt = five + left//3
        if cnt < answer or answer == -1:
            answer = cnt

print(answer)