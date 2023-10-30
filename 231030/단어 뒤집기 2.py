import sys
input = sys.stdin.readline

answer = ""
isTag = False
stack = ""

arr = list(input().rstrip())

for char in arr:
    # 태그가 아닌 경우 뒤집어서 출력
    if isTag == False:
        if char == "<":
            isTag = True
            stack += char
        elif char == " ":
            stack += char
            answer += stack
            stack = ""
        else:
            # 거꾸로 들어가도록 새로운 char + 기존 stack
            stack = char + stack
    # 태그인 경우 똑바로 출력
    else:
        stack += char
        if char == ">":
            isTag = False
            answer += stack
            stack = ""

print(answer+stack)