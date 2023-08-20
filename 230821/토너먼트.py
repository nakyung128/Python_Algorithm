# BOJ 1057
import sys

n, jimin, hansu = map(int, sys.stdin.readline().split())
answer = 0

# 둘은 무조건 이기기 때문에 무조건 붙을 거라 -1 하는 경우는 냅다 버려버림 ㅎㅎ
def round(a, b):
    global answer

    while a != b:
        answer += 1

        a -= a//2
        b -= b//2

    return answer

print(round(jimin, hansu))