from collections import deque
from collections import defaultdict


def solution(tickets):
    answer = []
    dic = defaultdict(list)

    for [start, end] in tickets:
        dic[start].append(end)
    for k in dic.keys():
        dic[k].sort(reverse=True)  # 알파벳 순 나열을 위한 sort

    stack = ["ICN"]
    while stack:
        start = stack[-1]
        if not dic[start]:  # start에서 출발하는 항공편이 없을 때
            answer.append(stack.pop())
        else:
            stack.append(dic[start].pop())

    return answer[::-1]