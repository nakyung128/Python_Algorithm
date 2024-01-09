from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    case_num = int(input())
    numbers = list(map(int, input().split()))
    arr_count = Counter(numbers)
    
    max_value = max(arr_count, key=arr_count.get)
    
    print("#%d %d" %(case_num, max_value))