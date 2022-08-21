
T = int(input())

for t in range(T):
    a, b = input().split()
    a = int(a)

    # b 의 인덱스 a -1 번째를 없애고,
    # 나머지만 출력한다
    word = []
    for i in range(len(b)):
        if i != a - 1:
            word.append(b[i])
    
    print(''.join(word))
