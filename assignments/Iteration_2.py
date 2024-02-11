'''
The human DNA is composed of four nucleic acid bases—adenine (A), thymine (T), guanine (G), 
and cytosine (C). In the DNA double helix structure, adenine should always pair with thymine 
(A-T pair), guanine should always pair with cytosine (G-C pair).

Write a function that takes in two strings s1, s2 representing the Nucleic acid double 
helix and returns True if the A-T and G-C pairings are correctly matched, False otherwise. 
s1 and s2 are always of equal length.
'''

def fooDNA(s1, s2):
    for i in range(len(s1)):
        if (s1[i] == "A" and s2[i] != "T") or (s1[i] == "T" and s2[i] != "A"):
            return False
        elif (s1[i] == "G" and s2[i] != "C") or (s1[i] == "C" and s2[i] != "G"):
            return False
    return True 

# print(fooDNA("GATTCCCAAAAATGTCAAAAAATAGGCAAAAAATGCCAAAAAATCCCAAAC", "CTAAGGGTTTTTACAGTTTTTTATCCGTTTTTTACGGTTTTTTAGGGTTTG"))


'''
Write a function that takes in two strings P1, P2 of equal length that represent 
a series of scissors-paper-rock game between player1(P1) and player2(P2) where 
[R-rock, S-scissors, P-Paper].

The funtion returns 'Player 1' if player 1 wins more sets than player 2. If player 2 
wins more, returns 'Player 2'. If both players win the same number of sets, return 'Draw'

'''

def fooSPR(P1, P2):
    player_1 = 0
    player_2 = 0
    for i in range(len(P1)):
        if P1[i] != P2[i]: # if not a tie
            if P1[i] == "R":
                if P2[i] == "S":
                    player_1 += 1
                else:
                    player_2 += 1
            elif P1[i] == "P":
                if P2[i] == "R":
                    player_1 += 1
                else:
                    player_2 += 1
            elif P1[i] == "S":
                if P2[i] == "P":
                    player_1 += 1
                else:
                    player_2 += 1
    if player_1 > player_2:
        return 'Player 1'
    elif player_2 > player_1:
        return 'Player 2'
    elif player_1 == player_2:
        return 'Draw'

# print(fooSPR("RPSSRPPRSS", "SSPRRPPSPR"))


'''
Write a function that takes in a numeric string s (len(s) > 3) and returns True 
if every digit from the 3rd position of the string onward is equal to the least 
significant digit of the sum of its previous two digits, return False otherwise.

For example:

13471
1+3 = 4
3+4 = 7
4+7 = 11 (least significant digit is 1)

So fooSum2digits(13471) should return True.
'''

def fooSum2digits(s):
    string_s = str(s)
    for i in range(2, len(string_s)):
        sum_ = int(string_s[i-1]) + int(string_s[i-2])
        if int(string_s[i]) != sum_ % 10:
            return False
    return True


'''
Write a function that takes in an uppercase alphabetical string s and encode it 
the following way. A->D, B->E, C->F, D->G, ... W->Z, X->A, Y->B, Z->C

You may need to use chr() and ord() to retrieve and convert bewteen 
the unicode and its character
'''

def encrypt(s):
    result = ""
    for char in s:
        encrypted = ord(char) + 3
        if encrypted > 90:
            encrypted = encrypted - 90 + 64
        result += chr(encrypted)
    return result

def encrypt(s):
    encoded_s = ""
    for char in s:
        # (ord(char)- ord("A"): converting letters to numbers of 0 to 5
        # add 3 to this number to shift to the right
        # % 26: for values < 26, it will remain as it is
        # but for values >= 26, it will become 0, 1, 2...
        encoded_s += chr((ord(char)- ord("A") + 3) % 26 + ord("A"))
    return encoded_s

# print(encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


"Write a function that takes in an uppercase alphabetical string s and reverse what was done in Q5."

def decrypt(s):
    result = ""
    for char in s:
        encrypted = ord(char) - 3
        if encrypted < 65:
            encrypted = encrypted + 90 - 64
        result += chr(encrypted)
    return result

def decrypt(s):
    decoded_s = ""
    for char in s:
        decoded_s += chr((ord(char)- ord("A") - 3) % 26 + ord("A"))
    return decoded_s

# print(decrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


'''
Write a function bin_to_dec(s) that takes in a string s consists of only 1s and 0s (no leading zero) and return its decimal equivalent .

You are not allowed to directly convert s to its decimal using int(s, 2). Do it using the calculation method.
'''

def bin_to_dec(s):
    int_s = int(s)
    result = 0
    i = 0
    while int_s > 0:
        result += 2 ** i * (int_s % 10)
        int_s //= 10
        i += 1
    return result

def bin_to_dec(s):
    result = 0
    for bit in range(len(s)):
        # starting from least significant bit
        # [-bit-1] have values -1, -2 ...
        # bit will have values 0, 1, 2 ...
        result += int(s[-bit-1]) * (2 ** bit)
    return result

# using recursion
def bin_to_dec(s):
    if len(s) == 1:
        return int(s)
    else:
        return int(s[0]) * 2 ** (len(s) - 1) + bin_to_dec(s[1:])


# print(bin_to_dec("100")) # expect 4
# print(bin_to_dec("1111")) # expect 15


'''
Write a function that takes in a numeric string s and returns True if there exists a 
consecutive string of digits where the sum of its digits are equal to 15

Hint: need to use while loop

To convert a string to int e.g. int("33") => 33, int("3") => 3

To convert an int to string e.g. str(33) => "33", str(3) => "3"
'''

def foo15(s):
    str_s = str(s)
    start_digit = 0
    while start_digit < len(str_s):
        sum = int(str_s[start_digit])
        i = start_digit + 1
        while i < len(str_s):
            sum += int(str_s[i])
            i += 1
            if sum == 15:
                return True
        start_digit += 1
    return False

def foo15(s):
    for i in range(len(s)):
        temp_sum = 0
        for j in range(i+1, len(s)):
            temp_sum += int(s[j])
            if temp_sum == 15:
                return True
    return False

# sliding window
def foo15(s):
    left = 0
    right = 0
    temp_sum = 0
    while right < len(s):
        if temp_sum < 15:
            temp_sum += int(s[right])
            right += 1
        elif temp_sum > 15:
            temp_sum -= int(s[left])
            left += 1
            
        if temp_sum == 15:
            return True
    return False

# print(foo15("1323322331231"))


'''
Write an function is_saw_teeth (s) that takes a non-empty numerical string s (len(s) >= 3) and returns True when:

All odd position digits in s are either bigger or smaller than its adjacent digits at even positions

Example:

# The 1s digit is smaller than the 2nd digit, the 2nd digit is larger than

#       the 3rd digit and the 3rd digit is smaller than the 4th digit and so on…. 

#       OR

# The 1s digit is larger than the 2nd digit, the 2nd digit is smaller than

#       the 3rd digit and the 3rd digit is larger than the 4th digit and so on…. 

'''

def is_saw_teeth(s):
    str_s = str(s)
    if str_s[0] < str_s[1]:
        check_smaller = True
    elif str_s[0] > str_s[1]:
        check_smaller = False
    elif str_s[0] == str_s[1]:
        return False
    
    i = 2
    while i < len(str_s):
        if check_smaller == True:
            if not int(str_s[i]) < int(str_s[i-1]):
                return False
            check_smaller = False
        elif check_smaller == False:
            if not int(str_s[i]) > int(str_s[i-1]):
                return False
            check_smaller = True
        i += 1

    return True

# a shorter way to do this
def is_saw_teeth(s):
    str_s = str(s)
    check_smaller = int(str_s[0]) < int(str_s[1])
    for i in range(1, len(str_s)):
        if check_smaller and int(str_s[i]) <= int(str_s[i-1]):
            return False
        elif not check_smaller and int(str_s[i]) >= int(str_s[i-1]):
            return False
        check_smaller = not check_smaller
    return True

# zhoup way
def is_saw_teeth(s):
    for i in range(2, len(s)):
        if not ((s[i-2] < s[i-1] and s[i-1] > s[i]) or \
                (s[i-2] > s[i-1] and s[i-1] < s[i])):
            return False
    return True

# another zhoup way
def is_saw_teeth(s):
    for i in range(1, len(s)-1):
        if (int(s[i]) - int(s[i-1])) * (int(s[i+1]) - int(s[i])) >= 0:
            return False
    return True
'''
logic:
1 * 1 = 1 (positive output)
-1 * -1 = 1 (also positive output)
'''

print(is_saw_teeth("1214364"))
print(is_saw_teeth("21212121"))
print(is_saw_teeth("1234567"))
