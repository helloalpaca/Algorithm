N = input()
answer = []

for i in range(len(N)):
    answer.append(N[i])

answer.sort(reverse=True)
print(''.join(answer))