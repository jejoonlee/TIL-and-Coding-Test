import sys
sys.stdin = open('input.txt')

# 포켓몬 N개
# 문제 개수 M개

N, M = map(int, input().split())

pokemon = {}

# 포켓몬 이름 : 번호
# 번호 : 포켓몬 이름
# 모두가 딕셔너리에 저장 됨

for n in range(1, N + 1):
    name = input()
    pokemon[name] = str(n)
    pokemon[str(n)] = name


for m in range(M):
    search = input()
    print(pokemon[search])