
p = "01033334444"

p = list(p)

for i in range(len(p) - 4):
    p[i] = '*'

print(''.join(p))