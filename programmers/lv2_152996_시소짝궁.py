from collections import Counter


def solution(weights):
    weights.sort()
    answer = 0

    # 1:1인 애들 빠르게
    counter = Counter(weights)
    for key, value in counter.items():
        if value >= 2:
            answer += (value * (value - 1)) // 2

    weights = set(weights)

    for w in weights:
        for case in [2 / 3, 2 / 4, 3 / 4]:
            if w * case in weights:
                answer += counter[w] * counter[w * case]

    return answer