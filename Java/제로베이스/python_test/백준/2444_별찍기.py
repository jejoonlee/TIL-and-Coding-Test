num = int(input())


for i in range(1, num + 1):
    print((' ' * (num - i)) + ('*' * (2 * i - 1)))

for i in range(num - 1, 0, -1):
    print((' ' * (num - i)) + ('*' * (2 * i - 1)))