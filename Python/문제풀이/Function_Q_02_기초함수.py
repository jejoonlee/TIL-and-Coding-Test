# 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# * 사각형 넓이 : 가로 * 세로 
# * 사각형 둘레 : (가로 + 세로) * 2

def rect(a, b):
    return a * b , (a + b) * 2  # ','를 통해 튜플로 반환시킨다

print(rect(20, 30))


#다른 가능한 공식
def rect(a, b):
    area = a * b
    perimeter = (a + b) * 2
    return area, perimeter

print(rect(20, 30))