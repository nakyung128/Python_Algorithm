### 어라 라이브러리가 되네?
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for i in range(1, n+1):
    numbers.append(i)

for per in permutations(numbers):
    print(*per)