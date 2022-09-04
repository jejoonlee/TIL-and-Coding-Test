# 주어진 숫자만큼 # 을 출력해보세요.
# 주어질 숫자는 100,000 이하다.

a = int(input())
stamp = '#'

for i in range(0, a):   # 개수만큼 i
    print(stamp, end = '')  # '#'을 출력해라