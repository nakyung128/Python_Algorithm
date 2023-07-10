N = int(input())
houses = []
houses = list(map(int, input().rstrip().split()))
houses.sort() # 오름차순 정렬

print(houses[(N-1)//2])