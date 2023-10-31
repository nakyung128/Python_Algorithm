import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 나이트가 이동할 수 있는 칸 탐색
        for i in range(8):
            nx = x + dx[i]
            ny  = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1

T = int(input()) # 테스트케이스의 개수

for _ in range(T):
    I = int(input())

    graph = [[0]*I for _ in range(I)]
    visited = [[False]*I for _ in range(I)]

    nowX, nowY = map(int, input().split())
    goX, goY = map(int, input().split())

    if nowX == goX and nowY == goY: # 현재 위치와 이동하려는 위치가 같은 경우 0 출력
        print(0)
    else:
        bfs(nowX, nowY)
        print(graph[goX][goY])