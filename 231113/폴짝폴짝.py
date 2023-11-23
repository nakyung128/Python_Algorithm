from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
bridge = [0] + list(map(int, input().split()))
start, end = map(int, input().split())

# 도착지점이 현재 위치보다 앞에 있을 수도 있음
# 앞뒤로 탐색해야 한다 (양쪽으로)
def bfs(x, y):
    queue = deque()
    queue.append(x) # 맨 처음 위치 추가해 주기

    # 횟수 세는 용도
    visited = [-1] * (N+1)
    visited[x] = 0

    while queue:
        now = queue.popleft()
        # 오른쪽으로 탐색
        for i in range(now, N+1, bridge[now]):
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)
                if i == y:
                    return visited[i]
        # 왼쪽으로 탐색
        for i in range(now, 0, -bridge[now]):
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)
                if i == y:
                    return visited[i]
    # 못 찾음
    return -1

print(bfs(start, end))