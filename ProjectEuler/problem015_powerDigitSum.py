# Power digit sum
#
# Problem 16
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

# ------------------------------------------------------------------------------
# idea:
# * naively compute 2 ** 1000 and then sum up the digits
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
import time

# works fast .. less than 2 s
startTime = time.time()
print(2 ** 10)
print("call to 2 ** 10 took", time.time() - startTime, "s")
startTime = time.time()
print(2 ** 100)
print("call to 2 ** 100 took", time.time() - startTime, "s")
startTime = time.time()
print(2 ** 1000)
print("call to 2 ** 1000 took", time.time() - startTime, "s")
startTime = time.time()
print(2 ** 10000)
print("call to 2 ** 10000 took", time.time() - startTime, "s")
# call to 2 ** 10000 took 0.0 s
startTime = time.time()
print(2 ** 1000000)
print("call to 2 ** 1000000 took", time.time() - startTime, "s")
# call to 2 ** 1000000 took 1.264249324798584 s