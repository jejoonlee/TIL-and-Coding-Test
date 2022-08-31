import sys
sys.stdin = open('GNS_test_input.txt')

# 딕셔너리를 이용해서, 딕셔너리의 key를 사용하면서
# 언어를 숫자로 변환해서 정렬한 후
# 숫자를 언어로 변환해서 출력하기

new_cnt = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
cnt = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

T = int(input())

for _ in range(T):
    t, N = input().split()

    sorting = []
    array = list(input().split())

    for i in array:
        sorting.append(new_cnt[i])

    sorting.sort()

    answer = []
    for ans in sorting:
        answer.append(cnt[ans])

    print(t)
    print(*answer)