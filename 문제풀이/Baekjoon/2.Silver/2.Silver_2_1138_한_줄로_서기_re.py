import sys
sys.stdin = open("input.txt")

N = int(input())

result = [0] * N

for index, num in enumerate(list(map(int, input().split()))):
    cnt = 0
    i = 0
    while True:
        if result[i] == 0 and cnt == num:
            result[i] = index + 1
            break
        elif result[i] == 0:
            cnt += 1
        i += 1
        
print(' '.join(map(str,result)))