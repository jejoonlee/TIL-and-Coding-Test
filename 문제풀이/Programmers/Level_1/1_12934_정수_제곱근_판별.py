def solution(n):
    answer = 0

    while True:
        answer += 1
        if answer ** 2 == n:
            answer = (answer + 1) ** 2
            break
        elif answer ** 2 > n:
            answer = -1
            break

    return answer


# n ** (1/2) 제곱근

def solution(n):
    square = n ** (1/2)

    if square % 1 == 0:
        return (square + 1) ** 2
    else:
        return -1