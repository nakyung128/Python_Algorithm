### 곱하기 혹은 더하기

number = input()
result = int(number[0]) # 첫 번째 숫자 먼저 담아놓기

for i in range(1, len(number)): # 두 번째부터 반복문 돌리기
    num = int(number[i])
    if (result <= 1 or num <= 1): # 첫 번째 숫자 or 두 번째 숫자가 1 이하인 경우에는 더하기
        result += num
    else: # 아니면 곱하기
        result *= num

print(result)