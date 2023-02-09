people = [70, 50, 80, 50]
limit = 100
answer = 0

total_weight = 0

people.sort()

i = 0
    
while people:
    total_weight = people.pop()
    
    if people:
        for index, person in enumerate(people):
            if total_weight + person > limit:
                break
                
        if index - 1 == -1:
            answer += 1
            if len(people) == 1:
                people.pop()
        else:
            people.pop(index-1)
            
    else:
        answer += 1
        break

print(answer)
