import sys
sys.stdin = open("input.txt")

# 돌상들은 왼쪽 또는 오른쪽을 보고 있다
# 돌상들을 연속으로 금칠을 한다
# 연속을 금칠하고 나서, 외쪽을 보는 돌상과 오른쪽을 보는 돌상들을 뺀다
    # 빼고 난 값이 깨달음의 양이다 (절대값으로 바꿔야 함)


N = int(input())

rocks = list(map(int, input().split()))

# 투포인터로 연속으로 금칠 한 돌상들을 구한다
start, end = 0, len(rocks) - 1

left, right = rocks.count(1), rocks.count(2)

max_count = abs(left - right)

while start < end:

    # 왼쪽을 보는 돌싱과 오른쪽을 보는 돌싱들 중, 수가 적은 쪽을 빼야 한다
    # 최대 값을 구하는 것이기 때문에
    if left > right:
        if rocks[start] == 2:
            start += 1
            right -= 1
        elif rocks[end] == 2:
            end -= 1
            right -= 1
        else:
            if rocks[end] == 1:
                left -= 1
            else:
                right -= 1
            end -= 1

    elif right > left:
        if rocks[start] == 1:
            start += 1
            left -= 1
        elif rocks[end] == 1:
            end -= 1
            left -= 1
        else:
            if rocks[end] == 1:
                left -= 1
            else:
                right -= 1
            end -= 1
    
    else:
        if rocks[end] == 1:
            left -= 1
        else:
            right -= 1
        end -= 1

    max_count = max(max_count, abs(left - right))

print(max_count)
        