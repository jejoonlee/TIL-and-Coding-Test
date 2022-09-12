import sys
sys.stdin = open('input.txt')

# 스택 안에 있는 요소의 개수를 더하면서 쇠막대기 개수를 센다

stick = input()

stack = []

result = 0
for i in range(len(stick)):
    if stick[i] == '(':
        stack.append(i)
    
    else:
        # 레이저로 자르는 기준에서 처음으로 ')'가 나오면
        # stack에 쌓아 두었던 쇠막대기의 개수를 센다
        if stick[i - 1] == '(':
            stack.pop()
            result += len(stack)
        
        # ')'가 연속으로 있을 수 있다
        # 이 뜻은, 처음은 레이저로 자르고, 그 뒤로는 막대의 길이가 짧아지는 것
        # 쯕 막대가 ')'가 연속으로 있으면, 하나씩 줄어든 다는 것
        # 그래서 그냥 result에 1을 더한다
        elif stick[i - 1] == ')':
            stack.pop()
            result += 1

print(result)