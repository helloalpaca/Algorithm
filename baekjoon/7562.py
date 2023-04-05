from collections import deque
import sys

N = int(input())
for _ in range(N):
    l = int(input())
    x, y = map(int, sys.stdin.readline().split())
    dx, dy = map(int, sys.stdin.readline().split())
    board = [[0 for _ in range(l)] for _ in range(l)]

    mx = [-2, -2, -1, -1, 1, 1, 2, 2]
    my = [-1, 1, -2, 2, -2, 2, -1, 1]

    def BFS(x, y):
        q = deque([(x, y)])
        board[x][y]=0
        while q:
            nx, ny = q.popleft()
            if nx == dx and ny == dy:
                break
            for i in range(8):
                tx=nx+mx[i]
                ty=ny+my[i]
                if 0<=tx<l and 0<=ty<l and board[tx][ty]==0:
                    board[tx][ty]=board[nx][ny]+1
                    q.append((tx, ty))

        return board[dx][dy]
    print(BFS(x, y))