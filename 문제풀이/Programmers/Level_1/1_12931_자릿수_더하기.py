def solution(n):
    n = str(n)
    answer = 0

    for N in n:
        answer += int(N)

    return answer

print(solution(987))