import sys
sys.stdin = open('input.txt')

N = int(input())

lst = []
for n in range(N):
    chat = input()
    lst.append(chat)

gomgom = set()
leng = []

for c in lst:
    if c != 'ENTER':
        gomgom.add(c)
    elif c == 'ENTER':
        leng.append(len(gomgom))
        gomgom.clear()

leng.append(len(gomgom))
print(sum(leng))