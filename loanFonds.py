# quick check how a loan could be used to buy ETF
# I am not really convinced, but naively the question is: should the ETF not outgrow (quickly) the current low itnerest rates?
# (83 for 1k for 12 months they say)

def loanFondsPrinter(startAmount = 1000, monthlyRates = 83, etfGrowthAnuallyInPercent = 12, monthsToRun = 12):
    # start at zero, then do the rates; first rate at 1
    growthPerMonthFactor = (etfGrowthAnuallyInPercent / 12.0) / 100.0 + 1.0
    amount = startAmount
    print("day 0 amount:", amount, "factor:", growthPerMonthFactor)
    for month in range(1, monthsToRun+1):
        # to keep it conservative: first deduct, then increase the rest by the gain
        amount -= monthlyRates
        amount *= growthPerMonthFactor
        # since you can't have negative amounts on an ETF account
        if amount < 0:
            amount = 0
        print("month", month, amount)
    print("remainder:", amount)

# added 100e as "additionally taken out
loanFondsPrinter(10000, 285 + 0, 15, 36)
# run: 285; 15%
# ..
# month 30 4090.639184306465
# month 31 3853.2096741102955
# month 32 3612.812295036674
# month 33 3369.4099487246326
# month 34 3122.96507308369
# month 35 2873.4396364972363
# month 36 2620.795131953452
# remainder: 2620.795131953452

# run: loanFondsPrinter(10000, 285 + 100, 15, 36)
# ..
# month 29 812.2305859245125
# month 30 432.57096824856893
# month 31 48.16560535167604
# month 32 0
# month 33 0
# month 34 0
# month 35 0
# month 36 0
# remainder: 0
