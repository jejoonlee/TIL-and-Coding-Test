# 🧑‍💻 문제 풀이

전체는 아님



### ✔️ 4673 셀프 넘버

```python
con = []
for num in range(1, 10001):
# num은 1이상 10000이하의 숫자를 꺼낸다
    sum_ = 0
    # nums 라는 리스트 안에 num을 미리 넣는다 
    nums = [num]
    # 생성자 여부: while문을 통해, 숫자를 쪼개는 것
    while num:
    # num의 값이 0이 아니면
        left = num % 10
        # num을 10으로 나누고 남은 값을 left에 저장하고
        sum_ = sum_ + left
        # left를 sum_이랑 더해준다 (초기값)
        num = num // 10
        # 그리고 num이 일이 숫자가 아닌 경우, 계속 10과 나눠, 몫을 구해 while문을 반복한다.
    nums.append(sum_)
    # 구한 sum_을 nums 라는 리스트에 넣는다
    num_sum = sum(nums)
    # 현재 nums 리스트에는 num이라는 값과 sum_이란 두 값들이 있다
    # 더해주면 문제에서의 d(n)이 만들어진다. 즉 num은 생성자 num_sum은 생성자가 존재하는 숫자다
    con.append(num_sum)


for num in range(1, 10001):
    if num not in con:
        print(num)
        # 즉 1이상 10000이하 숫자 중, con이라는 리스트 안에 존재하지 않으면 생성자가 없는 숫자들이다
```

**🚨중요 포인트**

- `num`이라는 변수는 '생성자'이고, while문을 통해 생성자가 만들어내는 숫자를 구한다
- while문을 통해 만들어낸 숫자는 `num_sum`이고,` num_sum`을` con`이라는 리스트 변수 안에 넣는다
- 여기서 `con`은 constructor라는 의미고, 생성자가 존재하는 숫자들의 값들이 들어가 있다

