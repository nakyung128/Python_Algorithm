import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
wait = [] # 한 명씩 설 수 있는 공간
order = 1
result = ""

# 첫 번째 실수
# 한 명 대기줄의 첫 번째 번호를 확인하여 해당 번호일 경우 pop해 주어야 함을 간과함

# 두 번째 실수
# 대기줄에 한 명 남아 있는 경우를 생각하지 않음 -> 한 명 남아 있는 경우는 무조건 마지막 번호이므로 Nice

# 찾았던 반례
# 5
# 5 3 1 2 4

while True:
    # 기존 대기줄에 아무도 없으면 break
    if len(numbers) == 0:
         break
    if numbers[0] == order:
        numbers.pop(0)
        order += 1 # 다음 순서
    elif len(wait) != 0 and wait[0] == order:
            wait.pop(0)
            order += 1
    else:
        # 한 명 대기줄 맨 앞에 추가
        wait.insert(0, numbers.pop(0))

# 한 명 씩만 설 수 있는 대기줄 확인
if len(wait) == 0 or len(wait) == 1: # 대기줄에 아무도 없거나 한 명일 때
     result = "Nice"
else: # 대기줄에 여려명 있는 경우
    for i in range(len(wait)-1):
        # 앞 숫자가 뒤 숫자 -1이 아니면
        if wait[i] != wait[i+1]-1:
            result = "Sad"
            break
        else:
            result = "Nice"

print(result)