import sys

sys.stdin = open("_괄호짝짓기.txt")

for t in range(1, 11):
    dis = int(input())
    brak = list(input())

    stack = []

    for i in brak:
        if i in '([{<':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '(':
                print(f'#{t} 0')
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '[':
                print(f'#{t} 0')
                break
            elif stack[-1] == '[':
                stack.pop()
        elif i == '}':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '{':
                print(f'#{t} 0')
                break
            elif stack[-1] == '{':
                stack.pop()
        elif i == '>':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '<':
                print(f'#{t} 0')
                break
            elif stack[-1] == '<':
                stack.pop()
    else:     
        if len(stack) != 0:
            print(f'#{t} 0')
        else:
            print(f'#{t} 1')