# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        print("line 11: i=", i)
        funcString = "print" + str(i)
        print("funcString:", funcString)
        def funcString():
            print(i)

        # works with the current value of i
        funcString()
        #print_i.__name__ = "print_i" + str(i)
        flist.append(funcString) # inserts correctly, without braces, or?

    print("########################################################")
    # test if here at least it works: does not!
    # I think the problem is that the function definition itself is overwritten each time
    # update: no, but the used "i" is always at 3 ..
    for f in flist:
        f()

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