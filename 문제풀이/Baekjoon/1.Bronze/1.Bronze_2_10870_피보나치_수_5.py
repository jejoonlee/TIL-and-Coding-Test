
n = int(input())

fibo_1 = 0
fibo_2 = 1
for i in range(n):
    fibo_3 = fibo_1 + fibo_2
    fibo_1 = fibo_2
    fibo_2 = fibo_3

print(fibo_1)
# fibo_2 또는 fibo_3는 89임

