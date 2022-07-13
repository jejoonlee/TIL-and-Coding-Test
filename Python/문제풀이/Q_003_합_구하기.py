# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# 1) while 문
n = 0
result = 0
user_input = int(input())

while n <= user_input :         # n이 user_input 값보다 작거나 같을 때까지
    result += n                 # n을 result와 계속 더해주고
    n += 1                      # n은 1씩 증가한다

print(result)


# 2) for 문
user_input = int(input())
n = 0
result = 0

for i in range(0, user_input + 1):      # range는 이상, 미만이라서 user_input에 1을 더함
    result += n                         
    n += 1

print(result)

# while문에서는 'n <= user_input' 이었지만, for문에서 range를 활용