# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

mult = a * b * c

li = [0] * 10
# 0부터 9의 리스트를 만들었음

mult_list = list(map(int, str(mult)))

# 'mult_list'를 인덱스로 만든 후
# 'li'의 'mult_list'의 N번째에 1씩 더한다
for i in range(len(mult_list)):
    li[mult_list[i]] += 1


for result in li:
    print(result)