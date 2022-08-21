
def solution(absolutes, signs):
    

    result = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            result = result + absolutes[i]
        elif signs[i] == False:
            result = result - absolutes[i]
    
    return result

print(solution([4, 7, 12], [True, False, True]))