import sys
sys.stdin = open("input.txt")

N = int(input())

alphabets = [input() for _ in range(N)]

alpha_dict = {}

for alphabet in alphabets:
    times = len(alphabet)
    for num in range(times):
        if alphabet[num] not in alpha_dict:
            alpha_dict[alphabet[num]] = 10 ** (times - 1)
            times -= 1
        else:
            alpha_dict[alphabet[num]] += 10 ** (times - 1)
            times -= 1

alpha = list(alpha_dict.values())
alpha.sort(key=lambda x : -x)

result = 0
cnt = 9
for al in alpha:
    result += al * cnt
    cnt -= 1

print(result)