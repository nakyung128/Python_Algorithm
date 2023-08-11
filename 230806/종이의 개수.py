import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt_minus, cnt_zero, cnt_one = 0, 0, 0

# 중첩 for문 사용 -> 시간은 더 오래 걸리는 듯
def divide(x, y, n):
    global cnt_minus, cnt_zero, cnt_one
    num = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                # 9개로 분할하기
                for k in range(3):
                    for l in range(3):
                        divide(x + k * n//3, y + l * n//3, n//3)
                return
            
    if num == -1:
        cnt_minus += 1
    elif num == 0:
        cnt_zero += 1
    else:
        cnt_one += 1

divide(0, 0, n)

print(cnt_minus)
print(cnt_zero)
print(cnt_one)


# 분할 부분을 위처럼 중첩 for문으로 바꿈
# def devide(x, y, n):
#     global cnt_minus, cnt_zero, cnt_one
#     num = paper[x][y]
#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if num != paper[i][j]:
#                 # 9개로 분할하기
#                 devide(x, y, n//3)
#                 devide(x, y+n//3, n//3)
#                 devide(x, y+(n//3*2), n//3)
#                 devide(x+n//3, y, n//3)
#                 devide(x+n//3, y+n//3, n//3)
#                 devide(x+n//3, y+(n//3*2), n//3)
#                 devide(x+(n//3*2), y, n//3)
#                 devide(x+(n//3*2), y+n//3, n//3)
#                 devide(x+(n//3*2), y+(n//3*2), n//3)
#                 return
#     if num == -1:
#         cnt_minus += 1
#     if num == 0:
#         cnt_zero += 1
#     if num == 1:
#         cnt_one += 1
#     return

# devide(0, 0, n)

# print(cnt_minus)
# print(cnt_zero)
# print(cnt_one)