def DFS(graph, v, visited):
    print(v, end=" ")
    visited[v] = True
    for adj in graph[v]:
        if visited[adj] == False:
            DFS(graph, adj, visited)


graph = [[],[2,3,8], [1,7], [1,4,5], [3,5] ,[3,4], [7], [2,6,8], [1,7]]
visited = [False] * 9
DFS(graph, 1, visited)