import sys
sys.stdin = open('input.txt')


min_num = 1e9
max_num = -1e9

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))


def dfs(num_depth, total, plus, minus, multiply, divide):
    global min_num, max_num

    if num_depth == N:
        min_num, max_num = min(total, min_num), max(total, max_num)
        return
    
    if plus > 0:
        dfs(num_depth + 1, total + numbers[num_depth], plus - 1, minus, multiply, divide)

    if minus > 0:
        dfs(num_depth + 1, total - numbers[num_depth], plus, minus - 1, multiply, divide)

    if multiply > 0:
        dfs(num_depth + 1, total * numbers[num_depth], plus, minus, multiply - 1, divide)

    if divide > 0:
        dfs(num_depth + 1, int(total / numbers[num_depth]), plus, minus, multiply, divide - 1)


# number[0]을 미리 argument의 total로 넣어서, num_depth를 1로 시작한다
# 그렇게 해야 다음 숫자와 연산자를 사용할 수 있다
dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(int(max_num))
print(int(min_num))