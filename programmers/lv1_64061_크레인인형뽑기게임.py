# 리스트 뒤집기 (리스트-맵-리스트, 집) 외우기

from collections import deque

def solution(board, moves):
    answer = 0
    newboard = list(map(list, zip(*board)))
    basket = deque([])

    for move in moves:
        temp = newboard[move - 1]
        for i in range(len(board)):
            if temp[i] != 0:
                if len(basket) > 0 and basket[-1] == temp[i]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(temp[i])
                newboard[move - 1][i] = 0
                break
    return answer