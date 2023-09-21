from copy import deepcopy

def solution(cards):
    answer = 0
    boxes = [0] * 100
    idx = 0  # 상자 위치
    num = 1  # 현재 내가 바라보는 cards의 위치
    flag = 0  # 이때까지 방문한 cards의 개수 다 더하기
    while flag < len(cards):
        # print("최상위", num, cards)
        if cards[num-1] == 0:
            i = num
            while True:
                if cards[i] != 0:
                    break
                i += 1
            num = i+1
            # print(num)
            continue
        while True:
            # print(num, cards, cards[num-1]==0)
            if cards[num - 1] != 0:
                boxes[idx] += 1
                tmp = deepcopy(num)
                num = cards[tmp - 1]
                cards[tmp - 1] = 0
                flag += 1
            else:
                idx += 1
                break
    boxes.sort(reverse=True)
    return boxes[0] * boxes[1]