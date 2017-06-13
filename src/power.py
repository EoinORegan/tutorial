# This is a script that claculates one number to 
# the power of another.
def to_the_power(x, y = 2):
    result = x
    for i in range(0, y):
        result = result * x
    return result

x = 9
<<<<<<< HEAD
y = 8 # 
=======
y = 8
>>>>>>> 3642a5831cd2152a5384496fb8adbff8aad109c6
print("{0} to the power of {1} is: {2}".format(x, y, to_the_power(x, y)))
print ("The End")

