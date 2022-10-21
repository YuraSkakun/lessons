class A:

    def __init__(self):
        super().__init__()

    def foo(self):
        print('Hello from A.foo()')


class A1(A):
    def __init__(self):
        super().__init__()
        self.attrA1 = 'attrA1'

    def foo_a1(self):
        print('foo_a1() called')


class A2(A):
    def __init__(self):
        super().__init__()
        self.attrA2 = 'attrA2'

    def foo_a2(self):
        print('foo_a2() called')


a1 = A1()
a2 = A2()
print(a1.attrA1)
print(a2.attrA2)
a1.foo()
a2.foo()

a1.foo_a1()
a2.foo_a2()

class B(A1, A2):
    def __init__(self):
        super().__init__()
        self.attr1 = 'attrB'
        self.attr2 = 'attr2B'

b = B()
print(b.__dict__)
