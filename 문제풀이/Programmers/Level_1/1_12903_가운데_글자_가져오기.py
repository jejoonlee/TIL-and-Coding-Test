s = 'qwer'

length = len(s)

if length % 2 == 0:
    print(f'{s[(length // 2) - 1]}{s[length // 2]}')
else:
    print(s[length // 2])