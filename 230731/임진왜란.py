import sys
from itertools import combinations

n = int(sys.stdin.readline())

score = 0

answer = dict(zip(sys.stdin.readline().split(), [i for i in range(n)]))
hyeonwoo = list(map(str, sys.stdin.readline().split()))

com_arr = list(combinations(hyeonwoo, 2))

# 올바른 순서로 적혀 있으면 점수
fir = 0
sec = 0

for com in com_arr:
    fir = answer[com[0]]
    sec = answer[com[1]]
    # index 함수 땜에 시간 초과 그래서 대신 정답을 dictionary로 만들어 줌
    # fir = answer.index(com[0])
    # sec = answer.index(com[1])
    if fir < sec:
        score += 1

print("%d/%d" % (score, n*(n-1)/2))