# quick check how a loan could be used to buy ETF
# I am not really convinced, but naively the question is: should the ETF not outgrow (quickly) the current low itnerest rates?
# (83 for 1k for 12 months they say)
# ------------------------------------------------------------------------------
# TODO
# * add unit-testing
# * monthly rate is actually a direct result of "start Amout divided by monthsToRun" - plan is to use this fully for financial growth
#   but what happens if it zeroes? and there is no "putback"?
# * add also a reminder of the fiscal tax? (25%?)

def loanFondsPrinter(startAmount = 1000, monthlyRates = 83, etfGrowthAnuallyInPercent = 12, monthsToRun = 12):
    # start at zero, then do the rates; first rate at 1
    growthPerMonthFactor = (etfGrowthAnuallyInPercent / 12.0) / 100.0 + 1.0
    amount = startAmount
    oneLineOutput = ""
    #print("day 0 amount:", amount, "growthPerMonthFactor:", growthPerMonthFactor)
    for month in range(1, monthsToRun+1):
        # to keep it conservative: first deduct, then increase the rest by the gain
        amount -= monthlyRates
        amount *= growthPerMonthFactor
        # since you can't have negative amounts on an ETF account, stop calculating the interest by growth
        # TODO this looks wrong; move above line 13
        if amount < 0:
            amount = 0
        #print("month", month, amount)
        oneLineOutput += str(amount) + ";"
    #print("remainder:", amount)
    #print("oneLineOutput:", oneLineOutput)
    print(oneLineOutput.replace(".", ",")) # god save Excel ..

# ------------------------------------------------------------------------------
# never let this see any developer xD but quick results are needed
#print("loanFondsPrinter(20000, 850 + 300, 10, 24)")
loanFondsPrinter(20000, 850 + 300, 10, 24)
#print("loanFondsPrinter(30000, 1275 + 300, 10, 24)")
loanFondsPrinter(30000, 1275 + 300, 10, 24)
#print("loanFondsPrinter(20000, 571 + 300, 10, 36)")
loanFondsPrinter(20000, 571 + 300, 10, 36)
#print("loanFondsPrinter(30000, 857 + 300, 10, 36)")
loanFondsPrinter(30000, 875 + 300, 10, 36)
# ------------------------------------------------------------------------------
# 19007,083333333332;18005,89236111111;16996,358130787034;15978,411115210258;14951,981207837009;13916,997717902317;12873,389365551502;11821,084276931098;10760,009979238857;9690,093395732514;8611,260840696952;7523,438014369426;6426,549997822504;5320,521247804359;4205,275591536061;3080,736221465528;1946,825689977741;803,4659040608888;0;0;0;0;0;0;
# 28661,875;27312,598958333332;25952,078949652776;24580,221274233216;23196,931451518492;21802,11421361448;20395,673498727934;18977,512444550666;17547,53338158859;16105,63782643516;14651,726474988787;13185,699195613694;11707,455022243807;10216,892147429171;8713,907915324415;7198,398814618785;5670,260471407275;4129,387642002335;2575,674205685688;1009,0131573997353;0;0;0;0;
# 19288,408333333333;18570,88673611111;17847,38579224537;17117,855673847414;16382,246137796143;15640,506522277778;14892,585743296759;14138,432291157564;13377,99422691721;12611,219178808185;11838,054338631586;11058,446458120183;10272,341845271185;9479,686360648444;8680,425413653847;7874,503958767629;7061,86649175736;6242,457045855337;5416,219187904131;4583,096014469998;3743,030147923915;2895,9637324899477;2041,8384302606971;1180,5954171795363;312,17537898936575;0;0;0;0;0;0;0;0;0;0;0;
# 29065,208333333332;28122,62673611111;27172,190292245366;26213,833544680743;25247,490490886416;24273,09457831047;23290,578699796388;22299,875188961356;21300,915815536035;20293,631780665502;19277,95371217105;18253,811659772473;17221,135090270578;16179,8528826895;15129,89332337858;14071,1841010734;13003,65230191568;11927,224404431643;10841,826274468573;9747,383160089144;8643,81968642322;7531,059850476746;6409,027015897385;5277,64390769653;4136,832606927334;2986,5145453183954;1826,6104998627154;657,0405873615714;0;0;0;0;0;0;0;0;
