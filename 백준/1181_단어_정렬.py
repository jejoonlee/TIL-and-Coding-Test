import sys

words = []
for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().split("\n")
    words.append([word[0], len(word[0])])

words.sort(key=lambda x: (x[1], x[0]))

print(words[0][0])

for i in range(1, len(words)):
    if words[i] != words[i - 1]:
        print(words[i][0])
