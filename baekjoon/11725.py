import sys
sys.setrecursionlimit(10**6)

def dfs(idx, parents, trees):
    for child in trees[idx]:
        if parents[child] == 0:
            parents[child] = idx
            dfs(child, parents, trees)

def solution(N, edges):
    parents = [0 for i in range(N+1)]
    trees = [[] for i in range(N+1)]
    for i in range(N-1):
        trees[edges[i][0]].append(edges[i][1])
        trees[edges[i][1]].append(edges[i][0])

    dfs(1, parents, trees)

    return parents

if __name__ == '__main__':
    N = int(input())
    edges = []

    for _ in range(N-1):
        edges.append(list(map(int, input().split())))

    answer = solution(N, edges)
    for i in range(2, N+1):
        print(answer[i])