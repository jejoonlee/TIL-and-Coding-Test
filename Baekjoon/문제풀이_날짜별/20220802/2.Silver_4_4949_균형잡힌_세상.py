import sys
sys.stdin = open('input.txt', 'r')

while True:
    sen = input()
    stack_ = []

    if sen == '.':
        break

    for s in sen:
        if s == '(' or s == '[':
            stack_.append(s)
        elif s == ')':
            if len(stack_) == 0 or stack_[-1] == '[':
                stack_.append(s)
                break
            elif stack_[-1] == '(':
                stack_.pop()
        elif s == ']':
            if len(stack_) == 0 or stack_[-1] == '(':
                stack_.append(s)
                break
            elif stack_[-1] == '[':
                stack_.pop()
        
    if len(stack_) == 0:
        print('yes')
    else:
        print('no')
