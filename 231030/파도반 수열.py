import sys
input = sys.stdin.readline

T = int(input())

P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    P.append(P[i-1] + P[i-5])

for _ in range(T):
    N = int(input())
    print(P[N])