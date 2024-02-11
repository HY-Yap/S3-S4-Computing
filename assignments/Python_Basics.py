'''
Given that variable a, b, c, d and e are bounded to values of 4, 8, 13, 17 and 48 respectively. 

Without using any direct assignment of integer values to variables or introducing new variables, 
bound the variables of a, b, c, d and e to new values of 13, 5, 4, 100 and 1/3 respectively.
'''

a = 4
b = 8
c = 13
d = 17
e = 48

a, b, c, d, e = c, c - b, a, e + e + a, a * a / e


'''
What is the value of the variable result if the following code is executed? Explain your answer.

54.

Line 1: result is set to 0

Line 2: result is 10 + 12 + (15 / 3) = 10 + 12 + 5 = 27

Line 3: value of x changed to 12, value of y changed to 15

Line 4: value of z changed to that of result (27)

Line 5: result is x + y + z (12 + 15 + 27 = 54)
'''


'''
Without executing the code, evaluate the following expressions.
'''
# x + y / z
# your answer = 1
# x ** y % x
# your answer = 0
# y <= z
# your answer = False
# x > y * z
# your answer = True
# (x < y) * z
# your answer = -2
# x - y + x - y  == z
# your answer = True
# x + z != z + y
# your answer = True
# y / 0
# your answer = error
# x / y + z
# your answer = -1.25
# y / x % z
# your answer = -2/3
# y % x / z
# your answer = -2/3
# x // 0
# your answer = error
# x // y
# your answer = 0
# y // x
# your answer = 1


'''
Identify areas of improvements for the following program.

def MY_FUNCTION   ( input1,input_2 ):
    sum=input1+input_2
    return sum
'''

# function name to lower case
# unnecessary spaces before / after the brackets
# variable name should not be sum
# space after comma
# more meaningful function name
# standardise input1 and input_2

def addition(input1, input_2):
    total = input1 + input_2
    return total