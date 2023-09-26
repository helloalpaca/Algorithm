# 테스트 페이지

from collections import deque

d = deque([])
# print(d[-1]) #안됨

p = []
# print(p[-1]) #안됨

car = [[3, 2],
 [4, 2],
 [5, 2]]

print(list(zip(*car))[0])