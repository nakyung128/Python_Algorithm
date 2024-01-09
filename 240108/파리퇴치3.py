T = int(input())

def out(graph, n, m):
    answer = []
    for i in range(n):
        for j in range(n):
            bugs = 0
            # + 형태
            bugs += graph[i][j]
            for x in range(1, m):
                if i-x >= 0:
                    bugs += graph[i-x][j]
                if i+x < n:
                    bugs += graph[i+x][j]
                if j-x >= 0:
                    bugs += graph[i][j-x]
                if j+x < n:
                    bugs += graph[i][j+x]
            answer.append(bugs)
            # x 형태
            bugs = 0
            bugs += graph[i][j]
            for x in range(1, m):
                if i-x >= 0 and j-x >= 0:
                    bugs += graph[i-x][j-x]
                if i+x < n and j+x < n:
                    bugs += graph[i+x][j+x]
                if i+x < n and j-x >= 0 :
                    bugs += graph[i+x][j-x]
                if i-x >= 0 and j+x < n:
                    bugs += graph[i-x][j+x]
            answer.append(bugs)
    return max(answer)

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    print("#%d %d" %(test_case, out(graph, n, m)))