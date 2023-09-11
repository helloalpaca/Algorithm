from collections import deque


def dfs(x, y, n):
    q = deque([x])
    visited = [0] * (y + 1)
    while q:
        now = q.popleft()
        for nxt in [now + n, 2 * now, 3 * now]:
            if nxt <= y and (not visited[nxt] or visited[nxt] > visited[now] + 1):
                visited[nxt] = visited[now] + 1
                q.append(nxt)
    return visited[y]


def solution(x, y, n):
    if x == y:
        return 0
    answer = dfs(x, y, n)
    if answer == 0:
        answer = -1
    return answer