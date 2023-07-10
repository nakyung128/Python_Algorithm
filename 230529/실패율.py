N = int(input())
stages = list(map(int, input().split()))
answer = []
fail_perc = {}

# 실패율 계산하여 딕셔너리에 추가
for stage in range(1, N+1):    
    peoples = len(stages)
    # 스테이지 번호가 있으면
    if stage in stages:
        rm = {stage}
        fail = stages.count(stage)
        percent = fail / peoples
        fail_perc[stage] = percent
        # 해당 숫자 모두 지워줌 (리스트 컴프리헨션 활용)
        stages = [j for j in stages if j not in rm]
    else:
        # 없으면 실패율 0
        fail_perc[stage] = 0

# value값 기준 내림차순 정렬 (람다 이용)
fail_perc = dict(sorted(fail_perc.items(), key=lambda item:item[1], reverse=True))

# 따로 실패율 같을 경우 stage 오름차순 안 해 준 이유
# 어차피 작은 스테이지 순서대로 확인하고 딕셔너리에 넣기 때문에 해 줄 필요가 없음
# key값 answer 배열에 넣기
for key in fail_perc.keys():
    answer.append(key)

print(answer)