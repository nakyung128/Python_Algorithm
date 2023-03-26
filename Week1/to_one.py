# n과 k 입력받기
n, k = map(int, input().split())
result = 0

while True:
    if n < k:
        while n > 1:
            result += 1
            n -= 1
        print(result)
        break
    if n == 1:
        print(result)
        break
    if n % k != 0:
        result += 1
        n -= 1
    else:
        result += 1
        n //= k