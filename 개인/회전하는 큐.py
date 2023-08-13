# BOJ 1021
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
locations = list(map(int, sys.stdin.readline().split()))

# 양방향 큐
queue = deque([i for i in range(1, n+1)])
count = 0
i = 0

while i < m:
    if queue[0] == locations[i]:
        queue.popleft()
        i += 1
        continue
    else:
        where = 0
        # 뽑아내려고 하는 수의 현재 위치 탐색
        for q in queue:
            if q == locations[i]:
                break
            else:
                where += 1
        # 현재 위치가 큐의 길이//2보다 작거나 같으면 앞으로 옮겨주는 게 빠르다
        if where <= len(queue)//2:
            # 왼쪽으로 한 칸 이동 (2번)
            queue.append(queue.popleft())
            count += 1           
        else:
            # 오른쪽으로 한 칸 이동 (3번)
            queue.appendleft(queue.pop())
            count += 1
print(count)