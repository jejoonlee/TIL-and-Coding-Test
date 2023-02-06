people = [70, 50, 80, 50]
limit = 100
answer = 0

total_weight = 0

people.sort()

for weight in people:
    if total_weight + weight > limit:
        total_weight = 0
        answer += 1
        total_weight += weight
    else:
        total_weight += weight

if total_weight != 0:
    answer += 1

print(answer)
