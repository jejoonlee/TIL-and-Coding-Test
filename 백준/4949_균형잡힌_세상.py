
import sys
from collections import deque

input = sys.stdin.readline

def check(sentence):
    check = deque()

    for w in sentence:

        if w == '(' or w == '[':
            check.append(w)

        elif w == ')':
            if len(check) != 0 and check[-1] == '(':
                check.pop()
            else:
                return False
        
        elif w == ']':
            if len(check) != 0 and check[-1] == '[':
                check.pop()
            else:
                return False

    if len(check) == 0: return True
    else: return False  
    


while True:
    sentence = input()
    sen = sentence[: -1]

    if sen == '.': break
    
    if check(sen): print('yes')
    else: print('no')