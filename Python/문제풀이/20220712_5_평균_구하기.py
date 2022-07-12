#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지
# numbers = [3, 10, 20]

num = [3, 10 ,20]

# 값 초기화
result = 0
count = 0

for i in num:  
    result += i             # num 에 있는 리스트들 더하기
    count += 1              # 리스트에서 하나씩 숫자를 꺼내올때마다 1씩 더하기         
    
print(result / count)
# print(sum(num) / len(num))
