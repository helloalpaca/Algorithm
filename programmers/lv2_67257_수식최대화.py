from itertools import permutations
import re


def calculate(val1, val2, exp):
    if exp == "-":
        return int(val1) - int(val2)
    elif exp == "+":
        return int(val1) + int(val2)
    else:
        return int(val1) * int(val2)


def solution(expression):
    answer = 0

    li = re.findall("\d+|\W", expression)  # 숫자가 반복되거나, 숫자가 아니거나
    exp = re.findall("\W", expression)
    exp = set(exp)  # 연산자만 찾기
    permutation = permutations(exp, len(exp))
    # 연산자 우선순위에 따라서 연산한 결과 가져오기
    for permut in permutation:  # 연산자 우선순위에 따라서
        # print(permut)
        temp = li[:]
        for i in range(len(exp)):
            while permut[i] in temp:
                idx = temp.index(permut[i])
                value = calculate(temp[idx - 1], temp[idx + 1], temp[idx])
                temp = temp[:idx - 1] + [str(value)] + temp[idx + 2:]
                # print(permut[i], temp)
        if abs(int(temp[0])) > answer:
            answer = abs(int(temp[0]))

    return answer