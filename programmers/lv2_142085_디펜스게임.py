# 최대-최소값 문제에서 heapq 아이디어 생각해내기

import heapq

def solution(n, k, enemy):
    answer = 0
    t = 0
    q = []
    for e in enemy:
        t += e
        heapq.heappush(q, -e)
        if t > n:
            if k == 0:
                break
            t += heapq.heappop(q)
            k -= 1
        answer += 1
    return answer

# def solution(n, k, enemy):
#     answer = 0
#     de = [False] * len(enemy)
#     rnd = 0
#     tmp = 0  # 무적권 없이 진행 가능한 라운드 구하기 위한 변수
#     while tmp + enemy[rnd] <= n:
#         tmp += enemy[rnd]
#         rnd += 1
#     # 무적권 k만큼 더하기
#     if rnd == 0: #무적권 없이 진행 가능한 라운드 없음
#         return k
#     rnd += k
#     # rnd안의 라운드에서 무적권을 쓸 라운드 구하기
#     defense = [[enemy[i], i] for i in range(len(enemy[:rnd]))]
#     defense.sort(reverse=True, key=lambda x: (x[0], -x[1]))  # sort해서
#     defense = defense[:k]  # enemy가 제일 큰 k개 구하기
#     for i in range(k):
#         de[defense[i][1]] = True
#     # defense = [defense[i][1] for i in range(k)] # 해당 라운드 index만 다시 defense에 저장
#
#     # defense.sort()
#     # print(de)
#     # print(defense)
#     # for문을 돌면서 무적권을 쓰는 라운드를 제외한 병사 숫자 구하기, 남은 병사 숫자보다 크면 break
#     while True:
#         print(answer, n, de[answer])
#         if de[answer]:  # 무적권을 쓰는 라운드
#             answer += 1
#             continue
#         n -= enemy[answer]
#         if n > 0:
#             answer += 1
#         else:
#             break
#     # for i in range(len(enemy)):
#     #     answer += 1
#     #     if i in defense:
#     #         continue
#     #     n -= enemy[i]
#     #     if n == 0:
#     #         break
#     #     elif n < 0:
#     #         answer -= 1
#     #         break
#     return answer
#
# # print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# print(solution(2, 4, [3, 3, 3, 3]))