#######################################
# Mission 1: Date Calculator Template #
#######################################

#############################
# Task 1 - Helper Functions #
#############################

###########
# Task 1a #
###########
def is_leap_year (year):
    """
    is_leap_year (year) -> boolean
    Function takes in a specific year.
    Returns True if it is a leap year, False otherwise.
    """
    ## Your Code Here ##
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

# print (is_leap_year(2000)) # True
# print (is_leap_year(1900)) # False
# print (is_leap_year(1984)) # True
# print (is_leap_year(2015)) # False

###########
# Task 1b #
###########
def days_in_month (month):
    """
    days_in_month (month) -> int
    Function takes in a specific month.
    Returns number of days in that month for a normal year.
    
    Note: This function needs not to consider leap year.
    """
    ## Your Code Here ##
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28

#Print out number of days in each month:
# for i in range (1, 13):
#     print (i, days_in_month(i))

###########
# Task 1c #
###########
def num_of_leap_years (start_year, end_year):
    """
    num_of_leap_years (start_year, end_year) -> int
    Function takes in 2 years: start_year (inclusive) and end_year (exclusive).
    Returns number of leap years in between the 2 years.
    """
    ## Define num_of_leap_years using iterative loop ##
    ## Your Code Here ##
    result = 0
    for i in range(start_year, end_year):
        if is_leap_year(i):
            result += 1
    return result


# print (num_of_leap_years(2010, 2016)) # 1
# print (num_of_leap_years(2008, 2013)) # 2
# print (num_of_leap_years(1900, 2016)) # 28

###########
# Task 1d #
###########
def is_valid_date (date):
    """
    is_valid_date (date) -> boolean
    Function checks if the date entered is a valid date.
    Returns True if it's valid, False otherwise.
    """
    ## Your Code Here ##
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])
    if is_leap_year(year) and month == 2:
        if day == 29:
            return True
    if day <= days_in_month(month):
        return True
    
    return False

# print (is_valid_date("29022016")) # True
# print (is_valid_date("31042015")) # False
# print (is_valid_date("29022015")) # False

###########################
# Task 2 - Main Functions #
###########################

###########
# Task 2a #
###########
def num_of_days_from_1900 (date):
    """
    num_of_days_from_1900 (date) -> int
    Function takes in a date.
    Returns the number of days of the input date after "01011900".
    """
    ## Your Code Here ##
    result = 0
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])

    # accounts for full years
    if year > 1901:
        result += ((year - 1900 - num_of_leap_years(1900, year)) * 365 + num_of_leap_years(1900, year) * 366) - 1
        # print("no. of leap years,", "days in full years: ", num_of_leap_years(1900, year), result)

    # accounts for full months in remaing year
    # print("year", year)
    for i in range(1, month):
        if i == 2 and is_leap_year(year):
            # print("leap year, add 29")
            result += 29
        else:
            # print("days in month", i, ":",  days_in_month(i))
            result += days_in_month(i)
        # print("month,", "current total: ", i, result)
            
    # since 01/01/1900 is not counted
    if year == 1900:
        result -= 1
    
    # accounts for remaining days
    result += day

    return result

# print (num_of_days_from_1900("30011900")) # 29
# print (num_of_days_from_1900("28021900")) # 58
# print (num_of_days_from_1900("01031904")) # 1520
# print (num_of_days_from_1900("31012016")) # 42398

###########
# Task 2b #
###########
def days_between_2_dates (date1, date2):
    """
    days_between_2_dates (date1, date2) -> int
    Function takes in 2 dates.
    Returns the number of days in between the 2 dates.
    """
    ## Your Code Here ##
    result = 0

    day1 = int(date1[:2])
    month1 = int(date1[2:4])
    year1 = int(date1[4:])
    day2 = int(date2[:2])
    month2 = int(date2[2:4])
    year2 = int(date2[4:])

    # first month
    if month1 == 2 and is_leap_year(year1):
        days_in_month1 = 29
    else:
        days_in_month1 = days_in_month(month1)

    for i in range(year1, year2+1):
        # print("\ncurrent year:", i, "leap status:", is_leap_year(i))

        # final remaining year - wrote this in front in case year1 == year2
        if i == year2:
            if month1 == month2:
                # print("same month same year so find difference")
                return day2 - day1
            
            if i == year1: # IF IT IS ALSO THE STARTING YEAR
                # print("same year yay!", "month1:", month1)
                
                result += (days_in_month1 - day1)
                # print("STARTING month:", month1, "added:", "difference", "result:", result)

                # full months in between
                for j in range(month1+1, month2):
                    if j == 2 and is_leap_year(i):
                        result += 29
                        # print("current month:", j, "added: 29 result:", result)
                    else:
                        result += days_in_month(j)
                        # print("current month:", j, "added:", days_in_month(j), "result:", result)
            else:
                # full months - considering the ENTIRE year is full
                for j in range(1, month2):
                    if i == year1 and j == month1: # IF IT IS FIRST MONTH OF THE FIRST YEAR
                        result += day1
                    elif j == 2 and is_leap_year(i):
                        result += 29
                        # print("current month:", j, "added: 29 result:", result)
                    else:
                        result += days_in_month(j)
                        # print("current month:", j, "added:", days_in_month(j), "result:", result)
            # FINAL MONTH
            if not (year1 == year2 and month1 == month2):
                result += day2
                # print("final month:", month2, "added:", day2, "result:", result)

        # first year (and still got years after that)
        elif i == year1:
            # current month
            result += (days_in_month1 - day1)
            # print("starting month:", month1, "added:", "difference", "result:", result)

            # remaining months
            for j in range(month1+1, 13):
                if j == 2 and is_leap_year(i):
                    result += 29
                    # print("current month:", j, "added: 29 result:", result)
                else:
                    result += days_in_month(j)
                    # print("current month:", j, "added:", days_in_month(j), "result:", result)

        # full years
        elif year1 < i < year2:
            for j in range(1, 13):
                if j == 2 and is_leap_year(i):
                    result += 29
                    # print("current month:", j, "added: 29 result:", result)
                else:
                    result += days_in_month(j)
                    # print("current month:", j, "added:", days_in_month(j), "result:", result)

    return result

# print (days_between_2_dates("15041984", "26102000")) # 6038
# print (days_between_2_dates("15041984", "26102000")) # 6038
# print(days_between_2_dates("03032024", "08052024")) # just to test whether same year works
# print (days_between_2_dates("26102000", "31012016")) # 5575

###########
# Task 2c #
###########
def add_n_days_after_1900 (days):
    """
    add_n_days_after_1900 (days) -> date
    Function takes in a specific number of days.
    Returns the date after adding the input number of days to "01011900".
    """
    ## Your Code Here ##
    day_count = 1
    max_days = 31
    month_count = 1
    year_count = 1900

    for i in range(days):
        day_count += 1

        # next month / year
        if day_count > max_days:
            day_count = 1
            month_count += 1
            if month_count > 12:
                month_count = 1
                year_count += 1
            
            # updates maximum days in month
            if month_count == 2 and is_leap_year(year_count):
                max_days = 29
                # print("IS LEAP YEAR")
            else:
                max_days = days_in_month(month_count)
                # print("month:", month_count, "max days:", max_days)
    
    # return the date in format ddmmyyyy
    return str(day_count).zfill(2) + str(month_count).zfill(2) + str(year_count)


# print (add_n_days_after_1900(30)) # "31011900"
# print (add_n_days_after_1900(31)) # "01021900"
# print (add_n_days_after_1900(59)) # "01031900"
# print (add_n_days_after_1900(1519)) # "29021904"
# print (add_n_days_after_1900(1520)) # "01031904"

###########
# Task 2d #
###########
def add_n_days_from_a_date (date, days):
    """
    add_n_days_from_a_date (date, days) -> date
    Function takes in a date and a specific number of days.
    Returns the date after adding the input number of days to the input date.
    """
    ## Your Code Here ##
    day_count = int(date[:2])
    month_count = int(date[2:4])
    year_count = int(date[4:])
    if month_count == 2 and is_leap_year(year_count):
        max_days = 29
    else:
        max_days = days_in_month(month_count)

    for i in range(days):
        day_count += 1

        # next month / year
        if day_count > max_days:
            day_count = 1
            month_count += 1
            if month_count > 12:
                month_count = 1
                year_count += 1
            
            # updates maximum days in month
            if month_count == 2 and is_leap_year(year_count):
                max_days = 29
                # print("IS LEAP YEAR")
            else:
                max_days = days_in_month(month_count)
                # print("month:", month_count, "max days:", max_days)
    
    # return the date in format ddmmyyyy
    return str(day_count).zfill(2) + str(month_count).zfill(2) + str(year_count)

# print (add_n_days_from_a_date ("15041984", 6038)) # 26102000
# print (add_n_days_from_a_date ("26102000", 6038)) # 08052017

###########
# Task 2e #
###########
def weekday_of_date (date):
    """
    weekday_of_date (date) -> str
    Function takes in a date.
    Returns the weekday of the input date.
    """
    ## Your Code Here ##
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])

    # Gauss's algorithm (https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week)

    # based on table of month offsets
    if month == 1:
        m = 0
    elif month == 2:
        m = 3
    elif is_leap_year(year):
        m = [4, 0, 2, 5, 0, 3, 6, 1, 4, 6][month - 3]
    else:
        m = [3, 6, 1, 4, 6, 2, 5, 0, 3, 5][month - 3]
        
    d = (day + m + 5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 * ((year - 1) % 400)) % 7
    d -= 1 # so Monday is 0, Tuesday is 1, etc.

    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][d]

# print (weekday_of_date("01011900")) # "Monday"
# print (weekday_of_date("02011900")) # "Tuesday"
# print (weekday_of_date("31012016")) # "Sunday"

############################
# Task 3 - Date Calculator #
############################
def date_calculator():
    """
    date_calculator ()
    Function takes in an input from user and performs the functions accordingly.
    """
    done = False
    while not done:
        # Prepare Menu
        print ("-----------------------------------------")
        print ("Welcome to date calculator")
        print ("  1. Calculate number of days between 2 dates.")
        print ("  2. Add n days from a date.")
        print ("  3. Find weekday of a date.")
        print ("  4. Exit the programme.\n")
        print ("**Please note the format of date should follow the format of 'DDMMYYYY'\n")
        
        # Get Input
        option = int(input ("Select a function: "))
        
        ## Your Code Here ##
        if option == 1:
            date1 = input("Enter the first date: ")
            date2 = input("Enter the second date: ")
            print("Number of days between the two dates:", days_between_2_dates(date1, date2))
        elif option == 2:
            date = input("Enter the date: ")
            days = int(input("Enter the number of days to add: "))
            print("The date after adding", days, "days:", add_n_days_from_a_date(date, days))
        elif option == 3:
            date = input("Enter the date: ")
            print("The weekday of the date is:", weekday_of_date(date))
        elif option == 4:
            print("Exiting the programme.")
            done = True

date_calculator()
