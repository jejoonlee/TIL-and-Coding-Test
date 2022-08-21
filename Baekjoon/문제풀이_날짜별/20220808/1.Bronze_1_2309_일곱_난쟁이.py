
import sys
sys.stdin = open('input.txt', 'r')

# 7명의 난쟁이 키의 합이 100이다
# 9명 중 2명을 빼야한다
# 9명의 키의 총 합은 140이다
# 즉 9명 중 2명을 해야하고, 40을 빼야한다
# 2명의 합이 40일 때, 그 둘을 찾아서 뺀다

# 9 난쟁이들의 키
H = []

for h in range(9):
    height = int(input())
    H.append(height)

total = sum(H)

for i in range(len(H) - 1):
    for j in range(i + 1, len(H)):
        rm = H[i] + H[j]
        if total - rm == 100:
            H.remove(H[j])
            # 앞에서부터 빼버리면, 뒤에 인덱스가 한칸씩 땡겨진다
            H.remove(H[i])
        if len(H) == 7:
        # 앞에서 두명을 빼고, 7명을 구했기 때문에
        # 7명이 나오면 for문을 끝내는 조건문을 넣는다
            result = sorted(H)
            break

for i in result:            
    print(i)    