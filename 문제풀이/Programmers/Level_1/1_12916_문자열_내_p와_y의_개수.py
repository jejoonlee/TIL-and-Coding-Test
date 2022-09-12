
# def solution(s):
#     p = 0
#     y = 0

#     for S in s:
#         if S == 'p' or S == 'P':
#             p += 1
#         if S == 'y' or S == 'Y':
#             y += 1
    
#     if p == y:
#         return True
#     else:
#         return False

# print(solution('pPooyY'))

# return 값이 자동으로 boolean으로 변환되어 출력된다
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution('pPooy'))