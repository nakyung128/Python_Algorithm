import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(sys.stdin.readline())
    # 점수 입력
    scores = [list(map(int, input().split())) for _ in range(2)]

    # 2열 이상인 경우 대각선 먼저 더해 주기
    if n >= 2:
        scores[0][1] += scores[1][0]
        scores[1][1] += scores[0][0]

    for i in range(2, n):
        # 대각선 점수랑, 한 칸 건너 뛴 대각선 점수 중에 큰 것을 더해 준다
        scores[0][i] += max(scores[1][i-1], scores[1][i-2])
        scores[1][i] += max(scores[0][i-1], scores[0][i-2])

    # 윗줄 시작, 아랫줄 시작 중에 더 큰 점수 출력
    print(max(scores[0][n-1], scores[1][n-1]))