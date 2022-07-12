# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# numbers = [0, 20, 100, 50, -60, 50, 100] 
# numbers = [0, 1, 0] 
# numbers = [-10, -100, -30] 

numbers = [0, 20, 100]
max = numbers[0]
second_max = numbers[0]

for i in numbers:           #최대값이었던 것이 두번째로 큰 수
    if max < i:
        second_max = max    
        max = i
print(second_max)