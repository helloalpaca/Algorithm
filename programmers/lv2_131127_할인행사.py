# Counter 무조건 외우기
# zip도 외우자 제발..

from collections import Counter

def solution(want, number, discount):
    answer = 0
    count = {w: n for w, n in zip(want, number)}

    for i in range(len(discount) - 9):
        temp_count = Counter(discount[i:i + 10])
        if temp_count == count:
            answer += 1

    return answer