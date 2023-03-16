def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []

    for i in range(len(prices)):
        while stack and prices[i]<prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer

print(solution([1, 2, 3, 2, 3]))