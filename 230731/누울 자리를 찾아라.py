import sys

n = int(sys.stdin.readline())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

# 가로 누울 자리 개수
def total_row(graph):
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    total += 1
                cnt = 0
        if cnt >= 2:
            total += 1

    return total

# 세로 누울 자리 개수
def total_col(graph):
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[j][i] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    total += 1
                cnt = 0
        if cnt >= 2:
            total += 1

    return total

print(total_row(graph), total_col(graph))