# 계속 메모리 초과가 나길래 이유를 찾아보니까 pypy3로 돌려서였음
# python3으로 돌리니까 됨

import sys
sys.setrecursionlimit(10**9)

def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            # node를 currentNode의 자식으로 추가
            childs[currentNode].append(node)
            # node의 부모를 currentNode로 설정
            parents[node] = currentNode
            makeTree(node, currentNode)

def countSubtreeNodes(currentNode):
    # 자신도 자신을 루트로 하는 서브 트리에 포함되므로 0이 아닌 1에서 시작
    size[currentNode] = 1
    for node in childs[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]

# 입력 받기
N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
childs = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
size = [0 for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

makeTree(R, -1)
countSubtreeNodes(R)

for _ in range(Q):
    i = int(sys.stdin.readline())
    print(size[i])