n = int(input())

for i in range(0, n + 1, 2):
        if i < n - 1:
            print(i, end = ",")
        else:
            print(i)



# def even(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1


# n=int(input())
# l = list()
# for i in even(n):
#     l.append(str(i))

# print(l, sep = ",")