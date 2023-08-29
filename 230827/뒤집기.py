import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
answer = 0

# 맨 끝에서부터 거꾸로
for a in range(n-1, -1, -1):
    for b in range(m-1, -1, -1):
        # 뒷면이면 뒤집어야 함
        if graph[a][b] == 1:
            answer += 1
            # 옆에 동전도 뒤집기
            for i in range(a+1):
                for j in range(b+1):
                    if graph[i][j] == 0:
                        graph[i][j] = 1
                    else:
                        graph[i][j] = 0

print(answer)
