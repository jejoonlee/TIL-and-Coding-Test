w, h, b = map(int, input().split())

result = (w * h * b) / 2 ** 23

print('%.2f'%result, 'MB')

# '%f' float를 포맷하는데 쓰인다. f에 '.2f' 처럼 쓰면 소수점 2까지 반올림 하는거다. 
# '%f'%float_number => float_number에 반올림 할 값을 쓴다