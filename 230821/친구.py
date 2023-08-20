# BOJ 1058
# 어딘가를 거쳐가는 문제는 플로이드-워셜
import sys

n = int(sys.stdin.readline())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
friends = [[0] * n for _ in range(n)]

# 서로 친구 또는 k 친구를 거친 한 다리 건너 친구이면 2-친구
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: # 본인이니까 continue
                continue 
            if graph[i][j] == "Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
                friends[i][j] = 1

answer = 0

# 각 행의 합 -> 친구수
for i in friends:
    answer = max(answer, sum(i))

print(answer)