import sys
input = sys.stdin.readline

N = int(input())
list = [0] * 10000

for _ in range(N):
    list[int(input())-1] += 1

for i in range(10000):
    if list[i] != 0:
        for j in range(list[i]):
            print(i+1)