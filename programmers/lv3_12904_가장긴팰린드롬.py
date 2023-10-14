def palindrome(s, l, r):
    if r - l == 1:
        length = 0
    else:
        length = 1

    while l >= 0 and r < len(s):  # 처음 시작한 l, r에서 좌 우로 확장하면서 palindrome 확인
        if s[l] == s[r]:
            l -= 1
            r += 1
            length += 2
        else:
            break

    return length


def solution(s):
    answer = 1  # 2 이상의 팰린드롬이 없으면, 1이 제일 크다

    if len(s) == 1 or s == s[::-1]:
        return len(s)

    for i in range(len(s) - 1):  # 0~1, 0~2, 1~2, 1~3 ...
        answer = max(answer, palindrome(s, i, i + 1), palindrome(s, i, i + 2))

    return answer
