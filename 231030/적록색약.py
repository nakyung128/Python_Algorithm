import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
colors = [ list(input().rstrip()) for _ in range(N) ]
visited = [ [0]*N for _ in range(N) ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

color_blind = 0
no_color_blind = 0

# 구역 개수 세기
def dfs(x, y):
    visited[x][y] = 1 # 방문
    color = colors[x][y] # 지금 색상

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0:
                if colors[nx][ny] == color:
                    dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            no_color_blind += 1

# 적록색약인 사람이 봤을 때 구역 개수
# 초 -> 빨로 바꿔주기
for i in range(N):
    for j in range(N):
        if colors[i][j] == "G":
            colors[i][j] = "R"

# visited 초기화
visited = [ [0]*N for _ in range(N) ]

# 구역 개수 세기
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            color_blind += 1

print(no_color_blind, color_blind)