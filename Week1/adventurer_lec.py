n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도가 낮은 것부터 하나씩 확인
    count += 1 # 현재 그룹에 모험가 한 명씩 포함
    if count >= i: # 만약 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면
        result += 1 # 그룹 결성
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result) # 총 그룹의 수 출력