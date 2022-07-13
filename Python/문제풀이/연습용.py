number = ['1', '2', '3']
# 리스트를 숫자로 형 변환 불가능/ 숫자에서 문자는 가능


new_num = map(int, number)
print(list(new_num))
# map 을 이용해서 리스트를 숫자 형으로 변환했다