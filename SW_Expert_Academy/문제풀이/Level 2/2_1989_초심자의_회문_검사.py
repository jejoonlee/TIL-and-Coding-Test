# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.


T = int(input())

for i in range(1, T + 1):
    a = input()
    b = a[::-1]     # a를 뒤로 읽기
    if a == b:
        print(f'#{i}', '1')
    else:
        print(f'#{i}', '0')