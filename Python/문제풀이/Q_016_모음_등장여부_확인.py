word = input()
cnt = 0

for vw in word:
    if(vw == 'a' or vw == 'e' or vw == 'i' or vw == 'o' or vw == 'u'):
        cnt += 1
print(cnt)


# 다른 풀이
count = 0
for char in word:
    if char in 'aeiou':
        count += 1
    print(count)