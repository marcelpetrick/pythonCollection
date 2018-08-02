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
