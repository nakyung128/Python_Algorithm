import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#cnt = 0

# # 파이프가 가로인지 세로인지 대각선인지 -> 가로: 0, 세로: 1, 대각선: 2
# # x: 파이프 시작점, y: 파이프 끝점

# ### 1. dfs 풀이 (시간 초과)
# def dfs(x, y, pipe):
#     global cnt
#     if x == n-1 and y == n-1:
#         cnt += 1
#         return
    
#     # 파이프가 가로일때
#     if 0 <= x < n and 0 <= y+1 < n and graph[x][y+1] == 0 and pipe != 1:
#         # 가로로 이동
#         dfs(x, y+1, 0) 
#     if 0 <= x+1 < n and 0 <= y < n and graph[x+1][y] == 0 and pipe != 0:
#         # 세로로 이동
#         dfs(x+1, y, 1)
#     if 0 <= x+1 < n and 0 <= y+1 < n and graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
#         dfs(x+1, y+1, 2)

# dfs(0, 1, 0)
# print(cnt)


### dp 풀이
# 배열에 x, y 좌표와 파이프의 상태 (가로, 세로, 대각선)를 저장하기 위해 3차원 배열 선언
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# 0: 가로, 1: 세로, 2: 대각선
dp[0][0][1] = 1
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
    for j in range(1, n):
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
            # 대각선 놓기
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        if graph[i][j] == 0:
            # 가로 놓기
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]

            # 세로 놓기
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])
