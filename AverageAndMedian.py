list = []

#---------------

def average(list):
    if len(list) == 0:
        return -666

    return sum(list) / len(list)

#---------------

def median(list):
    sorted = list.sort()
    lengthHalf = len(list) // 2
    median = ((sorted[lengthHalf] + sorted[lengthHalf]) / 2) if len(list) % 2 == 0 else sorted[lengthHalf]
    return median

#---------------

print(median([3, 2, 1]))
#---------------

# 907
# 758
# 712
# 706
# 951
# 617
# 551
# 737
# 733
# 1013
# 1019
# 740
#
# average	787
# median	738.5
