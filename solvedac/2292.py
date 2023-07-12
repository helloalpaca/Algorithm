N = int(input())

term = 6
end = 1
answer = 1
while True:
    if N <= end:
        print(answer)
        break
    answer += 1
    end += term
    term += 6
