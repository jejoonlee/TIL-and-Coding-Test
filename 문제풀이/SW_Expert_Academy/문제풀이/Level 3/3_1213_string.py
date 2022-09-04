import sys
sys.stdin = open('input.txt', encoding = 'utf-8')

for i in range(10):
    t = int(input())
    search = str(input())
    words = str(input())

    print(f'#{t} {words.count(search)}')
