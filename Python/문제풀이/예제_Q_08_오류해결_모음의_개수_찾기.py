# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)

# if 문에서 한번에 chr == 모음들을 적을 수 없다
# 하나씩 char == 'a'...을 쓰거나 in 을 쓴다

word = "HappyHacking"

count = 0

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    # if char in 'aeiou':   도 사용 가능
        count += 1

print(count)
