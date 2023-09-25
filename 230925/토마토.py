import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])
days = 0

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        # 첫 토마토
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 익지 않은 토마토면
                if tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = tomatos[x][y] + 1
                    q.append([nx, ny])
# 돌려돌려
bfs()

for row in tomatos:
    for col in row:
        if col == 0:
            print(-1)
            exit(0)
    days = max(days, max(row))

print(days-1)