# 좋은 단어 O)

# A  B   B  A
# |  |___|  |
# |_________|

# 좋은 단어 X)

# A  B A  B

# |_|__|  |

#   |_____|      

import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = 0

for _ in range(N):
    AB = list(input())
    stack = []

    for ab in AB:
        if not(stack) or stack[-1] != ab:
            stack.append(ab)

        # stack 마지막 단어와 같으면 stack에서 꺼낸다
        elif stack[-1] == ab:
            stack.pop()
    
    if not(stack):
        cnt += 1

print(cnt)