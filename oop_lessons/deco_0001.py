def cache(f):
    def deco(*args):
        if args not in deco._cache:
            result = f(*args)
            deco._cache[args] = result
        return deco._cache[args]

    deco._cache = {}
    print(deco._cache)
    return deco


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


fibo = cache(fibo)
print('***')
print(fibo)           # <function cache.<locals>.deco at 0x7f3930dfcdc0>
print(fibo._cache)    # {}

# 0 1 1 2 3 5 8 13
print(fibo(3))        # 2
print(fibo(35))       # 9227465
