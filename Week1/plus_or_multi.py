### 곱하기 혹은 더하기
# 대부분의 경우 + 보다는 x가 값을 더 크게 만들기 때문에 웬만하면 곱하기 해 주기
# 하지만 두 수 중에서 하나라도  0 혹은 1인 경우 곱하기보다 더하기를 수행하는 것이 효율적임
# 따라서 두 수에 대해 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱하기

number = input()
result = int(number[0]) # 첫 번째 숫자 먼저 담아놓기

for i in range(1, len(number)): # 두 번째부터 반복문 돌리기
    num = int(number[i])
    if (result <= 1 or num <= 1): # 첫 번째 숫자 or 두 번째 숫자가 1 이하인 경우에는 더하기
        result += num
    else: # 아니면 곱하기
        result *= num

print(result)