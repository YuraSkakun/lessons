import re
import time
import json
# import yaml
import random
import itertools
# import dicttoxml, xmltodict

from pprint import pprint as pp
from functools import wraps, partial




class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start) * 1000
        print(self.message.format(elapsed_time))




"""
class A():
    def __enter__(self):
        print('__enter__')

    def __exit__(self, type, value, traceback):
        print('__exit__')

# with A():
#     raise ValueError('WRONG!')
"""




# Magic attributes/methods¶
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
# print(dir(a))
# print(dir(A))
# print(dir(object))


print(a.__class__)
print(A.__class__, A.__bases__)
print(A.__doc__)
print(A.foo.__doc__)
help(A.foo)

print(a.__str__())
print(str(a))

dir(a)
a.__dir__()

# xxx(a)
# a.__xxx__()

v = 42
print(v + 1)
print(v.__add__(1))


class Employee:
    def __init__(self, first_name=None, last_name=None, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def __bool__(self):
        return bool(self._first_name or \
                    self._last_name or \
                    self._email)


e = Employee()

if e:
    print('Not empty')
    # do some work

if e is not None:  # None ~= null
    print('Is not None')
    # do some work



# operator overloading
class Q:
    def __init__(self, **params):
        self._params = params

    def __or__(self, other):
        self._params.update(other._params)
        return self

    #     def __and__(self, other):
    #         self._params.update(other._params)
    #         return self

    def __str__(self):
        result = ''
        for k, v in self._params.items():
            if result:
                result += ' OR '
            #             if result:
            #                 result += ' OR '
            result += f'{k}={repr(v)}'
        return result


filter = Q()
filter |= Q(first_name='John')
filter |= Q(last_name='Gonzalez')
filter |= Q(stuff=True)
filter |= Q(age=42)

print(filter)



#__dict__
class A:
    attr1 = 'attr1'  # static

    def __init__(self, obj_attr1, obj_attr2):
        self.obj_attr1 = obj_attr1
        self.obj_attr2 = obj_attr2


a = A(1, 'abc')
a2 = A(2, 'xyz')

print(a.obj_attr1, id(a.obj_attr1))
print(a2.obj_attr1, id(a2.obj_attr1))
print(a.attr1, id(a.attr1))
print(a2.attr1, id(a2.attr1))


pp('Obj attrs: ')
pp(a.__dict__)
print()
pp('Class attrs: ')
pp(A.__dict__)


print(a.obj_attr1)
print(a.__dict__['obj_attr1'])
a.__dict__['obj_attr1'] = 42
print(a.obj_attr1)
A.attr1 = 'XYZ'
print(A.__dict__['attr1'])
print(a.attr1)


b = A(1, 'abc')
print(id(a.attr1), id(b.attr1))
print(id(a.obj_attr1), id(b.obj_attr1))
print(id(a.obj_attr2), id(b.obj_attr2))


a = A(1024, 'abc')
b = A(1024, 'abc'.upper().lower())
# c = A(1024, 'ab'+'c')
print(id(a.attr1), id(b.attr1))
print(id(a.obj_attr1), id(b.obj_attr1))
print(id(a.obj_attr2), id(b.obj_attr2))


b.attr1 = 42
print(id(a.attr1), id(b.attr1))


pp('Obj attrs: ')
pp(b.__dict__)
print()
pp('Class attrs: ')
pp(A.__dict__)

# Monkey patchihttp://localhost:8889/notebooks/lesson_classes.ipynb#ng
a.xxxx = 42
pp('Obj attrs: ')
pp(a.__dict__)
print(a.xxxx)


def super_lib():
    def super_func():
        print('foo')

    super_func = super_func


def profile(f):
    from time import time
    def deco(*args):
        start = time()
        f(*args)
        print('Elapsed: ', time() - start)

    return deco


print(id(super_lib.super_func))
super_lib.super_func = profile(super_lib.super_func)
print(id(super_lib.super_func))




