# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

import math
pn = float(input("Please enter a positive number: "))
sqrt = math.sqrt(pn)
round = round(sqrt,1)

print("The square root of {} is approx. {}" .format(pn, round))