
# FileNotFound
# 원래는 a_file.txt가 없어 에러가 뜰 것

try:
    file = open('a_file.txt')
    a_dictionary = {"key" : "value"}
    print(a_dictionary["sdfsdf"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Hello")

except KeyError as error_message:
    print(f"That key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file closed")