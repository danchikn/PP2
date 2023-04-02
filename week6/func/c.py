# function which return reverse of a string
  
def isPalindrome(s):
    return s == s[::-1]
s = str(input())
str = isPalindrome(s)
  
if str:
    print("Yes")
else:
    print("No")