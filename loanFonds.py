# quick check how a loan could be used to buy ETF
# I am not really convinced, but naively the question is: should the ETF not outgrow (quickly) the current low itnerest rates?
# (83 for 1k for 12 months they say)

def loanFondsPrinter(startAmount = 1000, monthlyRates = 83, etfGrowthAnuallyInPercent = 12):
    # start at zero, then do the rates; first rate at 1
    growthPerMonthFactor = (etfGrowthAnuallyInPercent // 12.0) / 100.0 + 1.0
    amount = startAmount
    print("day 0 amount:", amount, "factor:", growthPerMonthFactor)
    for month in range(1,12+1):
        # to keep it conservative: first deduct, then increase the rest by the gain
        amount -= monthlyRates
        amount *= growthPerMonthFactor
        print("month", month, amount)

loanFondsPrinter(10000, 840, 20) # 508 remainder

# todo make the amount of months interactive
