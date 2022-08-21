import sys
sys.stdin = open('input.txt', 'r')
# 입력된 값들을 리스트에 넣는다
# 값들 중에서 제일 큰 값을 구한다 (max) 이용
# 그리고 값들을 인덱스로 순회하면서 최댓값이 몇번 째인지 알아낸다
# 인덱스니깐 + 1 을 해야 한다

num_list = []
for _ in range(9):
    num = int(input())
    num_list.append(num)

max_value = max(num_list)
print(max_value)

for i in range(len(num_list)):
    if num_list[i] == max_value:
        print(i + 1)