def factorial(num):
    if num <= 1:
        return 1
    else:
        answer = num*factorial(num-1)
        return answer

N = int(input())
print(factorial(N))