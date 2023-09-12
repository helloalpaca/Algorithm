# combinations 공부
# [tuple(item[key] for key in i) for item in relation] <- 이런식으로 선언 가능한거 확인
# issubset, issuperset : 각각 하위집합, 상위집합인지를 확인하는 함수

from itertools import combinations

def solution(relation):
    col = len(relation[0])
    row = len(relation)

    list_for_comb = [i for i in range(col)]
    combi = [] # column수에 대한 모든 combination 구하기
    for i in range(1, col + 1):
        combs = list(combinations(list_for_comb, i))
        for comb in combs:
            combi.append(comb)

    unique = [] # 유일성에 맞지 않는 combi 삭제
    for i in combi:
        tmp = [tuple(item[key] for key in i) for item in relation]
        if len(set(tmp)) == row: # 중복되는 요소가 있으면 유일성 조건에 맞지 않는다.
            unique.append(i)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])): # 다른 누군가의 subset인지 확인
                answer.discard(unique[j])
    return len(answer)