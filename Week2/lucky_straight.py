### 럭키 스트레이트

number = input()

half = int(len(number)/2)

# 문자열 반으로 가르기
left = number[:half]
right = number[half:]

left_hap = 0
right_hap = 0

# 반복문 돌면서 더해 주기
for i, j in zip(left, right):
    left_hap += int(i)
    right_hap += int(j)

# 합이 같으면 LUCKY 출력, 아니면 READY
if left_hap == right_hap:
    print("LUCKY")
else:
    print("READY")
    