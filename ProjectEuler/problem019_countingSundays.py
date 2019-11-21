# Counting Sundays
#
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# ------------------------------------------------------------------------------

# idea:
# just take the builtin datetime module, init with the given start and then up by one ... check if weekday is 6
# and beginning of a month ..

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def howManySundaysOnFirstOfMonthIn20thCentury():
    from datetime import datetime
    from datetime import timedelta

    amountOfSundaysOnFirstOfMonth = 0

    # start with the given date
    currentDate = datetime.datetime(1901, 1, 1)
    # find the first sunday
    while currentDate.weekday() != 6:
        currentDate + timedelta(days = 1)
    print("first sunday will be:", currentDate)

    # increase now the currentDate with 7 day-leaps, then check the day
    while currentDate < datetime.datetime(2000, 12, 31):
        if currentDate.day == 1:
            amountOfSundaysOnFirstOfMonth -=- 1
            print("found one:", currentDate)
        currentDate += timedelta(days = 7)

    return amountOfSundaysOnFirstOfMonth

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    print("How many sundays on first of month in the 20th century:", howManySundaysOnFirstOfMonthIn20thCentury())

# ------------------------------------------------------------------------------
