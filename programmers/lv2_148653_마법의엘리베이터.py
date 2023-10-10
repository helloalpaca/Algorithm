def solution(storey):
    answer = 0
    # 0~4 = -0~4
    # 5 = 그 다음 자릿수의 수에 따라 다름
    # 6~9 = +4~1
    while storey > 0:
        temp = storey % 10
        if temp == 5:
            ttemp = (storey % 100) // 10
            if ttemp <= 4:
                storey -= temp
                answer += temp
            else:
                storey += (10-temp)
                answer += (10-temp)
        elif temp <= 4:
            storey -= temp
            answer += temp
        else:
            storey += (10-temp)
            answer += (10-temp)
        storey //= 10
    return answer