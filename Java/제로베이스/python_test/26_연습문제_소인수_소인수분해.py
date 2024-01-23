
# 100부터 1000사이의 난수를 소인수분해를 하고 각각의 소인수에 대한 지수를 출력
# 20 = 2 ^ 2 * 5 ^ 1
# 지수는 2와 1

import random

num = random.randint(100, 1000)
print(num)

n = 2
map = {}

while num > 1:

    if num % n == 0:

        if n in map:
            map[n] += 1
        else:
            map[n] = 1
        
        num /= n

    else:
        n += 1

print(map)

for key, value in map.items():
    print(f'{key}의 지수 : {value}')