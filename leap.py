year = int(input("Enter a year: "))

# Leap year conditions:
# 1. Divisible by 400 - Leap year
# 2. Divisible by 4 but not by 100 - Leap year
# Otherwise - Not a leap year
#year % 4 = 0  year % 100 ==0 

if (year % 4 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
