from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# BFS
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i] # 헹
            ny = y + dy[i] # 열

            # 범위 벗어난 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽인 경우
            if graph[nx][ny] == 0:
                continue
            
            # 갈 수 있는 곳이면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    return graph[N-1][M-1]

print(bfs(0, 0))
