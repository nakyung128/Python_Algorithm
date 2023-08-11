import sys

# 총 입력받을 걸그룹의 수 n
# 맞혀야 할 문제의 수 m
n, m = map(int, sys.stdin.readline().split())
group = "" # 그룹명
num = 0 # 멤버 수

groups = {} # 그룹 담을 dictionary

for _ in range(n):
    members = []
    group = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline())
    for _ in range(num):
        members.append(sys.stdin.readline().rstrip())
    # 그룹 딕셔너리에 그룹이름 : 멤버들 추가
    groups[group] = members

question = {} # 문제 딕셔너리

for _ in range(m):
    fir = sys.stdin.readline().rstrip()
    sec = int(sys.stdin.readline())
    question[fir] = sec

for q in list(question.keys()):
    if question[q] == 1:
        for k, v in groups.items():
            if q in v:
                print(k)
    else:
        # 멤버 이름 순서대로 출력
        for i in sorted(list(groups[q])):
            print(i)