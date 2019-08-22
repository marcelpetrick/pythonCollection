# # Python code to demonstrate the working of
# # calendar() function to print calendar
#
# # importing calendar module
# # for calendar operations
# import calendar
#
# # using calender to print calendar of year
# # prints calendar of 2018
# print("The calender of year 2018 is : ")
# print(calendar.calendar(2018, 2, 1, 6))
# cal = calendar.calendar(2109, 1, 1, 1)
# print(cal)
#
#
# # taken from https://www.geeksforgeeks.org/python-calendar-module/
# # note sure if this is helpful
#
# # needed is some iterate-able calender, which has a given start-time, then strides over the days
#
# import time
#
# ticks = time.localtime()
# # --> ticks: time.struct_time(tm_year=2019, tm_mon=8, tm_mday=20, tm_hour=17, tm_min=1, tm_sec=32, tm_wday=1, tm_yday=232, tm_isdst=1)
#
# print("ticks:", ticks)
#
# # https://o7planning.org/de/11443/anleitung-python-date-time
# fakedTime = (2019, 8, 20, 0, 0, 0, 0, 0, 0)
# ticks = time.mktime(fakedTime)
# print("fakedTime:", fakedTime)
# print("ticks:", ticks)

# question: how to jump by "one day"?
# http://www.pressthered.com/adding_dates_and_times_in_python/
from datetime import datetime
from datetime import timedelta
#Pass multiple parameters (1 day and 5 minutes)
print("added 1 d 5 min:", datetime.now() + timedelta(days=1, minutes=5))

# algo:
# read file as input
# determine the "lowest timepoint as start" (eg. current state); maybe sort before the fixed dates
# step with 1 day setting over the time and trigger the actions

# 20190821:
# just implement the prototype-algo to see if this is working

class TransactionItem:
    name = "uninitialized item"
    triggerType = "not set" # once, daily, monthly, yearly
    amount = 0
    date = datetime.today()

    # default ctor
    def __init__(self, name, triggerType, amount, date):
        self.name = name
        self.triggerType = triggerType
        self.amount = amount
        # convert the date to a real type
        self.date = datetime.fromisoformat(date)

    # self representation
    def __repr__(self):
        return self.name + "|" + self.triggerType + "|" + str(self.amount) + "|" + str(self.date)

    # quite simple function to check depending on the set type if the transaction-item will trigger today
    def willTriggerToday(self, today):
        if self.triggerType == "daily":
            # no further checks needed
            return True

        if self.triggerType == "monthly":
            if today.day == self.date.day:
                return True

        if self.triggerType == "yearly":
            if today.day == self.date.day and today.month == self.date.month:
                return True

        if self.triggerType == "once":
            if today.day == self.date.day and today.month == self.date.month and today.year == self.date.year:
                return True

        if ["daily", "monthly", "yearly", "once"].__contains__(self.triggerType):
            return False

        raise Exception("not handle-able triggerType!")

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# about the datetime.fromisoformat throws on year 0000 and out of range error
# https://www.techatbloomberg.com/blog/work-dates-time-python/

# example transactions
# idea for the type-info inside the date is: if a column is zero, then this means "recurring"
# hint: this idea did not work out: because then the datetime-parsing complains about invalid format; therefore replace with the first valid one: the 1.
# but this leads to issues with "1" for real date and "1" as placeholder. So the type-information is really needed.
entry1 = TransactionItem("consumed food", "daily", -5, "0001-01-01") # starting from today; every day 5 kuan loss
entry2 = TransactionItem("salary", "monthly", +666, "0001-01-02") # test for the second of the month
entry3 = TransactionItem("birthday", "yearly", +123, "0001-09-05")
entry0 = TransactionItem("current state", "once", 1000, "2019-08-24")
transactions = [entry0, entry1, entry2, entry3]

# print with enumeration
print("--- transactions ----")
for entry in range(len(transactions)):
    print(entry, transactions[entry])

#-------- test run of the "program" --------
startDate = datetime.fromisoformat("2019-08-22")
currentDateTime = startDate
print("starting with:", currentDateTime)

currentCash = 0

# "walks" over the next twenty days :)
print("---------------------------------------")
for i in range(20):
    # check for all transactions if they trigger; and if, then evaluate
    appliedTransactions = ""  # also print what has happened
    change = 0 # track the daily change
    for item in transactions:
        if item.willTriggerToday(currentDateTime):
            currentCash += item.amount
            appliedTransactions += item.name + ";"
            change += item.amount

    # print the current state (datetime just as date)
    print(i,": date=", currentDateTime.strftime('%Y-%m-%d'), "budget=", currentCash, "triggers=", appliedTransactions,
          "change=", change)
    currentDateTime += timedelta(days=1)
