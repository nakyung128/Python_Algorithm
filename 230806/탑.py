import sys

n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0 for _ in range(len(tops))]

### 스택으로 풀기 (정답)
for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:
            answer[i] = stack[-1][0]
            break
        else:
            stack.pop()
    # 스택에 아무것도 없을 때
    stack.append([i+1, tops[i]])

print(*answer)

### 시간초과 (그냥 구현)
# i = len(tops)-1
# j = 1
# cnt = 0

# while i > 0:
#     # 앞에 더 없으면 i 줄여주고 continue
#     if i-j < 0:
#         i -= 1
#         continue
#     # 나보다 큰 탑이 앞에 있으면 그 위치에 전송되는 것
#     if tops[i] <= tops[i-j]:
#         answer[i] = i-j+1
#         i -= 1
#         j = 1
#     # 없으면 더 앞에 것으로 가게 j += 1
#     else:
#         j += 1

# print(*answer)