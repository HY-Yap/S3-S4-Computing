# Write a function insert_space(s) that takes in a string s, add a space in between each character.

def insert_space(s):
    result = ""
    for char in s:
        result += char + " "
    return result[:-1]

# print(insert_space("Hello"))
# print(insert_space("RV"))


# Write a function surround_by_hc(s) that takes in a string s, add a space in between each character, and returns the string surrounded by letters "H" and "C".
# You may consider to use the new line character "\n".

def surround_by_hc(s):
    result = ""
    for char in s:
        result += char + " "
    result = result[:-1] # slice off the last space

    surround = ""
    is_h = True
    i = 1
    while i <= len(result) + 4:
        if is_h:
            surround += "H"
        else:
            surround += "C"
        is_h = not is_h
        i += 1

    result = surround + "\n" + "H " + result + " C" + "\n" + surround
    return result

def surround_by_hc(s):
    # form the midle row
    ans = ""
    for i in range(len(s)):
        ans += s[i]
        if i != len(s) - 1:
            ans += " "
    surrounded = "H " + ans + " C"
    
    # form the top and bottom border
    border = ""
    for i in range(len(surrounded)):
        if i % 2 == 0:
            border += "H"
        else:
            border += "C"
    
    # combine
    return border + "\n" + surrounded + "\n" + border

# print(surround_by_hc("Python"))


# Write a function string_pyramid(s) that takes in a string s, and returns the string in the following format.
# You may consider to use the new line character "\n".
# In the following example "_" represents space characters " ",
# ____H____   
# ___H_e___
# __H_e_l__
# _H_e_l_l_
# H_e_l_l_o

def string_pyramid(s):
    total_char = len(s) * 2 - 1 # length of final line
    surround = total_char // 2
    result = " " * surround + s[0] + " " * surround # sets the first line
    for i in range(2, len(s) + 1): # values here represent line no.
        main_text = s[0] + " "
        for j in range(1, i):
            main_text += s[j] + " "
        main_text = main_text[:-1]
        surround -= 1
        result += "\n" + " " * surround + main_text + " " * surround
    return result

def string_pyramid(s):
    n = len(s)
    pyramid = []
    for i in range(n):
        line = " " * (n - i - 1)
        for j in range(i + 1):
            if j == i:
                line += s[j]
            else:
                line += s[j] + " "
        line += " " * (n - i - 1)
        pyramid.append(line)
    return "\n".join(pyramid) # \n is a connector to be inserted in between each element

# zhoup way
def string_pyramid(s):
    result = ""
    # iterate through i values from 0 to len(s) exclusive as the row numbers
    for i in range(len(s)):
        # front, back
        front_back = " " * (len(s) - 1 - i)

        # middle, insert space into s[:i+1]
        mid = insert_space(s[:i+1])
        print(mid)

        # combine
        result += front_back + mid + front_back + "\n"
    return result[:-1]

# print(string_pyramid("Hello"))
# print(string_pyramid("Python"))
# print(string_pyramid("Singapore"))


# Define a function factorial(n), which takes a non-negative integer n and return n! as the result.

def factorial(n):
    if n == 0:
        return 1 # stops the recursion
    else:
        return n * factorial(n-1)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# print(factorial(0)) # 1
# print(factorial(1)) # 1 * (1)
# print(factorial(5)) # 5 * (4 * (3 * (2 * (1 * (1)))))


# Write a function pascal_triangle(n) that takes in an integer n, and returns the string in the following format.
# You may assume n <= 5 so that there wont be any 2-digit numbers appearing in your return string. You may want to revise on binomial coefficient.
# You may consider to use the new line character "\n".

# In the following example, n = 5, "_" represents space characters " ".
# ____1____
# ___1_1___   
# __1_2_1__  
# _1_3_3_1_
# 1_4_6_4_1

def pascal_triangle(n):
    prev = "1"
    if n == 0:
        return prev
    
    result = " " * (n - 1) + prev + " " * (n - 1) + "\n"
    
    for i in range(1, n):
        curr = "1"
        for j in range(len(prev) - 1):
            curr += str(int(prev[j]) + int(prev[j+1]))
        curr += "1"

        # print(curr)
        prev = curr
        result += " " * (n - 1 - i) + insert_space(curr) + " " * (n - 1 - i) + "\n"

    return result[:-1]

# using ncr formula
def ncr(n, r):
    return factorial(n) // factorial(n-r) // factorial(r)

def pascal_triangle(n):
    result = ""
    for i in range(n):
        curr = ""
        for j in range(i+1):
            curr += str(ncr(i, j))
        # print(curr)
        result += " " * (n - 1 - i) + insert_space(curr) + " " * (n - 1 - i) + "\n"
    return result[:-1]

print(pascal_triangle(5))
