'''
Define a function distance that takes in the coordinates of two points on 
a plane: (x1, y1) and (x2, y2)  as arguments and returns the distance between them.
'''

import math
def distance(x1, y1, x2, y2):
    # Returns the magnitude of the vector
    # between (x1, y1) and (x2, y2).
    x_difference, y_difference = x1 - x2, y1 - y2
    distance = math.sqrt(x_difference**2 + y_difference**2)
    return distance


'''
Write a max_of_three function to find the maximum value of three numbers.
'''

def max_of_three(x, y, z):
    return max(x, y, z)


'''
Define a function that takes three numbers as arguments and returns the sum of the squares of the two larger numbers.

For example, given three numbers 1, 2 and 3, since 2 and 3 are larger than 1, the bigger_sum function should return the integer value 13. 

Note: is_approximately_equal has been pre-defined. You do not have to define it.
'''

def bigger_sum(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    total = numbers[1] ** 2 + numbers[2] ** 2
    return total
