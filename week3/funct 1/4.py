def is_prime(n):
    if(n == 1): return False
    if(n == 2): return True
    if(n % 2 == 0): return False

    p = int(n ** 0.5) + 1
    for i in range(3, p):
        if(n % i == 0):
            return False
    return True

def filter_prime(numbers):
    filtered_list = []
    for i in numbers:
        if(is_prime(i)):
            filtered_list.append(i)
    return filtered_list

