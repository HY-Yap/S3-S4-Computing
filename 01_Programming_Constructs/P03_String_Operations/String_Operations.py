'''
To concatenate strings in python, you can use the plus(+) sign.

For example, "There are 240 students in this class" + " and it is great!" will become
"There are 240 students in this class and it is great!"

As an exercise, assign a string using gunshot_single and car_exploded to guns_fired such that guns_fired will have the value 'Bang!Boom!'.
'''

gunshot_single = 'Bang!'
car_exploded = 'Boom!'
guns_fired = gunshot_single + car_exploded


'''
You can multiply strings in python using the multiplication operator: *

For example, "woof!" * 3 will give "woof!woof!woof!"

As an exercise, fill in the answer for fire_3_times such that it repeats gunshot_single for 3 times to get 'Bang!Bang!Bang!'

Then, fill in the answer fire_21_times such that it repeats gunshot_single for 21 times to get
Bang!Bang!Bang!.......Bang!Bang! where Bang! occurs in the string 21 times.
'''

gunshot_single = 'Bang!'
fire_3_times = gunshot_single * 3
fire_21_times = gunshot_single * 21


'''Without executing the code, evaluate the following expressions.'''

s = 'abc'
t = 'ABC'
u = 'abd'
# write your answer below without using IDLE 
# s + t + u
# your answer = abcABCabd
# s - t
# your answer = error
# s*3
# your answer = abcabcabc
# s > t
# your answer = True
# s > u
# your answer = False
# s + t < s
# your answer = False
# t + u > s + u
# your answer = False 
# t + s == s + t
# your answer = False


'''
You can use the inbuilt len function in python to calculate the length of a string. For example, len('I am a short string') will output 19.

As an exercise, assign the length of super_long_string to my_length.
'''

super_long_string = "I am so long that it is so taxing on the eyes to count the actual length of my string. You should rely on python to help you do this"
my_length = len(super_long_string)


'''
You can perform string slicing to remove portions of string that we may not be interested in. 

For example, given my_recent_purchase = 'I bought a new toy but it costed me 100 dollars' and 
we can do my_recent_purchase[:18] to only retain the characters from the start to index 17 of the string. 
my_recent_purchase[9:] will output all the characters from index 9 to the end of the string. 
You can use also my_recent_purchase[2:5] to get the characters from index 2 to 4 of the string. Try them!

As an exercise, assign the string consisting of the index 5 to index 15 (inclusive) 
from long_string to character_from_5_to_15 using string slicing. 
'''

long_string = 'I am only interested in the characters from 5 to 15 in this string'
character_from_5_to_15 = long_string[5:16]
