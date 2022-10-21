import functools
import time


def profile(f):
    def deco(*args):
        start = time.time()
        deco._num_call += 1
        result = f(*args)
        deco._num_call -= 1
        if deco._num_call == 0:
            print(f'Elapsed {time.time() - start}ms')
        return result

    deco._num_call = 0

    return deco


def cache(f):
    def deco(*args):
        if args not in deco._cache:
            result = f(*args)
            deco._cache[args] = result
        return deco._cache[args]

    deco._cache = {}

    return deco


# @profile
# @cache
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) +fibo(n-2# )


# fibo = cache(profile(fibo)) # !!!!!!!!!!!!!!!!!

@cache
@profile
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


# 1 1 2 3 5 8 13
print(fibo(35))
print(fibo._cache)
print(len(fibo._cache))

##################################################################################
# """ if we want to OGRANICHIT :
# @cache(max_limit=10),   togda :
#

def profile(f):
    @functools.wraps(f)  # help, .....    for f PROBRASYVAET VNUTR
    def deco(*args):
        start = time.time()
        deco._num_call += 1
        result = f(*args)
        deco._num_call -= 1
        if deco._num_call == 0:
            print(f'Elapsed {time.time() - start}ms')
        return result

    deco._num_call = 0

    return deco



def cache(max_limit=None):   # tut vyzyvaetsya function cache() <---- skobki
    def inner(f):            # TUT VNUTRI VYZYVAETSYA SAMA f --> u nas eto fibo
        @functools.wraps(f)  # help, .....    for f PROBRASYVAET VNUTR
        def deco(*args):
            if args not in deco._cache:
                result = f(*args)
                if max_limit is not None and len(deco._cache) > max_limit:
                    first_key = next(iter(deco._cache))
                    deco._cache.pop(first_key)
                deco._cache[args] = result
            return deco._cache[args]

        deco._cache = {}
        return deco
    return inner


#@functools.lru_cache  # est vstroennyy decorator lru_cache --> vnutri nego est max_limit !!! vmesto @cache(max..)
@cache(max_limit=10)  # tut decorator(@) ne object cache , a rezultat funkcii cache(...) !!!
@profile
def fibo(n):
    """ inefficient fibo function """
    if n < 2:
        return n
    else:
        return fibo(n-1) +fibo(n-2)


# 1 1 2 3 5 8 13
print(fibo(35))
print(fibo._cache)
print(len(fibo._cache))

help(fibo)
