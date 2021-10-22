# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.bar= 'abar'


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.foo='bfoo'


#Order of classes matter if both classes have similiar variables
class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)


c = C()
c.showprops()
print(C.__mro__)
