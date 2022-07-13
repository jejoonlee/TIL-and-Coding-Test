a, b = map(int, input().split())

# if a != b:
#     print('True')
# else:
#     print('False')

print((a and (not b)) or ((not a) and b))