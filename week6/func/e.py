def all_true(my_tuple):
    return all(my_tuple)


my_tuple = (True, True, False, True)
result = all_true(my_tuple)
print(result)