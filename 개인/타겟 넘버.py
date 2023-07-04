numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target):
    leaves = [0] # 모든 계산 결과를 담기
    count = 0

    for num in numbers:
        tmp = []
        
        # 자손 노드
        for leaf in leaves:
            tmp.append(leaf + num)
            tmp.append(leaf - num)

        leaves = tmp
    
    # 모든 경우의 수 계산 후 target과 같은지 확인
    for leaf in leaves:
        if leaf == target:
            count += 1

    return count

print(solution(numbers, target))