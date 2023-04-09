# 세로 길이 N, 가로 길이 M
N, M = map(int, input().split())

count = 0 # 결과값

# 2차원 배열 입력받기
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 틀에서 벗어나면 False 반환해 주기
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    elif graph[x][y] == 0:
        graph[x][y] = 1 # 방문
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우     
        return True    
    return False # 값이 1인 칸일 때 False

# 탐색
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1

print(count)