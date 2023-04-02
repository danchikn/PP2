def mfunc(n):
    return abs(n-50)

list = [100, 50, 65, 82, 23]
list.sort(key = mfunc)
print(list)