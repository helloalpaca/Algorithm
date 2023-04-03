from collections import deque

def BFS(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        print(node, end=" ")
        for adj in graph[node]:
            if visited[adj] == False:
                q.append(adj)
                visited[adj] = True



graph = [[],[2,3,8], [1,7], [1,4,5], [3,5] ,[3,4], [7], [2,6,8], [1,7]]
visited = [False] * 9
BFS(graph, 1, visited)