def even(n):
 for i in range(0, n+1):
     if i % 12 == 0:    # 3*4 = 12
        yield i

n=int(input())
l = list()
for i in even(n):
    l.append(str(i))

print(l, sep = ",")

# 2 way 
# def generate(n):
#     for i in range(0, n+1):
#         if i % 12 == 0:    # 3*4 = 12
#             yield i

# n = int(input())
# ret = [str(i) for i in generate(n)]
# print(ret, end = ",")

