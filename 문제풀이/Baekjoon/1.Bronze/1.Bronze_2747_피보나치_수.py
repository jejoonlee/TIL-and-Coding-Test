
# 0 1 1 2 3 5 8 13 21 34----
N = int(input())

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# print(fibo(N))

# a b 
# 0 1 1 
# 1 2 3
# 2 3 5  

a, b = 0, 1
for _ in range(N):
    a, b = b, b + a
print(a)