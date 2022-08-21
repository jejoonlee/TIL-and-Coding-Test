# import sys
# sys.stdin = open('input.txt', 'r')

long = list(input())

long = list(map(ord, long))

cap = (65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90)

short = []
for i in long:
    if i in cap:
        short.append(i)

# .isupper() 로 쓸 수 있음

print(''.join(list(map(chr, short))))

