### 1이 될 때까지
# n과 k 입력받기
n, k = map(int, input().split())
result = 0 # 횟수

# 반복하기
while True:
    if n == 1: # n이 1이 된 경우
        print(result) # 출력 후 반복문 탈출
        break
    if n % k != 0: # k가 n으로 나뉘어지지 않는 경우
        result += 1 
        n -= 1 # 나뉘어지는 수가 될 때까지 1을 빼 준다.
    else: # k가 n으로 나뉘어지는 경우
        result += 1
        n //= k # n을 k로 나누어 준다.