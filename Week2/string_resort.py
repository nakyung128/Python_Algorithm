### 문자열 재정렬

string = input()

string_arr = []
number_arr = []

result = ""
hap = 0

for i in string:
    if i >= 'A' and i <= 'Z':
        string_arr.append(i)
    else:
        number_arr.append(int(i))

string_arr.sort() # 정렬

for i in number_arr:
    hap += i

for i in string_arr:
    result += i

result += str(hap)
print(result)