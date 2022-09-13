import sys
sys.stdin = open('input.txt')

# L : 커서를 왼쪽으로 한 칸 옮김
# D : 커서를 오른쪽으로 한 칸 옮김
# B : 커서 왼쪽에 있는 문자를 삭제.
    # 예) [1, 2, 3] 커서가 3일때 2를 삭제하지만 커서는 3에 있음
# P $ : $라는 문자를 커서 왼쪽에 추가

array = list(input())
cnt = len(array)

for _ in range(int(input())):
    com = input().split()
    
    if com[0] == 'L':
        if cnt > 0:
            cnt -= 1
    
    elif com[0] == 'D':
        if cnt < len(array):
            cnt += 1
    
    elif com[0] == 'B':
        if cnt > 0:
            array.pop(cnt - 1)

    elif com[0] == 'P':
        array.insert(cnt, com[1])
        cnt += 1

print(array)