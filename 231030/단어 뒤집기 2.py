import sys
input = sys.stdin.readline

stack = ""
answer = ""
isTag = False # 태그인지 아닌지 여부

# 문자열 입력받기
arr = list(input().rstrip())

for char in arr:
    # 태그가 아닌 경우 뒤집어서 출력
    if isTag == False:
        if char == "<":
            isTag = True
            stack += char # 태그 시작이니까 그대로 넣어주기
        elif char == " ":
            stack += char # 띄어쓰기는 그대로 넣어 주기
            answer += stack # 정답 문자열에 넣어 주기
            stack = "" # 스택은 다시 비우기
        else:
            # 거꾸로 들어가도록 새로운 char + 기존 stack
            stack = char + stack
    # 태그인 경우 똑바로 출력
    else:
        stack += char # 그대로 넣어 주기
        if char == ">": # 태그 끝나면
            isTag = False
            answer += stack # 정답에 스택 문자열 추가
            stack = "" # 스택 비우기

# 마지막 공백 뒤 일반 문자열은 stack에 남아 있으므로 answer+stack 해 주기
print(answer+stack)