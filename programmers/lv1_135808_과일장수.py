def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) #정렬
    boxes = len(score) // m #판매할 상자 개수 구하기
    for i in range(boxes):
        temp = score[m*i: m*(i+1)]
        answer += min(temp) * m #최저 사과 점수 * 사과의 개수
    return answer