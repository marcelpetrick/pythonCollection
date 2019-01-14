# class which shall store all kinds of types in a stack.
# Default operations like push, pop, currentSize are offered.
# Popping on an empty stack leads to no errors.

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

class Stack(object):
    # ctor
    def __init__(self):
        #print("Stack: ctor :)")
        self.__body__ = []

    # methods
    def currentSize(self):
        #print("currentSize:", len(self.__body__))
        return len(self.__body__)

    def push(self, element):
        #print("push")
        self.__body__.append(element)

    def pop(self):
        #print("pop")
        if self.currentSize() > 0:
            self.__body__.pop(self.currentSize() - 1)

    # representation: empty Stack -> ""; else "elem0;elem1;elem2;.."
    def __repr__(self):
        result = ""

        for elem in self.__body__:
            result += elem + ";"

        return result

# ------------------------------------------------------------------------------

# just run if the current module name is ours
if __name__ == "__main__":

    stack = Stack()
    print("size:", stack.currentSize())
    print("stack:", stack)
    stack.push("foo")
    stack.push("bar")
    stack.push("coo")
    print("stack:", stack)
    stack.pop()
    stack.pop()
    print("stack:", stack)

    print("size:", stack.currentSize())

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_newStack(self):
        stack = Stack()
        self.assertEqual(0, stack.currentSize())
        self.assertEqual("", stack.__repr__())

    def test_push(self):
        stack = Stack()
        stack.push("albert")
        stack.push("berta")
        stack.push("caesar")
        self.assertEqual(3, stack.currentSize())
        # also the check for the representation-method
        self.assertEqual("albert;berta;caesar;", stack.__repr__())

    def test_pop(self):
        stack = Stack()
        stack.push("albert")
        stack.push("berta")
        stack.push("caesar")
        self.assertEqual(3, stack.currentSize())
        self.assertEqual("albert;berta;caesar;", stack.__repr__())
        stack.pop()
        self.assertEqual(2, stack.currentSize())
        stack.pop()
        self.assertEqual(1, stack.currentSize())
        stack.pop()
        self.assertEqual(0, stack.currentSize())
        # check against pop on empty stack
        stack.pop()
        self.assertEqual(0, stack.currentSize())
