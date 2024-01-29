
while True:
    a, b, c, = map(int, input().split(' '))

    if a == 0 and b == 0 and c == 0:
        break

    if a == b == c : print("Equilateral")
    
    elif a == b or a == c or b == c: 
        
        if a == b:
            if c < a + b : print("Isosceles")
            else: print("Invalid")
        if a == c:
            if b < a + c : print("Isosceles")
            else: print("Invalid")
        if b == c:
            if a < b + c : print("Isosceles")
            else: print("Invalid")

    else:
        if a > b and a > c:
            if a < b + c: print("Scalene")
            else: print("Invalid")

        elif b > a and b > c:
            if b < a + c: print("Scalene")
            else: print("Invalid")

        elif c > a and c > b:
            if c < a + b: print("Scalene")
            else: print("Invalid")