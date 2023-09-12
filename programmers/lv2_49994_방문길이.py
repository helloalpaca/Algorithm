# 코드 라인 수를 줄이는데만 치중했더니 채점했을때 10번의 시간이 25ms->38ms로 늘어났음
# set에 요소를 추가하는걸 최소로 해야할듯
# 배열로 더하는 (x+dx[0) 코드도 삭제했더니 25ms->22ms로 줄어듬
# 배열(25ms, 35줄) -> set두번(38ms, 21줄) -> 지금 코드가 최종(22ms, 32줄)
# set 안쓰니까 10초됨(38줄), 시간 생각하면 무조건 배열로 푸는게 이득
# 2차원 배열에서 3차원 배열로 바꾸니까 평균 시간이 더 늘어남
# -> 프로그래머스 테스트마다 시간이 달라짐, 그래도 3차원 배열이 조금 느린듯

# def solution(dirs):
#     x, y = 5, 5
#     s = set()
#
#     for dr in dirs: #dir은 예약어
#         bx, by = x, y
#         if dr == 'U':
#             x += 1
#             if x > 10:
#                 x = 10
#             else:
#                 s.add((bx, by, x, y))
#         elif dr == 'D':
#             x -= 1
#             if x < 0:
#                 x = 0
#             else:
#                 s.add((x, y, bx, by))
#         elif dr == 'R':
#             y += 1
#             if y > 10:
#                 y = 10
#             else:
#                 s.add((bx, by, x, y))
#         else:
#             y -= 1
#             if y < 0:
#                 y = 0
#             else:
#                 s.add((x, y, bx, by))
#
#     return len(s)
def solution(dirs):
    answer = 0
    x, y = 5, 5
    col = [[0] * 11 for _ in range(11)]
    row = [[0] * 11 for _ in range(11)]

    for dr in dirs:
        bx, by = x, y
        if dr == 'U':
            x += 1
            if x > 10:
                x = 10
            else:
                col[bx][by] = 1
        elif dr == 'D':
            x -= 1
            if x < 0:
                x = 0
            else:
                col[x][y] = 1
        elif dr == 'R':
            y += 1
            if y > 10:
                y = 10
            else:
                row[bx][by] = 1
        else:
            y -= 1
            if y < 0:
                y = 0
            else:
                row[x][y] = 1

    for i in range(11):
        for j in range(11):
            answer += col[i][j] + row[i][j]

    return answer