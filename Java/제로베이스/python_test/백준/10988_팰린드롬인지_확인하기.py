
word = input()

left, right = 0, len(word) - 1
answer = 1

while left <= right:
    
    if word[left] == word[right]:
        left += 1
        right -= 1
    else:
        answer = 0
        break

print(answer)