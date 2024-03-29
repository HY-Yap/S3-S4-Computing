# For data validation

def validate_option(msg):
    done = False
    while not done:
        option = input(msg)
        if option == "1" or option == "2":
            done = True
            return option
        else:
            print("Invalid input. Please enter either 1 or 2.")

def validate_base(msg):
    done = False
    while not done:
        base = input(msg)
        try:
            base = int(base)
            done = True
            if base == 0:
                done = False
                print("Not a valid base number. Please input an integer greater than 0.")
        except:
            print("Not a valid base number. Please input an integer greater than 0.")
    return base

def validate_input(msg, base):
    done = False
    while not done:
        input_ = input(msg)
        if check(input_, base) == True:
            done = True
        else:
            print("Error: certain digit(s) are not in the selected base " + str(base) + " number system.")
            print("Please ensure that your input contains only the following characters: " + check(input_, base))
    return input_

        
def check(input_, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_system = digits[:base]
    for char in input_:
        if char not in base_system:
            return base_system
    return True


# For conversion

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def any_to_den(any_num, base):
    if any_num == "":
        return 0
    else:
        return int(digits.index(any_num[0])) * (base ** (len(any_num) - 1)) + any_to_den(any_num[1:], base)

def den_to_any(den_num, base):
    if den_num == 0:
        return ""
    else:
        return den_to_any(den_num // base, base) + digits[den_num % base]

def base_1_to_2(input_, base1, base2):
    return den_to_any(any_to_den(input_, base1), base2)


# MENU

def menu():
    done = False
    while not done:
        print ("-----------------------------------------")
        print ("Welcome to number converter")
        print ("  1. Convert positive integers between any 2 numeral systems")
        print ("  2. Exit the programme.")

        # Get Input
        option = int(validate_option("\nSelect an option: "))

        # Output
        if option == 1:
            base1 = int(validate_base("\nPlease enter the base of the current number system: "))
            base2 = int(validate_base("\nPlease enter the base of the number system you want to convert to: "))
            input_ = str(validate_input("\nPlease enter what you would like to convert: ", base1))
            print("\n" + input_ + " in base " + str(base2) + " would give " + base_1_to_2(input_, base1, base2))
            print("\nExiting the function \n")

        elif option == 2:
            print("\nExiting the programme.\n")
            done = True

menu()
