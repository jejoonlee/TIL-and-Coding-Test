
A, B = input().split()

mini = int(A.replace('6', '5')) + int(B.replace('6', '5'))
maxi = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(mini, maxi)