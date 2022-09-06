import sys
sys.stdin = open('input.txt')

# A = 고정비용/ B 가변 비용 / C 노트북 가격

A, B, C = map(int, input().split())

# 노트북 가격이 가변 비용보다 많아야 한다
if C > B:

    # 책정한 가격에 가변 비용을 뺀다
    # 하나가 팔리는 만큼, 가변 비용도 빠져 나간다
    dif = C - B

    # 고정비용은 더 팔릴수록 줄어든다
    # 즉 책정 가격에서 가변 비용을 뺀 이익과 
    # 고정비용을 나눠주면 된다
    bef = A / dif

    print(int(bef) + 1)

else:
    print(-1)