import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    bit = list(input())
    flag = '0'
    cnt = 0

    # bit 리스트를 순회를 하면서, 숫자가 0으로 1로 바뀌거나 1에서 0으로 바뀌면
    # count를 한다
    # 하지만 초기화가 됬을 때 0이기 때문에, 0으로 시작을 해야 한다
    # 즉 첫번째 숫자가 1이면 count를 하며 리스트를 순회하고
    # 아니면 0부터 시작
    for i in range(len(bit)):
        if bit[i] != flag:
            cnt += 1
            flag = bit[i]

    print(f'#{t} {cnt}')