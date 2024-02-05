import sys

input = sys.stdin.readline


def isPalindrome(word, left, right):

    global count

    count += 1

    if left >= right:
        return 1
    
    elif word[left] != word[right]:
        return 0
    
    return isPalindrome(word, left + 1, right - 1)

for _ in range(int(input())):
    word = input().strip()

    count = 0

    print(isPalindrome(word, 0, len(word) - 1), count)

