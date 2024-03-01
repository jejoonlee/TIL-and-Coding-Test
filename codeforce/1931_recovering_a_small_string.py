

alphabets = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

t = int(input())

for _ in range(t):

    n = int(input())

    flag = False

    for i in range(1, 27):
        if flag : break
        for j in range(1, 27):
            if flag: break
            for k in range(1, 27):
                if i + j + k == n:
                    flag = True 
                    print(alphabets[i] + alphabets[j] + alphabets[k])    
                    break