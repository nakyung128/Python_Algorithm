import sys

n = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

# 해당 상자에 넣을 수 있는 최대 상자의 개수
# dp list 초기화
dp = [ 1 for _ in range(n) ]

# 2중 for문
for i in range(1, n):
    # 현재 상자보다 앞에 있는 상자들
    for j in range(i):
        # 앞의 상자 크기가 더 작으면
        if boxes[i] > boxes[j]:
            # dp 배열 비교해서 더 큰 값 넣어주기
            dp[i] = max(dp[i], dp[j]+1)

# 최댓값 출력해 주기
print(max(dp))