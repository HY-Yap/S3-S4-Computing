'''Write a function sum_digits(x) that takes in a non-negative integer x and returns the sum of all its digits.'''

def sum_digits(x):
    str_x = str(x)
    total = 0
    for i in range(len(str_x)):
        total += int(str_x[i])
    return total

def sum_digits(x):
    ans = 0
    for digit in (str(x)):
        ans += int(digit)
    return ans

# alternative method (using math), for loop
def sum_digits(x):
    result = 0
    for i in range(len(str(x))):
        result += x % 10
        x //= 10
    return result

# alternative method, recursion :D
def sum_digits(x):
    if x < 10:
        return x
    else:
        return x % 10 + sum_digits(x // 10)
    
print(sum_digits(85084))


'''Write a function sum_odd_digits(x) that takes in a non-negative integer x and returns the sum of all its odd digits.'''

def sum_odd_digits(x):
    str_x = str(x)
    total = 0
    for i in range(len(str_x)):
        if int(str_x[i]) % 2 == 1:
            total += int(str_x[i])
    return total


'''
Write a function change_case(s) that takes in a alphabetical string s and 
returns a string that is same as s but with all the cases changed.

You may want to use chr() or ord() for this question.
'''

def change_case(s):
    result = ""
    for i in range(len(s)):
        if s[i].islower():
            result += s[i].upper()
        elif s[i].isupper():
            result += s[i].lower()
    return result


'''Write a function remove_vowels(s) that takes in a string s and returns a string that is same as s but with all the vowels removed.'''

def remove_vowels(s):
    result = ""
    for i in range(len(s)):
        if s[i] not in "AEIOUaeiou":
            result += s[i]
    return result


'''
Write a function foo1(s) that takes in a string s and returns an inverse version of string s 
if s contains digit(s) else returns the same string s with all the vowels removed.

Consider to use function isdigit().
'''

def foo1(s):
    result = ""
    # runs through entire code and check if contains digit
    has_digit = False
    for i in range(len(s)):
        if s[i].isdigit():
            has_digit = True
    if has_digit:
        n = -1
        for i in range(len(s)):
            result += s[n]
            n -= 1
        return result
    else:
        for i in range(len(s)):
            if s[i] not in "AEIOUaeiou":
                result += s[i]
        return result


'''
Write a function foo2(s1, s2) that takes in two strings s1, s2 and returns a combined string 
where its 1st character came from 1st character of s1, its 2nd character came from 1st character of 
s2, 3rd character came from the 2nd charater of s1 and so on.


if there is no more characters to pick from the shorter string, the function will append the 
remaining characters from the longer string to the returned string
e.g. foo2("1234567", "abcd") returns "1a2b3c4d567"
'''


def foo2(s1, s2):
    result = ""
    if len(s2) < len(s1):
        shorter = s2
        longer = s1
    else:
        shorter = s1
        longer = s2
    if s1 != "" and s2 != "":
        for i in range(len(shorter)):
            result += s1[i] + s2[i]
            stopped_index = i+1
        if len(longer) - len(shorter) == 0:
            return result
        else:
            for i in range(len(longer) - stopped_index):
                result += longer[stopped_index+i]
            return result
    else:
        return longer
