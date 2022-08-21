

con = []
for num in range(1, 10001):
    sum_ = 0
    nums = [num]
    # 생성자 여부
    while num:
        left = num % 10
        sum_ = sum_ + left
        num = num // 10
    nums.append(sum_)
    num_sum = sum(nums)
    con.append(num_sum)


for num in range(1, 10001):
    if num not in con:
        print(num)