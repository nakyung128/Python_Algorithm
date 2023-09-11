import sys
from collections import deque

# 가로 m, 세로 n
m, n = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0))
visited[0][0] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 아직 방문하지 않았을 때
            if visited[nx][ny] == -1:
                # 벽이 아닐 때
                if miro[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

print(visited[n-1][m-1])