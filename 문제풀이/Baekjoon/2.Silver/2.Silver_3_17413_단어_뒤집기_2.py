import sys
sys.stdin = open('input.txt')

# 붙어있는 문자열은 뒤집는다
# <> 사이에 있는 문자열은 그냥 놔둔다

S = list(input())

idx = 0
start = 0

while len(S) != idx:

    # <> 사이에 있으면 문자열에 아무 일도 없다
    # <>가 끝날때까지 while문을 통해 인덱스 값을 더한다
    if S[idx] == '<':
        while S[idx] != '>':
            idx += 1
        idx += 1
    
    # 숫자나 알파벳이면 인덱스 슬라이싱을 위해 start 포인트를 변수로 저장해둔다
    elif S[idx].isalnum():
        start = idx

        # while문을 통해 idx 값을 숫자나 알파벳이 아니거나, 리스트 끝까지 도달할 때까지
        # 1을 누적시킨다
        while idx < len(S) and S[idx].isalnum() != False:
            idx += 1
        
        # an 이라는 변수에 start:idx 를 슬라이싱을 하고, 순서를 뒤바꾼다
        an = S[start : idx]
        an.reverse()
        S[start : idx] = an
    
    else:
        idx += 1

print(''.join(S))