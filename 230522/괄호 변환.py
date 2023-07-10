# 올바른 괄호 문자열인지 판단하는 함수
def isCorrect(s):
    stack = []
    for i in s:
        # 스택이 비어 있을 때
        if len(stack) == 0:
            if i == ')':
                return False
            else:
                stack.append(i)
        # 스택이 비어 있지 않을 때
        else:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
    # 스택 비어 있으면 올바른 괄호
    if len(stack) == 0:
        return True
    return False

def solution(p):
    answer = ""
    # 1
    if p == "":
        return answer   
    # 2
    u, v = split(p)
    # 3
    if isCorrect(u):
        # 3-1
        return u + solution(v)
    # 4
    else:
        # 4-1
        answer += '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

def split(p):
    left = 0
    right = 0

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1], p[i+1:]
        
p = input()
print(solution(p))