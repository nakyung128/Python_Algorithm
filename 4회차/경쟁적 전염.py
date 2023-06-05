# 가로, 세로
N, K = map(int, input().split())
S, X, Y = map(int, input().split())

graph = []

# 2차원 배열 입력받기
for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= K:
        return False
    elif graph[x][y] != 0:      
        if x-1 < 0 or x + 1 >= N or y-1 < 0 or y+1 >= K:
            graph[x][y] = min(graph[x-1][y], graph[x+1][y], graph[x][y-1], graph[x][y+1])
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        else: return False

for _ in range(S):
    dfs(0, 0)

print(graph[X][Y])