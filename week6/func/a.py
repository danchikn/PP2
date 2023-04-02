from functools import reduce

num = lambda x, y: x * y
mult = [1, 5,3,10,15]
res = reduce(num, mult)
print(res)