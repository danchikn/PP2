def squares(a,b):
    while a <= b:
        yield a*a
        a += 1
        
for i in squares(a = int(input()), b = int(input())):
    print(i, end = " ")
        