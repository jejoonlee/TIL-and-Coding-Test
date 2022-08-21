import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    t_num = int(input())
    score = list(map(int, input().split()))

    scores = {}

    for i in score:
        if i not in scores:
            scores[i] = 1
        else:
            scores[i] += 1

    max_value = max(scores.values())

    result = []
    for key, value in scores.items():
        if value == max_value:
            result.append(key)

    print(f'#{t_num} {max(result)}')