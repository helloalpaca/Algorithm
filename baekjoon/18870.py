import sys

N = int(input())
points = list(map(int, sys.stdin.readline().rstrip().split()))
temp = sorted(list(set(points)))
dic = {temp[i]: i for i in range(len(temp))}
answer = []

for point in points:
    answer.append(str(dic[point]))

print(' '.join(answer))