#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지
# numbers = [3, 10, 20]

num = [3, 10 ,20]
sum_li = 0
len_li = 0

for i in num:  
    sum_li += i             # num 에 있는 리스트들 더하기
    len_li += 1             # 리스트에서 하나씩 숫자를 꺼내올때마다 1씩 더하기         
    
print(sum_li / len_li)

