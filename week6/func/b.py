def str(s):
    upp = 0
    low = 0
    
    for char in s:
        if char.isupper():
            upp +=1
        elif char.islower():
            low +=1
    return upp, low

string_s = "Hi, weolsMPMIOObn ND "
result = str(string_s)
print(result)