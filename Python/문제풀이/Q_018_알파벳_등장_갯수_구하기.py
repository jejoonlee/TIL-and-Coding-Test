word = input()
result = {}                 # empty 'Dictionary'

for i in word:              
    if i in result:
        result[i] += 1      
    else:
        result[i] = 1       # 초기값

print(result)

#새로운 문제 풀이
for char in word:
    #딕셔너리에 키가 없으면?
    if not char in result:
        # 키랑 값을 0으로 초기화한다
        result[char] = 1
    # 딕셔너리에 키가 있으면?
    else:
        result[char] = result[char] + 1
print(result)


# 새로 문제 풀이
result = {}
for char in word:
    # result['a']없으면 keyError
    # result.get('a') 기본값이 none
    # result.get('a', 0) 기본값이 0
    result[car] = result.get(char, o) + 1
print(result)
