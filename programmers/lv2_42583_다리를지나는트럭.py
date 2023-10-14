from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1

    truck_weights = truck_weights[::-1]  # 트럭은 stack
    q = deque([[truck_weights.pop(), 1]])  # 브릿지는 queue

    while truck_weights:
        new = truck_weights.pop()
        sum_of_q = 0  # 현재 브릿지에 있는 트럭의 무게를 다 합쳤을 때
        for i in range(len(q)):
            sum_of_q += q[i][0]

        if sum_of_q + new > weight:  # 새로운 트럭이 진입 가능한지 안한지 확인
            truck_weights.append(new)
        else:
            q.append([new, 0])

        for i in range(len(q)):
            q[i][1] += 1

        if q[0][1] == bridge_length:
            q.popleft()

        answer += 1

    answer += (bridge_length - q.pop()[1])
    return answer + 1