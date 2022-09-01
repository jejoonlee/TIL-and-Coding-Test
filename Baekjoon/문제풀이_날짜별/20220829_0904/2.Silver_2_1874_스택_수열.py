import sys
sys.stdin = open('input.txt')

# 1부터 N번까지 순회한다
# 순회하면서 주어진 수열의 첫번째 숫자와 비교를 한다
# 숫자가 다르면 stack에 넣는다. stack의 마지막 숫자와 
# 수열의 첫번째 숫자가 같을때까지 반복한다

# 질문 잘 읽기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


n = int(input())

array = []
for _ in range(1, n + 1):
    N = int(input())
    array.append(N)

stack = []
result = []

# 1부터 n번까지 순환하기
for i in range(1, n + 1):
    # 순환하는 숫자 i를 stack에 저장한다
    stack.append(i)
    # 그리고 result에 '+'를 저장한다
    result.append('+')

    # 스택에 제일 마지막에 있는 숫자와
    # 입력 받은 수열의 첫번째 숫자를 비교한다
    # 둘이 같지 않으면 다시 숫자를 순환한다
    if stack[-1] != array[0]:
        continue
    # 만약 같다면 while문을 실행한다
    if stack[-1] == array[0]:
        # 스택에 마지막 숫자, 그리고 입력받은 수열을 첫번째
        # 숫자를 비교하면서, 같으면 그 둘을 리스트에서 빼면서
        # result에 '-'을 넣는다
        while stack[-1] == array[0]:
            stack.pop()
            array.pop(0)
            result.append('-')

            # while문이 종료되는 기준은 스택에 마지막 숫자와
            # 수열의 첫번째 숫자가 다르거나
            # stack에 숫자가 아예 없을 때
            if len(stack) == 0:
                break

if len(array) == 0:
    for ans in result:
        print(ans)
else:
    print('NO')



# 1부터 N번까지 순회한다
# for i in range(1, n + 1):
#     # i가 주어진 수열 첫번째 수와 같지 않다면
#     # stack에 i를 넣고, +를 반환한다
#     if i != array[0]:
#         stack.append(i)
#         result.append('+')

#     # i와 수열 첫번째 수와 같다면
#     # + 과 - 을 차례대로 result에 저장하고
#     # 수열 첫번째 수를 없앤다
#     if i == array[0]:
#         result.append('+')
#         result.append('-')
#         array.pop(0)
#         # stack의 개수가 0이 아닌 경우
#         # while문을 통해 stack의 마지막 숫자와 수열의 첫번째 숫자를 비교한다
#         if len(stack) > 0:
#             while len(stack) != 0:
#                 if stack[-1] == array[0]:
#                     stack.pop()
#                     array.pop(0)
#                     result.append('-')
#                 else:
#                     break

# if len(stack) == 0 and len(array) == 0:
#     for ans in result:
#         print(ans)
# else:
#     print('NO')

