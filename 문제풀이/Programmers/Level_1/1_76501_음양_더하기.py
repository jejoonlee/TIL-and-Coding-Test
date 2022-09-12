
absolutes = [4,7,12]
signs = [True,False,True]

result = 0
for i in range(len(absolutes)):
    if signs[i] == True:
        result += absolutes[i]
    else:
        result += -absolutes[i]

print(result)