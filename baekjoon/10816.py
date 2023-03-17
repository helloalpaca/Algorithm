import math

def binary_search(li, target):
    start = 0
    end = len(li)-1

    while start <= end:
        mid = math.floor((start+end)/2)
        if li[mid] == target:
            return True
        elif li[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return False

def solution(N, cards, K, numbers):
    answer = [0 for i in range(K)]
    card_dic = {}

    #dictionary 자료형에 card의 개수를 저장 => ex) {10 : 3, -10 : 2}
    for i in range(N):
        if cards[i] in card_dic:
            card_dic[cards[i]]+=1
        else:
            card_dic[cards[i]]=1

    cards_key = list(card_dic.keys())
    cards_key.sort()

    for i in range(K):
        if binary_search(cards_key, numbers[i]):
            answer[i] = card_dic[numbers[i]]

    return ' '.join(map(str, answer))

if __name__ == '__main__':
    N = int(input())
    cards = list(map(int, input().split()))


    K = int(input())
    numbers = list(map(int, input().split()))

    print(solution(N,cards, K, numbers))
