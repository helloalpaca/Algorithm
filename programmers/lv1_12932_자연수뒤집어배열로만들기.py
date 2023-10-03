# return list(map(int, reversed(str(n)))) << 다른 사람 풀이에 이거 좋은듯

def solution(n):
    return [(n//(10**i))%10 for i in range(len(str(n)))]