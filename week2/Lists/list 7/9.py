fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)

newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)