import itertools

numbers = [6, 10, 2]

### 시간초과
# def solution(numbers):
#     number = []
#     for i in itertools.permutations(numbers):
#         number.append(''.join(map(str, i)))
#     return max(number)  

def solution(numbers):
    # list 문자로 변경
    number_list = list(map(str, numbers))
    
    # 내림차순 정렬
    # 람다식 사용
    number_list.sort(key = lambda x:x*3, reverse=True)
    
    return str(int(''.join(number_list)))