import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(' ')))
# + , - , *, /
operatorInput = list(map(int, input().split(' ')))

def combi(array, idx, limit):

    global result

    if len(array) >= limit:
        number = outcome(array)
        result = [max(result[0], number), min(result[1], number)]
        return
    
    for i in range(0, len(operators)):
        if visited[i] == 0:
            visited[i] = 1
            combi(array + [operators[i]], idx + 1, limit)
            visited[i] = 0

def outcome(array):
    number = nums[0]
    for i in range(len(array)):

        if array[i] == 0:
            number += nums[i + 1]
        elif array[i] == 1:
            number -= nums[i + 1]
        elif array[i] == 2:
            number *= nums[i + 1]
        elif array[i] == 3:
            if nums[i + 1] < 0 and number < 0:
                number = number * - 1
                number //= abs(nums[i + 1])
            elif nums[i + 1] < 0:
                number //= abs(nums[i + 1])
                number *= -1
            elif number < 0:
                number *= -1
                number //= nums[i + 1]
                number *= -1
            else:
                number //= nums[i + 1]

    return number


operators, result = [], [-1000000000, 1000000000]

for i in range(4):
    for j in range(0, operatorInput[i]):
        operators.append(i)

visited = [0] * len(operators)

combi([], 0, len(operators))

for r in result: print(r)