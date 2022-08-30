import sys
sys.stdin = open('input.txt')

# push X: 정수 X를 스택에 넣음
# pop: 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력. 
#   정수가 없으면 -1을 출력
# empty: 스택이 비어있으면 1, 아니면 0을 출력
# size: 스택에 있는 정수의 개수를 출력
# top: 스택의 가장 위에 있는 정수를 출력
#    스택에 들어있는 정수가 없으면 -1을 출력


N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        stack.append(com[1])
    
    elif com[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    
    elif com[0] == 'size':
        print(len(stack))

    elif com[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    
    elif com[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)