
arr = [5, 9, 7, 10]
divisor = 11

result = []
for a in arr:
    if a % divisor == 0:
        result.append(a)

# if len(result) != 0:
#     result.sort()
#     print(result)
# else:
#     result.append(-1)
#     print(result)

print(result if len(result) != 0 else [-1])

#------------------------------------------------------#

# def solution(arr, divisor):

#     result = []
#     for a in arr:
#         if a % divisor == 0:
#             result.append(a)

#     return result if len(result) != 0 else [-1]