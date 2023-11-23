import sys
input = sys.stdin.readline

N, P = map(int, input().split())
guitar = [[0] for _ in range(7)]
result = 0

for _ in range(N):
    line, number = map(int, input().split())
    # 눌러야 하는 플렛이 기존에 누르고 있는 가장 큰 플렛보다 큰 경우
    if number > max(guitar[line]):
        # 해당 줄의 누르고 있는 플렛에 추가
        guitar[line].append(number)
        result += 1 # +1회
    # 가장 큰 플렛과 같으면
    elif number == max(guitar[line]):
        continue
    # 가장 큰 플렛보다 작으면
    else:
        index = []
        # 떼야 하는 플렛들
        for i in guitar[line]:
            if i > number:
                index.append(i)
                result += 1 # 떼니까 +1회씩
        # 눌러야 하는 플렛보다 큰 플렛들 다 제거하기
        for idx in index:
            guitar[line].remove(idx)
        # 플렛이 해당 줄에서 기존에 누르고 있는 게 아니라면
        if number not in guitar[line]:
            guitar[line].append(number) # 추가해 주기
            result += 1 # 누르니까 +1회

print(result) 