# This is a script that claculates one number to 
# the power of another.
def to_the_power(x, y = 2):
	### trying this out
	###
    return x ** y 
	result = x
    for i in range(0, y):
        result = result * x
    return result

import math
def square_root(x):
return math.sqrt(x)

x = 5 #
y = 8 # 
print("{0} to the power of {1} is: {2}".format(x, y, to_the_power(x, y)))
print("The square root of {0} is {1}".format(x, square_root(x)))
print ("The End")

