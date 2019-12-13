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
# 2. compare all "class" forward declarations if they are really used a second time within the same header-file.
# Common issue is that they are not used for a type-ptr.

# TODO implement
# TODO unit-test (maybe with generated data)

# ------------------------------------------------------------------------------
import unittest
class Testcase(unittest.TestCase):
    def test_calcValueOfName(self):
        # self.assertEqual(1, calcValueOfName("A"))
        # self.assertEqual(53, calcValueOfName("COLIN"))
        pass

    def test_finalRun(self):
        # print("final score is:", calcNameScore())
        # self.assertTrue(1337)
        pass

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
# ------------------------------------------------------------------------------
