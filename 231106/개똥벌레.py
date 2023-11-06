import sys
input = sys.stdin.readline

### 메모리 초과
# cave = [[0]*N for _ in range(H)]

# # 장애물 세우기
# for i in range(N):
#     block = int(input())
#     # 짝수 번째 장애물은 아래서부터, 홀수 번째는 위에서부터
#     if i % 2 == 0:
#         for j in range(block):
#             cave[j][i] = 1
#     else:
#         for j in range(H-1, H-block-1, -1):
#             cave[j][i] = 1

# answer_arr = [] # 각 칸마다 파괴해야 하는 장애물 개수 배열
# answer = 0 # 파괴해야 하는 장애물의 최솟값
# count = 0 # 그러한 구간의 수

# # 각 행마다 1의 개수 세기 (부숴야 하는 장애물)
# for i in range(H):
#     cnt = 0
#     for j in range(N):
#         if cave[i][j] == 1:
#             cnt += 1
#     answer_arr.append(cnt)

# answer = min(answer_arr)

# # 구간 수 세기
# for ans in answer_arr:
#     if ans == answer:
#         count += 1

# print(answer, count)

### 정답
N, H = map(int, input().split())
top = [0] * (H+1) # 종유석
bottom = [0] * (H+1) # 석순
result = []
count = 0 # 구간 개수
min_count = N # 최소 장애물 개수

for i in range(N):
    # 석순
    if i % 2 == 0:
        bottom[int(input())] += 1
    # 종유석
    else:
        top[int(input())] += 1

# 거꾸로 계산 (누적합)
for i in range(H-1, 0, -1):
    bottom[i] += bottom[i+1]
    top[i] += top[i+1]

# 장애물 최솟값 찾기
for i in range(1, H+1):
    hap = bottom[i]+top[-i]      
    result.append(hap)          
    if min_count > hap:
        min_count = hap

# 같은 구간의 수 세기
for i in range(H):
    if result[i] == min_count:
        count += 1

print(min_count, count)