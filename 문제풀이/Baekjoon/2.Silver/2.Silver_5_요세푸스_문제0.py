import sys
sys.stdin = open('input.txt')

# 1번부터 N명의 사람이 원으로
# K번째 사람을 제거한다
# N명의 사람이 모두 제거될 때까지 계속됨

N, K = map(int, input().split())

array = []

for n in range(1, N + 1):
    array.append(n)

result = []
cnt = 1
i = 0

# 계속 리스트를 순회해야 한다
while len(array) != 0:
    if i < len(array):

        # 리스트를 순회하면서 cnt가 K와 같으면
        if cnt == K:
            # array에서 해당 인덱스 i 에 있는 숫자를 pop하고
            # resuly 리스트에 저장한다
            a = array.pop(i)
            result.append(a)
            # 그리고 cnt를 초기화 하기
            cnt = 0
            # 숫자가 하나씩 사라지면, 숫자들이 앞으로 당겨져서, 1을 빼야한다
            i -= 1

        # 만약 array가 비어있지 않고, 마지막 숫자가, 순회하는 숫자와 같을 경우
        # i를 -1로 초기화 한다.
        # -1으로 초기화 하는 이유는, 마지막 숫자가 끝나고 다시 인덱스 0으로 가야한다
        # 밑에 i를 1씩 누적시켜서, -1로 초기화 시켜야 한다
        if len(array) != 0 and array[-1] == array[i]:
            i = -1


    cnt += 1
    i += 1

result = ', '.join(map(str, result))
print(f'<{result}>')