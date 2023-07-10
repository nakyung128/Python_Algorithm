from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)
distance[X] = 0 # 출발 지점은 거리 0으로 해 주기

# 특정 도시에서 갈 수 있는 도시 입력받기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

queue = deque([X])

# bfs
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

# 최단 거리 K인 거 확인하기
check = False
for i in range(N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)