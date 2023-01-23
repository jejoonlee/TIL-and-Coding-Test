
# 이름들을 받아서, 리스트 안에 저장하기
with open("./Input/Names/invited_names.txt") as names:
    name = names.read()
    name_list = name.split("\n")

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()


for new_name in name_list:
    with open(f"./Output/ReadyToSend/{ new_name }.txt", "w") as new_letter:
        new_letter.write(content.replace('[name]', new_name))