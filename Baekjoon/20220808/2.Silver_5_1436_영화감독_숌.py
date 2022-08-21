# 666이 적어도 6이 3개 이상

N = int(input())

num = 665
cnt = 0

while cnt != N:
    # num에 cnt가 N이랑 같아질 때까지, 1을 누적시킨다
    num += 1
    nums = str(num)

    # 666이 연속으로 있으면, cnt에 1을 누적시킨다
    if '666' in nums:
        cnt += 1

# 최종 숫자를 출력하는 것이라서, num을 출력
print(num)