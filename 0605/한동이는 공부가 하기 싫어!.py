### BOJ 3182

N = int(input())

# 선배들 번호가 1부터 시작하니까 앞에 하나 추가해 주기
sunbae = [0]
result = [0]

# 선배 대답 입력
for _ in range(N):
    sunbae.append(int(input()))

def dfs(start):
    visited[start] = True # 방문
    if not visited[sunbae[start]]: # 해당 선배 방문하지 않았으면
        dfs(sunbae[start]) # 재귀

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i) # 1부터 (첫 번째 선배부터)
    result.append(visited.count(True)) # 몇 명에게 방문했는지 result 배열에 추가

print(result.index(max(result))) # 가장 큰 방문수를 갖고 있는 인덱스 번호 출력하기 (인덱스 번호 = 선배 번호)
