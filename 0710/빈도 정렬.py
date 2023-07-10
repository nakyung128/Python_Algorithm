# 등장 횟수 세는 기능 제공하는 라이브러리 Counter import
from collections import Counter

# 결과 넣을 배열
result = []

# 입력받기
N, C = map(int, input().split())
lst = list(map(int, input().split()))

# 람다식으로 내림차순 정렬
lst = sorted(Counter(lst).items(), key=lambda x: x[1], reverse=True)

for item in lst:
    for i in range(item[1]):
        result.append(item[0])

# 리스트 출력
print(*result)