#--- 두배 수 ---
new_number = [n * 2 for n in range(1,5)]

#--- 레터가 5개 이상인 이름의 레터들을 다 대문자로 리스트에 저장하기 ---
names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']
long_names = [n.upper() for n in names if len(n) >= 5]

#--- 제곱수 ---
number = [1,2,3,4,5,6]
new_number = [n ** 2 for n in number]

#---짝수 필터링---
number = [1,2,3,4,5,6]
even_number = [n for n in number if n % 2 == 0 ]

#--- 이름들에 랜덤 점수 주기 ---
import random

names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']

random_score = {name : random.randint(1,100) for name in names}

#--- 통과한 학생 ---

passed_student = {key : value for key, value in random_score.items() if value >= 60}

print(passed_student)