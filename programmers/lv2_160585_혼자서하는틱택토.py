from collections import Counter

def bingo(board):
    cnt_o = 0
    cnt_x = 0
    # 가로줄
    for idx in range(3):
        temp = board
        if Counter(temp[idx])['O'] == 3:
            cnt_o += 1
        if Counter(temp[idx])['X'] == 3:
            cnt_x += 1
    # 세로줄
    for idx in range(3):
        temp = board[0][idx] + board[1][idx] + board[2][idx]
        if Counter(temp)['O'] == 3:
            cnt_o += 1
        if Counter(temp)['X'] == 3:
            cnt_x += 1
    # 대각선1
    temp = board[0][0] + board[1][1] + board[2][2]
    if Counter(temp)['O'] == 3:
        cnt_o += 1
    if Counter(temp)['X'] == 3:
        cnt_x += 1

        # 대각선2
    temp = board[0][2] + board[1][1] + board[2][0]
    if Counter(temp)['O'] == 3:
        cnt_o += 1
    if Counter(temp)['X'] == 3:
        cnt_x += 1
    return cnt_o, cnt_x


def solution(board):
    answer = 1
    temp = ''.join(board)
    cntO = ''.join(board).count('O')
    cntX = ''.join(board).count('X')
    if cntX > cntO or cntO - cntX >= 2:  # x의 개수가 o보다 많거나, o가 두개 이상 많으면 실패
        answer = 0

    won_o, won_x = bingo(board)  # board에서 O와 X의 빙고 개수 구하기
    if won_o > 0 and won_x > 0:  # 둘 다 빙고가 있으면 실패
        answer = 0
    if won_o and cntO == cntX:  # O가 빙고 -> 빙고 이후에 x를 놓으면 실패
        answer = 0
    if won_x and cntO == cntX + 1:  # X가 빙고 -> 빙고 이후에 o를 놓으면 실패
        answer = 0
    return answer