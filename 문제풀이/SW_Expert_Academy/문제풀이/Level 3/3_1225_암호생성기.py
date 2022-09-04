import sys
sys.stdin = open('input.txt')
# 8개의 숫자를 입력받는다
# 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다
# 그 다음 번째 숫자는 2 감소한 뒤 맨 뒤로 보내고,
# 5까지 감소할때를 한 사이클이다

# 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료되고, 
# 해당 8자리 숫자 값이 암호가 된다

from collections import deque

for _ in range(10):
    
    t = int(input())
    N = list(map(int, input().split()))

    N = deque(N)

    # 리스트 마지막 숫자가 0이 될때까지 while반복문을 돌린다
    while N[-1] != 0:
        # for문을 통해 1부터 5까지 빼는 사이클을 만들어준다
        # 이 사이클은 첫번째 숫자와 1~5 숫자를 뺐을때 0과 같거나
        # 낮은 수면, 0을 리스트 마지막에 넣고 for문을 끝낸다
        for i in range(1, 6):
            num = N.popleft()
            if num - i > 0:
                N.append(num - i)
            else:
                N.append(0)
                break

    N = ' '.join(map(str, N))
    print(f'#{t} {N}')