
def add(*args):
    answer = 0
    for n in args:
        answer += n
    
    return answer

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)