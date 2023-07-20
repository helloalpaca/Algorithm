# 최단 거리를 구할 때는 djikstra 알고리즘 사용.
# 1->v1->v2->N, 1->v2->v1->N을 구하고 최솟값을 print

import heapq
import sys

INF = int(1e9)
def djikstra(start):
    distance = [INF for _ in range(N+1)] #1에서 어떤 노드e까지 가는 최단 거리를 저장
    q = [] # q 선언
    heapq.heappush(q, (0, start)) #heapq에 밀어 넣는다. dist, node
    distance[start] = 0 # start -> start의 거리는 0이다.
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 기존 dist가 더 작을 때
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return distance

read = sys.stdin.readline
N, E = map(int, read().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, read().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, read().rstrip().split())
v1_to_v2 = 0
for edge in graph[v1]:
    if edge[0] == v2:
        v1_to_v2 = edge[1]
# print(v1_to_v2)
visited1 = [False for _ in range(N)]
visited2 = [False for _ in range(N)]

d_start = djikstra(1)
d_v1 = djikstra(v1)
d_v2 = djikstra(v2)

answer = min(d_start[v1]+d_v1[v2]+d_v2[N], d_start[v2]+d_v2[v1]+d_v1[N])
print(answer if answer < INF else -1)
