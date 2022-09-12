def solution(n):
    return list(map(int, list(str(n))[::-1]))

print(solution(12345))