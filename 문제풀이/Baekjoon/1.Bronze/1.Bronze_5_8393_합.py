# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.


n = int(input())
result = 0

for i in range(n):
    i += 1
    result += i
    # i 는 1씩 증가하고
    # 증가된 i는 result 값과 더해진다

print(result)