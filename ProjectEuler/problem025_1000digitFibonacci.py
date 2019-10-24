# 1000-digit Fibonacci number
#
# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# copied from one of my previous solutions :)
def getFibGen():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b

# ------------------------------------------------------------------------------

# straight forward implementation for solving the challenge
import time
startTime = time.time()
pos = 0
fibGen = getFibGen()
while True:
    pos = pos + 1
    fib = next(fibGen)
    #print("fib:", fib)
    if(len(str(fib)) >= 1000):
        print("found: wanted fib is:", fib)
        break

print("pos of the first component is:", pos)
print("computation took", time.time() - startTime, "s")

# ------------------------------------------------------------------------------
# ..
# found: wanted fib is: 1070066266382758936764980584457396885083683896632151665013235203375314520604694040621889147582489792657804694888177591957484336466672569959512996030461262748092482186144069433051234774442750273781753087579391666192149259186759553966422837148943113074699503439547001985432609723067290192870526447243726117715821825548491120525013201478612965931381792235559657452039506137551467837543229119602129934048260706175397706847068202895486902666185435124521900369480641357447470911707619766945691070098024393439617474103736912503231365532164773697023167755051595173518460579954919410967778373229665796581646513903488154256310184224190259846088000110186255550245493937113651657039447629584714548523425950428582425306083544435428212611008992863795048006894330309773217834864543113205765659868456288616808718693835297350643986297640660000723562917905207051164077614812491885830945940566688339109350944456576357666151619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816
# pos of the first component is: 4782
# computation took 0.015620946884155273 s
#
# ------------------------------------------------------------------------------
# Congratulations, the answer you gave to problem 25 is correct.
#
# You are the 143997th person to have solved this problem.
