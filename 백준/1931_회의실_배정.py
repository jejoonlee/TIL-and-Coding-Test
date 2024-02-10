import sys

input = sys.stdin.readline

n = int(input())

times = []

for _ in range(n):
    times.append(list(map(int, input().split(" "))))

times.sort(key=lambda x: (x[1], x[0]))

count, end = 0, 0

for i in range(n):
    currentStart, currentEnd = times[i][0], times[i][1]

    if end <= currentStart:
        end = currentEnd
        count += 1

print(count)
