import sys
r, c = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 길에서 세 곳 이상이 빌딩이면 막다른 길임 -> 무조건 유턴
# 모든 길은 근처 길이 2개 이상이어야만 함
def dfs():
    uturn = False
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X":
                continue

            cnt = 0
            # 상하좌우
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == ".":
                        cnt += 1

            if cnt <= 1:
                uturn = True
                break

    if uturn:
        return 1
    else:
        return 0
    

print(dfs())
