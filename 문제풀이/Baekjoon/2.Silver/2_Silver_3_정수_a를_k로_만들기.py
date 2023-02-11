import sys
sys.stdin = open('input.txt')

end, start = map(int, input().split())
count = 0

while start != end:
    if start % 2 == 0 and start // 2 >= end:
        start //= 2
        count += 1
    else:
        start -= 1
        count += 1

print(count)