
import sys
sys.stdin = open('input.txt', 'r')


hear, see = map(int, input().split())

lst = []
for h in range(hear):
    h_name = input()
    lst.append(h_name)

for s in range(see):
    s_name = input()
    lst.append(s_name)

hs_dict = {}
for i in lst:
    if i not in hs_dict:
        hs_dict[i] = 0
    else:
        hs_dict[i] += 1

names = []
for key,value in hs_dict.items():
    if value == 1:
        names.append(key)
        names.sort()

print(len(names))
print('\n'.join(names))