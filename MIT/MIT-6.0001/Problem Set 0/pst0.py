# Author : Mohamed S. Gabriel
# Date : 12/8/2021 (DECEMBER)


# Assignment:
# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.

from math import log

x = int(input("Enter a x please: "))
y = int(input("Enter a y please: "))

print(x ** y)
print(log(x, 2))
