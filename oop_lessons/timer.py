import time


class timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, exc_type, value, traceback):
        elapsed_time = (time.time() - self.start) * 1000
        print(self.message.format(elapsed_time))


"""
with timer('It takes me {}'):
    a = list(range(10 ** 7))
    print('OK')
"""

"""
def foo():
    for i in range(10):
        yield i

for x in foo():
    print(x)
"""
