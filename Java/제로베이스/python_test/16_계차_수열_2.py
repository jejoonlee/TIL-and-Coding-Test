
# 어떤 수열의 인접하는 두 항의 차로 이루어진 또 다른 수열
# 0    3    8   15  24      35      48      63
#   3     5   7    9    11      13       15         => 여기서 수열이 보인다

# 두 번째의 an = a1 + (n-1) * d 일반항을 구해라
# 그리고 sn = n(a1 + an) / 2 수열의 합을 구하면 된다

inputAN1 = int(input('a1 입력 : '))
inputAN = int(input('an 입력 : '))

inputBN1 = int(input('b1 입력 : '))
inputBD = int(input('bn 공차 입력 : '))

valueAN = inputAN1
valueBN = inputBN1
n = 1

while n <= inputAN:

    print(f'an의 {n}번째 항의 값 : {valueAN}')

    valueAN += valueBN
    valueBN += inputBD

    n += 1