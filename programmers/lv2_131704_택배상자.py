# order를 기준으로 문제를 풀었을 때 -> 30줄
# 컨베이어 벨트를 기준으로 문제를 풀었을 때 -> 14줄
# 관점의 차이. 어떤걸 기준으로 삼을지 먼저 고민하고 문제를 풀자

from collections import deque
def solution(order):
    answer = 0
    d = deque([])

    for i in range(1, len(order)+1):
        d.appendleft(i) #처음에는 무조건 보조에 넣고

        while len(d) > 0:
            if order[answer] == d[0]: #보조==order[answer]인거 계속 빼내기
                answer += 1
                d.popleft()
            else: #더이상 보조에서 꺼낼 수 있는게 없다. while문 탈출
                break

    return answer

"""
from collections import deque

def solution(order):
    answer = 1
    lastest = order[0]
    d = deque([i for i in range(1, lastest)])
    visited = [False] * (len(order) + 1)
    visited[lastest] = True

    for i in range(1, len(order)):
        visited[order[i]] = True
        if order[i] == lastest + 1:
            answer += 1
            latest = order[i]
        elif order[i] < lastest:
            if order[i] == d[-1]:
                d.pop()
                answer += 1
                lastest = order[i]
            else:
                break
        elif order[i] > lastest:
            for j in range(lastest + 1, order[i]):
                if not visited[j]:
                    d.append(j)
            answer += 1
            lastest = order[i]
        # print(order[i], d, answer)

    return answer
"""