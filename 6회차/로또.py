### BOJ 6603

# 라이브러리 사용
from itertools import *

while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    S = lst[1:]

    if k == 0:
        break

    lotto = combinations(S, 6)
    for i in lotto:
        print(*i)
    print()

# 재귀 (dfs)
def dfs(lotto, idx):
    if len(lotto) == 6:
        print(*lotto)
        return
    for i in range(idx, k):
        lotto.append(S[i])
        dfs(lotto, i+1)
        lotto.pop()

while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    S = lst[1:]
    lotto = []

    if k == 0:
        break
    dfs(lotto, 0)
    print()