# generators
# decorators



# def bar():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 2
#     print('step 3')
#     yield 3
#
# gen = bar()
# for x in gen:
#     print(x)



# def foo():
#     for i in range(10**10):
#         return i
#
# print(foo())



# def foo_1():
#     for i in range(10**10):
#         yield i
#
# print(foo_1())
#
# for x in foo_1():
#     print(x)



# new_gen = (i for i in range(10**10))
#
# for i in new_gen:
#     print(i)



# def foo_2():
#     for i in range(10**10):
#         yield i
#
# for i in foo_2():
#     print(i)



# path_from = '/home/dbhost/Downloads/1GB.bin'
# path_to = '/home/dbhost/Downloads/dest.bin'
#
# def read_file(filepath):
#     with open(filepath, 'r+b') as f:
#         chunk_size = 4096
#         chunk = f.read(chunk_size)
#
#         while chunk:
#             yield chunk
#             chunk = f.read(chunk_size)
#
# f = open(path_to, 'w+b')
# for chunk in read_file(path_from):
#     f.write(chunk)
# f.close()



# """ description yield: """
#
# def callback(*args, **kwargs):
#     print(locals())
#
# def hand_made_gen(start, stop, cb, *cb_args, **cb_kwargs):
#     while start < stop:
#         cb(start, *cb_args, **cb_kwargs)
#         start += 1
#
# hand_made_gen(0, 10**10, callback)



import time


def foo_3():
    start = time.time()

    time.sleep(2)

    elapsed = time.time() - start
    print(f'Elapsed: {elapsed}')
    return 42

print(foo_3())



def fib(n):
    start = time.time()
    result = 1 if n <= 2 else fib(n-1) + fib(n-2)
    elapsed = time.time() - start
    print(f'Elapsed: {elapsed}')
    return result

print(fib(10))



def profile(f):
    def inner(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        elapsed = time.time() - start
        print(f'Elapsed: {elapsed}s')
        return ret

    return inner


def foo_4():
    time.sleep(2)
    return 43

foo_4_decorated = profile(foo_4)

print(foo_4_decorated())



@profile
def foo_5():
    time.sleep(2)
    return 44

print(foo_5())



def cache(f):

    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in inner.cache:
            inner.cache[key] = f(*args, **kwargs)
        return inner.cache[key]

    inner.cache = {}

    return inner


@profile
@cache
def fib_cache(n):
    result = 1 if n <= 2 else fib_cache(n-1) + fib_cache(n-2)
    return result


print(fib_cache(40))
