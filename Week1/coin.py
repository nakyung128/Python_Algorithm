money = 1260 # 거스름돈
result = 0 # 동전 개수

coin = [500, 100, 50, 10]

for i in coin:
    result += money // i
    money %= i

print(result)