# quick test: 5x5 matrix with brightness from
# 100% shall be: all 25 led on
# 1 LED would be 4 %; fill up linewise; top-down
# the last one maybe blinks

#------------------------------

def computeMatrix(number):
    returnString = ""

    # newline either by : or with \n
    returnString += "90009:" + "07070:" + "00200:" + "90009:" + "07070:" # for now hardcoded; use something like number//4%25 for the remainder

    # problem: that string can't be auto-converted to Image-type; super weird ..
    return returnString

print(computeMatrix(80))
