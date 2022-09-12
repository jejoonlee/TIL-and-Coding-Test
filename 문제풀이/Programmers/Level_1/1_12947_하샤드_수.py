

def solution(x):
    if x % sum(list(map(int, str(x)))) == 0:
        return True
    elif x % sum(list(map(int, str(x)))) != 0:
        return False


print(solution(12))