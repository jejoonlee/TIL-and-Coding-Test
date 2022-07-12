# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# 1) while문
result = 1                              # result 와 n을 '0'으로 나두면 계속 답이 '0'이 된다
n = 1
user_input = int(input())

while user_input >= n:                   # 위에서 아래로 볼 것 (계산되는 형식도, 위에서 아래로!)
    result *= n
    n += 1
print(result)


# 2) for문
result = 1
n = 1
user_input = int(input())

for i in range(1, user_input + 1):
    result *= n
    n += 1
print(result)