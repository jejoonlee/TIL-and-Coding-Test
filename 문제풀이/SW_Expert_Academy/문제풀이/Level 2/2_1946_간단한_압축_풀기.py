import sys
sys.stdin = open('input.txt')

# 너비가 10인 여러 줄의 문자열
# 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍

# 리스트의 개수 num // 10
# 이차원 리스트를 10개의 단어 묶음에, 나머지가 있는 묶음을 추가로 만든다
# 그리고 단어 10개씩, 한 묶음에 넣는다

# T = int(input())

# for t in range(1, T + 1):
#     N = int(input())

#     letter = int(input())

#     letters = []
#     num_add = 0
#     for _ in range(letter):
#         l, num = input().split()
#         num = int(num)

#         let = l * num

#         for i in let:
#             letters.append(i)

#         num_add += num

#         # 필요한 리스트 개수 구하기
#         list_count = num_add // 10
    
#     # 넣어야 할 리스트 개수 구하기
#     result = [[] for _ in range(list_count + 1)]

#     for row in range(len(result)):

#         while len(result[row]) != 10:
#             # letters 리스트에 있는 모든 알파벳이 없어질 때까지
#             # while문을 실행한다
#             if len(letters) == 0:
#                 break
#             else:
#                 result[row].append(letters[0])
#                 letters.pop(0)

#     print(f'#{t}')
#     for i in result:
#         i = ''.join(i)
#         print(i)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    
    li = []
    for i in range(N):
        alpha, num = input().split()
        num = int(num)
        for j in range(num):
            li.append(alpha)
            
    cnt = 0
    for j in range(len(li)):
        # 리스트에 순회하고 순회하면서 값을 출력한다
        print(li[j], end = '')
        # 카운트가 10이 될때까지 진행
        cnt += 1
        if(cnt == 10):
            # 10이 되면 cnt를 0으로 초기화 시킨다
            # 그리고 print()으로 한칸 아래로 내려간다
            cnt =0
            print()
    print()