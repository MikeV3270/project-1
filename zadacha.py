a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a == 0:
    x = -c/b
    print (x) 
if a!= 0:   
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + (d**0.5) / (2 * a))
        x2 = (-b - (d**0.5) / (2 * a))
        print(x1,x2)
    elif d == 0:
        x = -b / (2 * a)
        print(x)
    if d < 0:
        print("no roots")
