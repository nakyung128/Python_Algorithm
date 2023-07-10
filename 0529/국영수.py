### 국영수 (BOJ 10825) - 실버 4
import sys

# 학생의 수
N = int(sys.stdin.readline())
scores = []

# 이름과 점수 입력받기
for _ in range(N):
    scores.append(sys.stdin.readline().split())

# 람다식 이용하기
# 1. 국어 점수가 감소하는 순서 (내림차순)
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서 (오름차순)
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서 (내림차순)
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서 (오름차순)
scores.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 이름 출력
for score in scores:
    print(score[0])