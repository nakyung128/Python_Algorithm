T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    idx_cnt = 0

    if n <= m:
        arr_a = list(map(int, input().split()))
        arr_b = list(map(int, input().split()))
        idx_cnt = n
    else:
        arr_b = list(map(int, input().split()))
        arr_a = list(map(int, input().split()))
        idx_cnt = m

    count = abs(n - m)

    answer = []

    for i in range(count+1):
        hab = 0
        for j in range(idx_cnt):
            hab += arr_a[j] * arr_b[j+i]
        answer.append(hab)

    print("#%d %d" %(test_case, max(answer)))

