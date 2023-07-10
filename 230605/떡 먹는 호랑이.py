### BOJ 2502
D, K = map(int, input().split())

dp = [0 for _ in range(D)]
dp[0], dp[1] = 1, 1 # 일단 초기값은 1, 1로 설정

while(True):
    for i in range(2, D):
        dp[i] = dp[i-1] + dp[i-2]

    if dp[D-1] == K:
        print(dp[0])
        print(dp[1])
        break
    # 결과가 K보다 크다면 새로운 경우의 수
    # A를 1 증가시켜주기
    elif dp[-1] > K:
        dp[0] += 1
        dp[1] = dp[0]
    # 결과가 K보다 작다면 B를 1 증가시키기
    # A와 B의 차이를 크게 만들어 주어야 함 -> 그래야 다음 숫자가 커짐
    else:
        dp[1] += 1
        