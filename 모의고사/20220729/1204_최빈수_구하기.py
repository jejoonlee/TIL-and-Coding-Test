import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    t_num = int(input())
    inp_score = input().split()

    scores = {}
    # 딕셔너리에 점수를 넣는다. 
    # 점수가 key, 점수의 개수가 value
    for i in inp_score:
        if i in scores:
        # 점수가 이미 있으면, value에 1씩 더하기
            scores[i] += 1
        else:
        # 없으면 key를 넣고, 1을 설정
            scores[i] = 1
    
    # 딕셔너리 value 중에 제일 큰 숫자 가지고 오기
    max_val = max(scores.values())

    # max-val 이랑 숫자가 같은 key를 lst에 넣기
    lst = []
    for key, value in scores.items():
        if value == max_val:
            lst.append(key)
    
    result = list(map(int, lst))
    
    # 리스트 안에서 max 숫자를 가지고 오면, 답이 된다
    print(f'#{t_num} {max(result)}')