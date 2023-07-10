### 안테나 - 실버 3
# 시간초과
N = int(input())
houses = list(map(int, input().rstrip().split()))
distance = {}

# 나중에 거리 같으면 집 숫자 작은 거 출력해 줘야 하니까 미리 오름차순 정렬
houses = sorted(houses)

for house in houses:
    hap = 0
    for dis in houses:
        hap += abs(house-dis)
    distance[house] = hap

# key, value 뒤집기
# 거리가 같은 집 5가 사라지게 됨
# reverse_dict = dict(map(reversed, distance.items()))

# 반복문
for key, value in distance.items():
    if value == min(distance.values()):
        print(key)
        break