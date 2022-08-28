

# 0, 1

def fibo(N):
    if N == 1 or N == 0:
        return 1
    else:
        return fibo(N - 2) + fibo(N - 1)

print(fibo(int(input())))