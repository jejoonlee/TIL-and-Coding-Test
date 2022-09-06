# import sys
# sys.stdin = open('input.txt', 'r')

input_ = input()
question = []

while input_ != '고무오리 디버깅 끝':
    input_ = input()
    if input_ == '문제':
        question.append('문제')
    elif input_ == '고무오리':
        if question:
            question.pop()
        else:
            question.append('문제')
            question.append('문제')
    elif input_ == '고무오리 디버깅 끝':
        if len(question) == 0:
            print('고무오리야 사랑해')
        else:
            print('힝구')
        break