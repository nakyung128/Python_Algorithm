### 모험가 길드

n = int(input()) # 모험가 수 n
scared = list(map(int, input().split())) # 각 모험가의 공포도 값 리스트 scared
scared.sort() # 오름차순 정렬
result = 0 # 최대값 (결과)
big = False # 길드에 본인보다 공포도 큰 사람이 있는가 확인

while len(scared) > 0:
    score = scared[0] 
    guild = scared[:score]
    # 길드에 본인보다 공포도가 큰 사람이 있는지 확인한다
    for i in range(1, len(guild)):
        if guild[i] > score:
            big = True # 있으면 True로 변경
        else: continue
    # 공포도가 큰 사람이 있으면 반복문 중지
    if big == True:
        break
    else: # 없으면 길드 결성, result에 1 더하기
        scared = scared[score:]
        result += 1

# while문이 종료되면 결과 출력
print(result)