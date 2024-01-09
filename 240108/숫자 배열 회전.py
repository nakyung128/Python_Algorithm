T = int(input())

for test_case in range(1, T + 1):
    arr = []
    n = int(input())
    
    for i in range(n):
        arr.append(list(map(int, input().split())))

    arr_90, arr_180, arr_270 = [], [], []

    #90도
    for i in range(n):
        number_str = ""
        for j in range(n-1, -1, -1):
            number_str += str(arr[j][i])
        arr_90.append(number_str)

    #180도
    for i in range(n-1, -1, -1):
        number_str = ""
        for j in range(n-1, -1, -1):
            number_str += str(arr[i][j])
        arr_180.append(number_str)

    #270도
    for i in range(n-1, -1, -1):
        number_str = ""
        for j in range(n):
            number_str += str(arr[j][i])
        arr_270.append(number_str)

    print("#%d" %test_case)
    # 출력
    for i in range(n):
        print(arr_90[i] + " " + arr_180[i] + " " + arr_270[i])