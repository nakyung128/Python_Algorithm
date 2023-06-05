### 바이러스 silver3
from collections import deque

computer = int(input()) # 컴퓨터의 개수
N = int(input()) # 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for i in range(computer+1)]
visited = [0] * (computer+1) # 방문했는지 여부

for _ in range(N):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x):
    count = 0
    queue = deque([x])
    visited[1] = 1
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)
                count += 1
    return count 

print(bfs(1))