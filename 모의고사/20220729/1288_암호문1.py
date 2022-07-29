
# # 10개의 테스트
# for t in range(1, 11):

ori_range = int(input())
# 원본 암호문 길이

ori = input().split()
# 원본 암호문

com_range = int(input())
# 명령어의 개수

com = input().split()
# 명령어

print(ori_range)
print(ori)
print(com_range)
print(com)

com_lst = []
for command in com:
    if command == 'I':
        continue
    else:
        com_lst.append(command)

print(com_lst)