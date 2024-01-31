

import sys
import math

input = sys.stdin.readline

def is_prime(num):

    if num == 0 or num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True


t = int(input())

for _ in range(t):

    num = int(input())

    while not is_prime(num):
        num += 1
    
    print(num)