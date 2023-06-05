array = []

def dfs():
    if len(array) == M:
        print(*array)
        return
    for i in range(1, N+1):
        if i not in array:
            array.append(i)
            dfs()
            array.pop()

N, M = map(int, input().split())

dfs()