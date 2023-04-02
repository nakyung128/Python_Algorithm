### 문자열 압축

s = input()
repeat = "" # 압축된 문자열을 담을 repeat
result = [] # 압축된 문자열의 길이를 담을 배열

# 문자열 i개씩 자르기
for i in range(1, len(s)//2+1): # 최대 반만큼 자를 수 있으니까 범위를 len(s)//2+1로 설정
    repeat = ""
    count = 1
    alp = s[:i] # 몇 번 반복되는지 확인하기 위해 i만큼 자른 문자열을 담아 준다.

    # 몇 번 반복되는지 확인. step을 i로 설정해 줬다.
    for j in range(i, len(s)+i, i):
        if alp == s[j:j+i]:
            count += 1
        else:
            if count > 1:
                string = str(count) + alp
                repeat += string
            else:
                repeat += alp
          
            alp = s[j:j+i] # 다음으로 잘리는 문자열 담아 주기.
            count = 1
    result.append(len(repeat)) # 압축된 문자열의 길이를 배열에 추가    

print(min(result)) # 가장 작은 수 출력하기