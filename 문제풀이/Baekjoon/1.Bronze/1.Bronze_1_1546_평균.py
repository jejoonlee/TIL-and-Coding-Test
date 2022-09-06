import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

scores = list(map(int, input().split()))

 
# 제일 큰 값을 구한다 / max_s
max_s = 0

for i in scores:
    if i > max_s:
        max_s = i


# 각 수에 제일 큰 값 나눈 후 100을 곱한다 for문 사용하기
div = []
for i in scores:
    num = (i / max_s) * 100
    div.append(num)

# 나온 수들을 더한 후 과목 개수와 나눈다
result = sum(div) / N

print(result)