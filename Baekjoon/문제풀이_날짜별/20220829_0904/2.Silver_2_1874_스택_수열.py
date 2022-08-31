import sys
sys.stdin = open('input.txt')
# 1부터 N의 수열을 stack에 넣기 시작한다

# stack에 넣었을 때, 입력된 수와 같으면, stack에서 pop을 한다

# 여기서 stack에 마지막 수가 입력된 첫번째 수와 같아야 한다

# 마지막에 stack에 숫자가 남으면 NO 출력

n = int(input())

array = []
for _ in range(1, n + 1):
    N = int(input())
    array.append(N)

stack = []
result = []
# 1부터 N번까지 순회한다
for i in range(1, n + 1):
    # i가 주어진 수열 첫번째 수와 같지 않다면
    # stack에 i를 넣고, +를 반환한다
    if i != array[0]:
        stack.append(i)
        result.append('+')

    # i와 수열 첫번째 수와 같다면
    # + 과 - 을 차례대로 result에 저장하고
    # 수열 첫번째 수를 없앤다
    if i == array[0]:
        result.append('+')
        result.append('-')
        array.pop(0)
        # stack의 개수가 0이 아닌 경우
        # while문을 통해 stack의 마지막 숫자와 수열의 첫번째 숫자를 비교한다
        if len(stack) > 0:
            while stack[-1] == array[0]:
                stack.pop()
                array.pop(0)
                result.append('-')
                if len(array) == 0:
                    break

if len(stack) != 0:
    print('No')
else:
    for ans in result:
        print(ans)
