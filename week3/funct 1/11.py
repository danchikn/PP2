def pal(n):
    if n == n[::-1]:
        return True 
    else:
        return False
n = input()
print(pal(n))