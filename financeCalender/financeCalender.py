# Python code to demonstrate the working of
# calendar() function to print calendar

# importing calendar module
# for calendar operations
import calendar

# using calender to print calendar of year
# prints calendar of 2018
print("The calender of year 2018 is : ")
print(calendar.calendar(2018, 2, 1, 6))
cal = calendar.calendar(2109, 1, 1, 1)
print(cal)


# taken from https://www.geeksforgeeks.org/python-calendar-module/
# note sure if this is helpful

# needed is some iterate-able calender, which has a given start-time, then strides over the days