# all values in euro, fractions are calculated mathematically. Not "bank"-mathematically!
# 12 months per year are assumed

initialAmount = 0 # in Euro
ratePerMonth = 200 # in Euro; added twelve times
forecastDuration = 10 # in years
expectedInterest = 10 # in percent; is added once at the end of every year; not per month!

def determineFinalAmount():

    for year in range(0, forecastDuration):
        print("year " + str(year+1) + ":")




# test call
determineFinalAmount()
