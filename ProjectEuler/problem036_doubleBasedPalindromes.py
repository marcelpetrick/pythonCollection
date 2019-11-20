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
#
# def driver(number):
#     isPalindromic = palindromeCheck(number)
#     if isPalindromic:
#         #print(number, "->", bin(number))
#         pass
#
# import time
# startTime = time.time()
#
# limit = 10 ** 6
# for number in range(1, limit, 2): # step width 2 decreased runtime for 10 ** 6 (with output) from 0.44s to 0.22s
#     driver(number)
#
# print("Processing up to", limit, "took", time.time() - startTime, "s")
# # no multi processing: Processing up to 10 ** 7 took 1.8554871082305908 s

# ------------------------------------------------------------------------------

# # warning: also even number cans be palindromic
# def prepareList(excludedLimit):
#     return list(range(1, excludedLimit, 1))
#
# print("list to process:", prepareList(100))
#
# # call to process the whole list
# startTime = time.time()
# results = [elem for elem in prepareList(10 ** 6) if palindromeCheck(elem)]
# print("Processing up to", limit, "took", time.time() - startTime, "s") # 10 ** 8: 30s
# print("results:", results)

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

# from concurrent import futures
# #import threading
#
# print("### ThreadPoolExecutor: BEGIN ###")
# ex = futures.ThreadPoolExecutor(max_workers=16)
# startTime = time.time()
# inputList = range(1, 10 ** 4)
# results = ex.map(palindromeCheck, inputList)
# print("unformatted results:", results)
# realResults = list(results)
# print("better? {}".format(realResults))
#
# from itertools import compress
# filteredList = list(compress(inputList, realResults))
# print("filtered results:", filteredList)
# print("Processing took", time.time() - startTime, "s") # 10 ** 6: 23s ... not really faster!
# # also not really using all cores ... something is wrong
# print("### ThreadPoolExecutor: END ###")
# ---------------- multi processing now! -----------------

if __name__ == '__main__': # see guidelines for multiprocessing: https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming
    import multiprocessing
    import time
    from itertools import compress

    print("### multiprocessing: BEGIN ###")

    limit = 10 ** 6
    print("handle now numbers up to", limit)

    # input preparation
    startTime = time.time()
    inputList = range(limit)
    print("Creating the input-list took", time.time() - startTime, "s")

    # multiprocessing via map onto the input
    startTime = time.time()
    with multiprocessing.Pool(32) as pool: # 64 or 32 does not matter ... compress takes the longest, or?
        results = pool.map(palindromeCheck, inputList) # should result in a  list as well

    print("Processing took", time.time() - startTime, "s")

    # compressing (almost instantaneous)
    startTime = time.time()
    filteredList = list(compress(inputList, results))
    print("Compressing took", time.time() - startTime, "s")

    print("filteredList:", filteredList)
    print("sum of the values:", sum(filteredList))
    print("### multiprocessing: END ###")

# ------------------------------------------

# results for a run with up to 10**9:
#
# ### multiprocessing: BEGIN ###
# handle now numbers up to 1000000000
# Creating the input-list took 0.0 s
# Processing took 205.50690913200378 s
# Compressing took 14.142150402069092 s
# filteredList: [0, 1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585, 1758571, 1934391, 1979791, 3129213, 5071705, 5259525, 5841485, 13500531, 719848917, 910373019, 939474939]
# ### multiprocessing: END ###

# ------------------------------------------
# limit 10 ** 6 just like the task demanded

# ### multiprocessing: BEGIN ###
# handle now numbers up to 1000000
# Creating the input-list took 0.0 s
# Processing took 0.4377901554107666 s
# Compressing took 0.02025580406188965 s
# filteredList: [0, 1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585]
# sum of the values: 872187
# ### multiprocessing: END ###

# ------------------------------------------

# Congratulations, the answer you gave to problem 36 is correct.
#
# You are the 82518th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%.

