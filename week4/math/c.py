"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
from math import tan, pi
n = int(input())
a = int(input())
area = n * (a ** 2) / (4 *tan(pi/n))
print(area)
