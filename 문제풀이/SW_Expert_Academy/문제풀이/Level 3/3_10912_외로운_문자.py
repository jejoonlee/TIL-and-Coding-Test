import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for t in range(1, T + 1):
  words = deque(list(input()))
  stack = []

  while words:
    word = words.popleft()

    if len(stack) == 0:
      stack.append(word)

    elif word in stack:
      stack.pop(stack.index(word))
    
    else:
      stack.append(word)
  
  stack.sort()
  stack = ''.join(stack)

  if stack:
    print(f'#{t} {stack}')
  else:
    print(f'#{t} Good')