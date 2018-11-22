# This problem was asked by Microsoft.
#
# Implement a URL shortener with the following methods:
#
# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string into the original url. If no such
# shortened string exists, return null.
#
# Hint: What if we enter the same URL twice?

# ------------------------------------------------------------------------------
#my ideas:
# + create class with two members
# + hash the input and put into dictionary
# + to avoid the problem with "double input -> what now?" use the current time as suffix as salt; but what kind
# of separator which is not in the valid urls?

# 20180804:
# read about https://blog.codinghorror.com/url-shortening-hashes-in-practice/ to get some practical insight
# https://www.pythoncentral.io/hashing-strings-with-python/

# Afterwards I tend to use the "just count upwards some six-digit word made out of regular of expanded alphabet"-approach.

import string
allchar = string.ascii_letters +\
    string.digits
          #string.punctuation +\

print(allchar.__len__()) # 62
print(allchar)

# six digits with 52 possibilities: 19*10^4 - but is 'a' different from 'A' for urls?