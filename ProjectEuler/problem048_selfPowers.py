# Self powers
#
# Problem 48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

#------------
result = sum([i ** i for i in range(1, 1000 + 1)])
print("result:", result)
print("last ten digits:", str(result)[-10::])
