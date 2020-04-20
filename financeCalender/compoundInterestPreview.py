# all values in euro, fractions are calculated mathematically. Not "bank"-mathematically!
# 12 months per year are assumed

initialAmount = 0 # in Euro
ratePerMonth = 500 # in Euro; added twelve times
forecastDuration = 10 # in years
expectedInterest = 10 # in percent; is added once at the end of every year; not per month!

def determineFinalAmount():

    currentAmount = initialAmount
    for year in range(0, forecastDuration):
        print("year " + str(year+1) + ":")
        # invested
        for month in range(0, 12):
            currentAmount += ratePerMonth

        # gathered by interest (attention: problem is that this is calculated on the full amount, which is wrong, slightly, but wrong)
        currentAmount = (1.0 + expectedInterest / 100.0) * currentAmount

        print(str(currentAmount) + "€")

# test call
determineFinalAmount()

# result:
# year 10:
# 105187.00236660003€
