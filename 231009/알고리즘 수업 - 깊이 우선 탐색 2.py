import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())

point = [i for i in range(1, n+1)]
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
cnt = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점 번호를 내림차순으로 정렬
sorted_graph = [sorted(sub_arr, reverse=True) for sub_arr in graph]

# 시작 정점 r
def dfs(v, e, r):
    global cnt
    # 시작 정점 방문했다고 표시
    visited[r] = 1
    answer[r] = cnt
    for p in sorted_graph[r]:
        if visited[p] == 0: 
            cnt += 1       
            dfs(v, e, p)

dfs(point, graph, r)

for i in answer[1:]:
    print(i)