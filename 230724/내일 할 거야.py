import sys

n = int(sys.stdin.readline())
assignment = []

for _ in range(n):
    d, t = map(int, sys.stdin.readline().split())
    assignment.append([d, t])

# 마감 날짜 내림차순 정렬
assignment.sort(key=lambda x:x[1], reverse=True)

# 마지막 과제 무조건 해야 하는 날에 하고 남는 날
day = assignment[0][1] - assignment[0][0] + 1

# 반복문
for i in range(1, len(assignment)):
    # 남은 날이 두 번째 과제 마감 기한보다 뒤인 경우
    if assignment[i][1] < day:
        # 남은 날 앞으로 땡겨 주기
        day = assignment[i][1] - assignment[i][0] + 1
    else:
        day = day - assignment[i][0]

print(day-1)