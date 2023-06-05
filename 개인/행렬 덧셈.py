### 행렬 덧셈 Bronze 5

n, m = map(int, input().split())

a = []
b = []
hap = []
total = []
result = ""

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    hap = []
    for j in range(m):
        hap.append(a[i][j] + b[i][j])
    total.append(hap)

for i in range(n):
    result = ""
    for j in range(m):
        result += str(total[i][j]) + " "
    print(result)