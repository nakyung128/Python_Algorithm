import sys
input = sys.stdin.readline

n = int(input())
str_dict = {} # key: 알파벳, value: 자릿수 총합 담을 딕셔너리 생성
result = 0 # 정답

str_arr = [list(input().rstrip()) for _ in range(n)]

# 단어 자릿수로 10제곱 해 주기
# 세 글자면 첫 번째 자리는 10^2, 두 번째 10^1, 세 번째 10^0
for word in str_arr:
    for i in range(len(word)):
        if word[i] not in str_dict:
            str_dict[word[i]] = 10 ** (len(word) - i - 1)
        else:
            str_dict[word[i]] += 10 ** (len(word) - i - 1)

# 내림차순 해 주기
sorted_arr = sorted(str_dict.items(), key=lambda x: x[1], reverse=True)

# 앞에서부터 값에 9 곱해 주기
start = 9
for i in range(len(sorted_arr)):
    sorted_arr[i] = (sorted_arr[i][0], sorted_arr[i][1] * start)
    start -= 1
    result += sorted_arr[i][1]

print(result)