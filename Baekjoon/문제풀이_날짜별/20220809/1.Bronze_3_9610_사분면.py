import sys
sys.stdin = open('input.txt', 'r')

# Q1 = x, y
# Q2 = -x, y
# Q3 = -x, -y
# Q4 = x, -y

area = {
    'Q1' : 0,
    'Q2' : 0,
    'Q3' : 0,
    'Q4' : 0,
    'AXIS' : 0
}

T = int(input())

for t in range(T):

    x, y = map(int, input().split())

    if x == 0 or y == 0:
        area['AXIS'] += 1
    elif x > 0 and y > 0:
        area['Q1'] += 1
    elif x < 0 and y > 0:
        area['Q2'] += 1                                                            
    elif x < 0 and y < 0:
        area['Q3'] += 1
    elif x > 0 and y < 0:
        area['Q4'] += 1

for key, value in area.items():
    print(f'{key}: {value}')