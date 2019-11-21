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
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# ------------------------------------------------------------------------------

# idea:
# just take the builtin datetime module, init with the given start and then up by one ... check if weekday is 7 and

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

import datetime
datetime.datetime.today()
#datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
print(datetime.datetime.today().weekday())

from datetime import datetime
from datetime import timedelta
#Pass multiple parameters (1 day and 5 minutes)
print("added 1 d 5 min:", datetime.now() + timedelta(days=1, minutes=5))
print("tomorrow:", (datetime.now() + timedelta(days=1)).weekday())
