from collections import deque
import copy

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 결과
result = 0

# 바이러스 전염
def bfs():
    global result
    queue = deque()
    new_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                queue.append((nx, ny))
    count = 0
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 0:
                count += 1
    result = max(count, result)


# 벽 세우기
def wall(count):
    # 벽 세 개 세웠으면
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count+1)
                graph[i][j] = 0

wall(0)
print(result)