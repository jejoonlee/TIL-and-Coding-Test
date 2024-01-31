
import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

pokemon = {}
pokemonNo = {}

for i in range(1, n + 1):
    name = input().strip()
    pokemon[name] = i
    pokemonNo[i] = name

for i in range(m):
    poke = input().strip()

    if poke.isdigit(): print(pokemonNo[int(poke)])
    else: print(pokemon[poke])