# def foo_1():
#     for i in range(10**10):
#         yield i
#
#
# print(foo_1())
#
# for x in foo_1():
#     print(x)



# path_from = '/home/yshost/Downloads/001.txt'
# path_to = '/home/yshost/Downloads/dest.txt'
#
# def read_file(filepath):
#     with open(filepath, 'r') as f:
#         chunk_size = 4
#         chunk = f.read(chunk_size)
#
#         while chunk:
#             yield chunk
#             chunk = f.read(chunk_size)
#
#
# g = read_file(path_from)
#
# f = open(path_to, 'w')
# for chunk in read_file(path_from):
#     f.write(chunk)
# f.close()



import time


# def foo_3():
#     start = time.time()
#
#     time.sleep(2)
#
#     elapsed = time.time() - start
#     print(f'Elapsed: {elapsed}')
#     return 42
#
# print(foo_3())



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
