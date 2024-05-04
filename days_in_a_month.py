def is_leap(year):
    """Check if the year is a leap year"""
    if year % 4 == 0:
       if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
       else:
            return True
    else:
       return False
   
def days_in_month(year, month):
    """"Checks the number of days in a month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_or_not = is_leap(year)
    if leap_or_not == True:
        if month == 2:
            return month_days[month - 1] + 1
        else:
            return month_days[month - 1]
    else:
        return month_days[month - 1]
    
# OR

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#     if is_leap(year) and month == 2:
#             return month_days[month - 1] + 1
#     return month_days[month - 1]
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)