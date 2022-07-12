# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

num = [0, 20, 100, 50, -60, 50, 100]
max = num[0]                 # 초기값을 'num'의 첫번째 값으로 지정하는 것

for i in num:
    if i > max:         # 비교 값
        max = i         # 제일 큰 값
print(max)