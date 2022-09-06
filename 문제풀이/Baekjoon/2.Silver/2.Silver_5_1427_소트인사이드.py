
# 수가 주어지면, 내림차순으로 정렬하기

# 정렬에 인덱스 별로, 숫자를 넣어준다
# 그리고 뒤에서부터 순회를 한다
# 0이 아닌 인덱스를 찾고,
# 0이 될때까지 해당 인덱스를 result 리스트에 넣으면서
# 하나씩 인덱스 값을 빼준다

N = input()

arr = [0] * 10

for n in N:
    n = int(n)
    arr[n] += 1

result = []
for num in range(len(arr))[::-1]:
    if arr[num] != 0:
        while arr[num] != 0:
            result.append(num)
            arr[num] -= 1

result = ''.join(map(str, result))
print(result)
