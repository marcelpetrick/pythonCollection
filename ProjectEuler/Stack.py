class Stack(object):
    # ctor
    def __init__(self):
        print("Stack: ctor :)")
        self.__body__ = []

    # methods
    def currentSize(self):
        print("currentSize:", len(self.__body__))
        return len(self.__body__)

    def push(self, element):
        print("push")
        self.__body__.append(element)

    def pop(self):
        print("pop")
        self.__body__.pop(self.currentSize() - 1)

    # representation
    def __repr__(self):
        result = ""
        for elem in self.__body__:
            result += elem + ";"

        return result

#---------------------------------------------------------------------------

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