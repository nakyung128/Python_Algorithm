import sys
from collections import Counter

# n주 동안의 매주 상위 m명의 랭킹 정보
while True:
    rank = []
    answer = []
    n, m = map(int, sys.stdin.readline().split())

    # 0, 0 입력받으면 종료
    if n == 0 and m == 0:
        break

    # 여러 줄 한 배열에 다 받아주기
    for _ in range(n):
        rank += list(map(int, sys.stdin.readline().split()))

    # 카운트 하고 내림차순으로 정렬
    sorted_count = sorted(Counter(rank).items(), key=lambda x: x[1], reverse=True)
    answer.append(sorted_count[1][0])

    # 동점도 answer 배열에 넣어주기
    for i in range(2, len(sorted_count)):
        if sorted_count[i][1] != sorted_count[1][1]:
            break
        else:
            answer.append(sorted_count[i][0])

    # 출력
    print(*sorted(answer))