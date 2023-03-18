def add(str):
    add_num = 0
    numbers = list(map(int, str.split("+")))
    for num in numbers:
        add_num += num
    return add_num
def solution(str):
    answer = add(str[0])

    for i in range(1, len(str)):
        answer -= add(str[i])
    return answer


if __name__ == '__main__':
    str = input().split("-")

    print(solution(str))