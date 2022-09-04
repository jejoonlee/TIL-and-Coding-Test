
# 같은 단어가 있으면, 앞에만 바뀌고, 바로 다음 단어로 넘어간다.
# 다 다른 단어면 가능

# s = "1zerotwozero3"

# num_let = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# num = []

# for i in range(len(num_let)):
#     if num_let[i] in s:
#         num.append(str(i))
#     if str(i) in s:
#         num.append(str(i))

# print(num)


s = "1zerotwozero3"
num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

answer = ''
alp = ''

for letters in s:
    if letters.isdigit():
        answer += letters
    else:
        alp += letters
        if alp in num.keys():
            answer += num[alp]
            alp = ''

print(int(answer))