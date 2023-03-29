class Singleton(type):
    def __init__(self, *args, **kwds):
        self.__instance = None
        super().__init__(*args, **kwds)

    def __call__(self, *args, **kwds):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwds)
            return self.__instance
        else:
            return self.__instance


class A(metaclass=Singleton):
    def __init__(self):
        print("Class A")


class B(metaclass=Singleton):
    def __init__(self):
        print("Class A")


a_1 = A()
a_2 = A()
b_1 = B()
b_2 = B()

print("a_1 is a_2", a_1 is a_2)
print("b_1 is b_2", b_1 is b_2)

