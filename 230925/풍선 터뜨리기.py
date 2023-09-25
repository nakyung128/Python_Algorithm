import sys
from collections import deque

n = int(sys.stdin.readline())
# 튜플로 인덱스 받기
deq = deque(enumerate(map(int, sys.stdin.readline().split())))
answer = []

while deq:
    index, balloon = deq.popleft() # 인덱스, 풍선 번호
    answer.append(index + 1)

    # 이미 한번 pop 했으니까 숫자-1만큼만 Rotate
    if balloon > 0:
        deq.rotate(-(balloon-1))
    # 음수면 왼쪽으로
    else:
        deq.rotate(-balloon)

print(*answer)