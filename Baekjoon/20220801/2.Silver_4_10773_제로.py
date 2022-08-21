
K = int(input())

lst = []
for k in range(K):
    num = int(input())
    lst.append(num)

stack = []
for num in lst:
    if num != 0:
        stack.append(num)
    else:
        stack.pop()



print(sum(stack))