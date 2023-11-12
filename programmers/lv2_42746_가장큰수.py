def solution(numbers):
    temp = [str(num) for num in numbers]
    temp.sort(key=lambda num: num * 3, reverse=True)

    return str(int(''.join(temp)))