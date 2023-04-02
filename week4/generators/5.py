def all(n):
    while n >= 0:
        yield n
        n -= 1
for i in all(n = int(input())):
    print(i, end = " ")