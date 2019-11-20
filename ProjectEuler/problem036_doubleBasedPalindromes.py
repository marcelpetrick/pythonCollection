# Double-base palindromes
#
# Problem 36
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# ------------------------------------------------------------------------------

# idea:
# * loop over all numbers up to a certain limit (maybe parallelized - this would be actually the big bang for that task!)
# * create a function which tests a single number for palindromic (int and binary)
# * if true, then add to the result list
# * sum that result-list

# hints:
# * to do th palindrome check, just revert the stringified version and check against the original
# * just odd numbers (dec) can be fitting, because even numbers converted to binary would have a 0 as last digit. and
# for the first digit no numbers with 0 are allowed in the task (same applies for numbers divisible by ten in decimal, but
# mod 10 == 0 is already included in mod 2 == 0)

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def palindromeCheck(number):
    #print("palindromeCheck:", number)

    # no checks for odd-ness included, because the inputs are already filtered
    # saves a check here, saves time for one function-call, or?

    # reverting a string in python: ten thousands of ways
    # https://www.journaldev.com/23647/python-reverse-string#python-reverse-string-using-slicing

    # check first if number itself is palindrome
    stringifiedDec = str(number)
    if stringifiedDec != stringifiedDec[::-1]:
        return False

    # do then the same check for the binary version
    stringifiedBin = format(number, 'b') # str(bin(number)) will return with leading "0b", which is crap
    if stringifiedBin != stringifiedBin[::-1]:
        return False

    return True

# ------------------------------------------------------------------------------

# todo add unittest

# ------------------------------------------------------------------------------
# simple driver

# print(5, palindromeCheck(5))
# print(17, palindromeCheck(17))
# print(585, palindromeCheck(585))

def driver(number):
    isPalindromic = palindromeCheck(number)
    if isPalindromic:
        #print(number, "->", bin(number))
        pass

import time
startTime = time.time()

limit = 10 ** 6
for number in range(1, limit, 2): # step width 2 decreased runtime for 10 ** 6 (with output) from 0.44s to 0.22s
    driver(number)

print("Processing up to", limit, "took", time.time() - startTime, "s")
# no multi processing: Processing up to 10 ** 7 took 1.8554871082305908 s

# ------------------------------------------------------------------------------

# warning: also even number cans be palindromic
def prepareList(excludedLimit):
    return list(range(1, excludedLimit, 1))

print("list to process:", prepareList(100))

# call to process the whole list
startTime = time.time()
results = [elem for elem in prepareList(10 ** 6) if palindromeCheck(elem)]
print("Processing up to", limit, "took", time.time() - startTime, "s") # 10 ** 8: 30s
print("results:", results)

# ------ multithreaded? -----------
# from threading import Thread
#
# def process(data):
#     print(f"processing {data}")
#
# l= ["data1", "data2", "data3"]
#
# for task in range(1, 10**6):
#     t = Thread(target=palindromeCheck, args=(task,))
#     t.start()
# ---- end: not really working, just one thread .. ------------

# -------------- concurrent.futures -----
# import concurrent.futures
#
# # followed this tutorial: https://docs.python.org/3/library/concurrent.futures.html
# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     futureCollection = {executor.submit(palindromeCheck, number): number for number in list[range(1, 10 ** 6)]}
#
#     for future in concurrent.futures.as_completed(futureCollection):
#         number = futureCollection[future]
#         try:
#             result = future.result()
#         except Exception as ecx:
#             print("whatever .. %s" % ecx)
#         else:
#             print(number, "->", result)

# --------------- also did not really work: 'type' object is not subscriptable ... ?!? ----

# another attempt ... start simple, start basic
# take from https://pymotw.com/3/concurrent.futures/

from concurrent import futures
#import threading

ex = futures.ThreadPoolExecutor(max_workers=16)
print("auf los geht's los")
startTime = time.time()
inputList = range(1, 10 ** 6)
results = ex.map(palindromeCheck, inputList)
print("unformatted results:", results)
realResults = list(results)
print("better? {}".format(realResults))

from itertools import compress
filteredList = list(compress(inputList, realResults))
print("filtered results:", filteredList)
print("Processing took", time.time() - startTime, "s") # 10 ** 6: 23s ... not really faster!
# also not really using all cores ... something is wrong
