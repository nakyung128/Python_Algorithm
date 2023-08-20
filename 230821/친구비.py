# BOJ 16562
# 분리 집합
import sys

n, m, k = map(int, sys.stdin.readline().split()) # 학생 수, 친구 관계 수, 가지고 있는 돈
money = [0] + list(map(int, sys.stdin.readline().split())) # 친구비
parent = [i for i in range(n+1)]

answer = 0

# 부모 노드 찾기
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return p
    
# 두 부모 노드를 합치기
def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        # 합칠 때 비용 적게 드는 애를 root로 설정해 주기
        if money[a] > money[b]:
            parent[a] = b
        else:
            parent[b] = a

# 친구 관계 만들기
for _ in range(m):
    v, w = map(int, sys.stdin.readline().split())
    union(v, w)

# 최소 비용 친구 찾아내기
for idx in range(n+1):
    if idx == parent[idx]:
        answer += money[idx]

if answer > k:
    print("Oh no")
else:
    print(answer)