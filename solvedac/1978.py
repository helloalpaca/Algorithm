"""
1은 소수가 아니다.
"""
# INPUT 받기
N = int(input())
arr = [d for d in map(int, input().split())]

# 초기값 세팅 for 에라토스테네스의 체
maxIdx = max(arr)+1
prime_board = [-1 for _ in range(maxIdx)] #한번도 들리지 않은 위치: -1, 소수의 배수: 0, 소수: 1
prime_board[1] = 0

for i in range(2, maxIdx):
    if prime_board[i] == -1: #다른 수의 배수가 아닌 수
        prime_board[i] = 1
    for cnt in range(i+1, maxIdx): #해당 소수의 배수를 전체 OUT 시킨다. -> 이부분 좀 더 빠르게 짤 수 있을듯.
        if cnt % i == 0:
            prime_board[cnt] = 0
answer = 0
for ar in arr:
    if prime_board[ar] == 1:
        answer += 1
print(answer)