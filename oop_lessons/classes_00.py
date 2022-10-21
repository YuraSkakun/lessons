class A:  # class A(object):
    """
    This is A
    """

    def __init__(self, name):
        self.name = name

    def foo(self):
        """
        foo
        """
        print('foo', self.name, self)


a = A('test')
b = A('test2')
# a.foo()
A.foo(a)
A.foo(b)

print(a)
print(b)
print(dir(a))
print(dir(A))
print(dir(object))


print(a.__class__)
print(A.__class__, A.__bases__)
print(A.__doc__)
print(A.foo.__doc__)
help(A.foo)
