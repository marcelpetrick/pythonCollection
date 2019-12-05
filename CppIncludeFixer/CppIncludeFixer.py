# author mail@marcelpetrick.it
# license: GPLv3.0

# idea:
#
# 0. check the given file (either h/cpp) for double includes (of course, maybe some normalized format has to be used)
# because "item.h" and "../item.h" cannot be (without evaluation the project structure/build-system (cmake in this case)
# distinguished
#
# 1. normalize the Qt includes to the fully qualified form (e.g. <QtCore/QDebug> instead of <QDebug>).
# Maybe some input-lookup table has to be created
#

# TODO implement
# TODO unit-test (maybe with generated data)
