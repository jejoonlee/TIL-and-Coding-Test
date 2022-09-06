
# 은민이는 4와 7을 좋아함
# 금민수 = 4와 7로만 이루어진 수
# N보다 작거나 같은 금민수 중 가장 큰 수

N = int(input())

# 작거나 같은 => + 1

while True:
    flag = True

    nums = str(N)

    for i in range(len(nums)):
        if nums[i] == '4' or nums[i] == '7':
            pass
        else:
            # 4, 7이 아예 없다면 flag는 False로 저장된다
            # 그렇게 저장되면, 아래 if 조건문과 성사가 안 되서
            # 다시 while문 시작점으로 돌아간다
            flag = False
            N -= 1
            # 최대값을 구하기 때문에, 내려오면서 계산한다
            # 예를 들어 100부터 시작해서, flag가 False이면
            # N에 1일 빼준다

    if flag:
        print(N)
        break