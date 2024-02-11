'''Write a function sum_digits(x) that takes in a non-negative integer x and returns the sum of all its digits.'''

def sum_digits(x):
    str_x = str(x)
    i = 0
    total = 0
    while i < len(str_x):
        total += int(str_x[i])
        i += 1
    return total

# alternative method (using math)
def sum_digits(x):
    result = 0
    while x > 0:
        result += x % 10
        x //= 10
    return result


'''Write a function sum_odd_digits(x) that takes in a non-negative integer x and returns the sum of all its odd digits.'''

def sum_odd_digits(x):
    str_x = str(x)
    i = 0
    total = 0
    while i < len(str_x):
        if int(str_x[i]) % 2 == 1:
            total += int(str_x[i])
        i += 1
    return total

def sum_odd_digits(x):
    sum_ = 0
    while x > 0:
        if x % 2 != 0:
            sum_ += x % 10
        x //= 10
    return sum_


'''
Write a function find_next_square(x) that takes in a non-negative integer x and returns its next largest perfect square.
You do not need to worry about efficiency for your implementation.
'''

import math
def find_next_square(x):
    next_square = x
    while True:
        next_square += 1
        if math.sqrt(next_square) == int(math.sqrt(next_square)):
            return next_square

def find_next_square(x):
    return int(math.sqrt(x) + 1) ** 2

    # or:
    # return math.floor(math.sqrt(x) + 1) ** 2

def find_next_square(x):
    i = 1
    while x >= i ** 2:
        i += 1
    return (i) ** 2


'''
Write a function change_case(s) that takes in a alphabetical string s and returns a string that is same as s but with all the cases changed.
You may want to use chr() or ord() for this question.
'''

def change_case(s):
    result = ""
    i = 0
    while len(result) < len(s):
        if s[i] == s[i].lower():
            result += s[i].upper()
        elif s[i] == s[i].upper():
            result += s[i].lower()
        i += 1
    return result

def change_case(s):
    result = ""
    i = 0
    while i < len(s):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            result += chr(ord(s[i]) + 32)
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            result += chr(ord(s[i]) - 32)
        i += 1
    return result

def change_case(s):
    return s.swapcase()

# print(change_case("aBcDeFgHiJkLmNoP123456789"))


'''
Write a function remove_vowels(s) that takes in a string s and returns a string that is same as s but with all the vowels removed.
'''

def remove_vowels(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i] not in "aeiouAEIOU":
        # if s[i].lower() not in "aeiou":
            result += s[i]
        i += 1
    return result

# print(remove_vowels("qwertyui"))


'''
Write a function foo1(s) that takes in a string s and returns an inverse version of string s 
if s contains digit(s) else returns the same string s with all the vowels removed.

Consider to use function isdigit().
'''

def foo1(s):
    # check if got digit
    # alternatively can create a function check_number() to return whether true or false
    # def check_number(s):
    #     i = 0
    #     while i < len(s):
    #         if s[i].isdigit():
    #             return True
    #         i += 1
    #     return False

    contains_digit = False
    i = 0
    while i < len(s):
        if s[i].isdigit():
            contains_digit = True
        i += 1
    
    result = ""
    if contains_digit:
        i = -1
        while i >= -len(s):
            result += s[i]
            i -= 1
        return result
    else:
        i = 0
        while i < len(s):
            if s[i] not in "aeiouAEIOU":
                result += s[i]
            i += 1
        return result
    
# print(foo1("1234567890"))
# print(foo1("qwertyuiopasdfghjklzxcvbnm"))


'''
Write a function foo2(s1, s2) that takes in two strings s1, s2 and returns a combined string 
where its 1st character came from 1st character of s1, its 2nd character came from 1st character 
of s2, 3rd character came from the 2nd charater of s1 and so on.


if there is no more characters to pick from the shorter string, the function will append the remaining 
characters from the longer string to the returned string
e.g. foo2("1234567", "abcd") returns "1a2b3c4d567"
'''

def foo2(s1, s2):
    i = 0
    result = ""
    if len(s1) > len(s2):
        longer, shorter = s1, s2
    else:
        longer, shorter = s2, s1
    while i < len(shorter):
        result += s1[i] + s2[i]
        i += 1
    result += longer[i:]
    return result

def foo2(s1, s2):
    i = 0
    result = ""
    while i < len(s1) and i < len(s2):
        result += s1[i] + s2[i]
        i += 1
    result += s1[i:] + s2[i:]
    return result

def foo2(s1, s2):
    result = ""
    i = 0
    min_len = min(len(s1), len(s2))
    while i < min_len:
        result += s1[i] + s2[i]
        i += 1
    return result + s1[min_len:] + s2[min_len:]

print(foo2("1234567", "abcdefg"))

'''
Write a function get_nth_digit(k, n) that takes in two positive integer k, n and returns the nth 
digit of the given number k counted from the back where length of k is greater or equal to n
'''

def get_nth_digit(k, n):
    if len(str(k)) >= n:
        return int(str(k)[-n])

def get_nth_digit(k, n):
    i = 1
    while i < n:
        k //= 10
        i += 1
    return k % 10

def get_nth_digit(k, n):
    return (k // (10 ** (n - 1))) % 10 # lol

print(get_nth_digit(375416, 2))