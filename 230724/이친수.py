# dp (dynamic programming) 문제
import sys

dp = [0, 1, 1]

for i in range(3, 91):
    dp.append(dp[i-1] + dp[i-2])

N = int(sys.stdin.readline())

print(dp[N])
