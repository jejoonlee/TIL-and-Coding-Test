
# 시작과 끝의 구분이 없는 순열
# (n - 1)! or n!/n
#           1
#       2       3
#           4

n = int(input('친구 수 입력 : '))

ans = 1

for i in range(n - 1, 0, - 1):
    ans *= i

print(f"result : {ans}")