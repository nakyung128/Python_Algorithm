import sys

n, m = map(int, sys.stdin.readline().split())
array = []
answer = []

def dfs(num):
    if len(array) == m:
        print(*array)
        return          
    for i in range(num, n+1):
        if i not in array:
            array.append(i)
            # 중복이 없어야 하므로 (앞자리 수가 뒷자리보다 더 큰 경우는 X)
            # 하나 더 큰 수부터 dfs 돌리기
            dfs(i+1)
            array.pop()
dfs(1)