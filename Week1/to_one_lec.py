n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k # target은 항상 k의 배수가 됨
    result += (n - target)
    n = target

    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
result += (n - 1)
print(result)
