def solution(numbers):
    size = len(numbers)
    answer = [-1] * size
    stack = []

    for i in range(size):
        while stack and numbers[stack[-1]] < numbers[i]:
            num = stack.pop()
            answer[num] = numbers[i]
            # print(num, numbers[i], answer)
        stack.append(i)

    return answer