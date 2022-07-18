# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# numbers = input().split()
# print(sum(numbers))

numbers = map(int, input().split())
print(sum(numbers))
# int를 넣어준다. 오류 코드에는 입력시, str으로 반환 되어, 계산을 못 한다