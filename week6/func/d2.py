#Sample Input: 
# 25100 
# 2123 
# Sample Output: 
# Square root of 25100 after 2123 miliseconds 
# is 158.42979517754858

from time import sleep
import math


def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)

print(delay(lambda x: math.sqrt(x), 2123, 25100))

