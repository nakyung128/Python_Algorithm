# recursion error 해결 코드
# recursion error: 1000번 이상의 recursion이 발생하면 에러가 뜬다.
import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())
    # 양방향으로 추가해 주기
    graph[i].append(j)
    graph[j].append(i)

def dfs(root):
    for node in graph[root]:
        # 부모 아직 못 찾았으면
        if parents[node] == 0:
            parents[node] = root
            dfs(node)

dfs(1)

for i in range(2, N+1):
    print(parents[i])