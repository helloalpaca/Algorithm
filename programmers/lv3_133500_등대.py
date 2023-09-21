# dfs를 너무 오랜만에 풀어서 아이디어가 기억 안남
# 참고 : https://www.ai-bio.info/programmers/133500
# 외워야 할 것 
# 1. setrecursionlimit
# 2. defaultdict 선언
# 3. dfs 아이디어

import sys
from collections import defaultdict

sys.setrecursionlimit(1000001)  # 8,9번 런타임 에러

edges = defaultdict(list)
v = [False] * 100001

def dfs(edge):
    v[edge] = True
    if not edges[edge]:  # edge가 리프노드라면 # len(edges[edge]) == 1로하면 왜 안되는걸까..
        return 1, 0  # 내가 켜지면 1, 내가 꺼지면 0

    on, off = 1, 0
    for e in edges[edge]:
        if not v[e]:
            temp_on, temp_off = dfs(e)
            on += min(temp_on, temp_off)  # 내가 켜젔다면, 자식은 onoff상관X 더 작은 값 더하기
            off += temp_on  # 내가 꺼져있으면 자식은 무조건 켜져있어야 함
    return on, off

def solution(n, lighthouse):
    for edge in lighthouse:
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])

    return min(dfs(1))