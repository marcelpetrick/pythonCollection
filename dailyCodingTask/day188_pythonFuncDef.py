# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# What will this code print out?

# def make_functions():
#     flist = []
#
#     for i in [1, 2, 3]:
#         def print_i():
#             print(i)
#         flist.append(print_i)
#
#     return flist
#
# functions = make_functions()
# for f in functions:
#     f()

#---------------------------------------------

def make_function(inputValue):
    def newFunc():
        print(inputValue)
        return

    return newFunc

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        newFunction = make_function(i)
        #newFunction() # just for testing

        flist.append(newFunction) # inserts correctly, without braces, or?

    return flist


print("########################################################")
functions = make_functions()
print("########################################################")
for f in functions:
    f()

# prints:
#$day188_pythonFuncDef.py
#3
#3
#3
#
#Process finished with exit code 0

#---------------------------------- new version :) --------------------------
# The difference is now that a specific function is creating the new function.
# And then returns it. Then it is stored (as first class function) inside the list.
# And that works! :)
#
# 1
# 2
# 3
#
# Process finished with exit code 0