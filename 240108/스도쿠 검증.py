T = int(input())

def verification(sudoku):
    # 같은 줄에 겹치는 숫자 없는지 확인 (가로, 세로)
    for i in range(9):
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            row_number = sudoku[i][j]
            col_number = sudoku[j][i]

            # 가로
            row[row_number] += 1
            if row[row_number] == 2:
                return False
            
            #세로
            col[col_number] += 1
            if col[col_number] == 2:
                return False      
            
    # 3x3 겹치는 숫자 없는지 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr_3 = [0] * 10
            for x in range(3):
                for y in range(3):
                    arr_3[sudoku[i+x][j+y]] += 1
                    if arr_3[sudoku[i+x][j+y]] == 2:
                        return False
    
    return True


for test_case in range(1, T+1):
    sudoku = []

    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    if verification(sudoku):
        print("#%d %d" %(test_case, 1))
    else:
        print("#%d %d" %(test_case, 0))