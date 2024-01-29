
tList = list(map(int, input().split(' ')))

tList.sort()

answer = tList[0] + tList[1]

if answer <= tList[2]:
    answer += answer - 1

else:
    answer += tList[2]

print(answer)