# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# words = list(map(int, input().split()))
# print(words)
# word는 int로 되어있어, 문자열이 들어갈 수 없다
# ValueError: invalid literal for int() with base 10: "I'm"

words = list(input().split())
print(words)
# map 함수와, int를 빼면 해결 된다