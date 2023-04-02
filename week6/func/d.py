import math
import time


def squy(number, de):
    print((de / 1000, "in seconds"))
    time.sleep(de / 1000)
    result = math.sqrt(number)
    return result


number = 25100
de = 2123
result = squy(number, de)
print(result)