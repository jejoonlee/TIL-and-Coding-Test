# 가장 많은 학생들이 유학을 가는 대학교는 영국의 캠브리지 대학교이다. 
# 정부는 인터넷 검열을 통해서 해외로 나가는 이메일의 내용 중 일부를 삭제하기로 했다. 
# 이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했다. 
# 즉, 어떤 이메일에 LOVA란 단어가 있다면, A는 CAMBRIDGE에 포함된 알파벳이기 때문에, 받아보는 사람은 LOV로 받는다.



input_ = input()

del_word = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
# 해당 알파벳을 input_에서 찾게되면, .replace를 통해 없애는 것

for i in del_word:
    if i in input_:
        input_ = input_.replace(i, '')

print(input_)