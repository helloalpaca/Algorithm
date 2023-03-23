#다익스트라 알고리즘
#시간복잡도 O(N**2)
#선형탐색

import sys

num = 6
INF = sys.maxsize

a = [[0, 2, 5, 1, INF, INF],
     [2, 0, 3, 2, INF, INF],
     [5, 3, 0, 3, 1, 5],
     [1, 2, 3, 0, 1, INF],
     [INF, INF, 1, 1, 0, 2],
     [INF, INF, 5, INF, 0, 2]]

v = [0 for i in range(num)] #visited

def getSmallerIndex(d):
    idx = 0
    val = INF
    for i in range(num):
        if d[i]<val and v[i]==0:
            idx = i
            val = d[i]
    return idx

def djikstra(start):
    d = a[start] #distance
    v[start] = 1

    for i in range(num-2):
        cur = getSmallerIndex(d)
        v[cur] = 1
        for j in range(num):
             if v[j] != 1 and d[cur]+a[cur][j] < d[j]:
                 d[j] = d[cur]+a[cur][j]

    return d

print(djikstra(0))