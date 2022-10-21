class FloatRange:

    _temp = 0

    def __init__(self, start=None, stop=None, step=1.0):
        if start is None:
            raise TypeError('float_range expected 1 arguments, got 0')
        if step == 0:
            raise ValueError('float_range() arg 3 must not be zero')
        else:
            self._start =(start + 0.0) if stop is not None else 0.0
            self._stop = (stop + 0.0) if stop is not None else (start + 0.0)
            self._step = step
            self._temp = self._start
            # print (f'start: {self._start} --- stop: {self._stop} --- step: {self._step}')

    def __iter__(self):
        return self

    def __next__(self):
        if (
                self._step > 0 and self._temp < self._stop
        ) or (
                self._step < 0 and self._temp > self._stop
        ):
            self._temp += self._step
            return self._temp - self._step
        else:
            raise StopIteration

fr = FloatRange(0, 10, 0.1)
print(list(fr))
print(list(FloatRange(0, 10, 0.2)))

fr1 = FloatRange(10)

fr2 = FloatRange(0, 10)

fr3 = FloatRange(1, 10, 2.5)

fr4 = FloatRange(100, 10, -2.5)

print ('___________________________________')

FloatRange(0, 0)
print(list(FloatRange(0, 0)))

print ('___________________________________')

FloatRange(100, 0)
print(list(FloatRange(100, 0)))

print ('___________________________________')


frange = FloatRange(10, -4, -2.2)

for i in frange:
    print(i)

print ('___________________________________')

frange1 = FloatRange(10, 100, -2.2)

for i in frange1:
    print(i)

print ('___________________________________')

frange2 = FloatRange(10, 20, 2.2)

for i in frange2:
    print(i)

assert (list(FloatRange(5)) == [0.0, 1.0, 2.0, 3.0, 4.0])
assert (list(FloatRange(5)) == [0, 1, 2, 3, 4])
assert (list(FloatRange(2, 5.5, 1.5)) == [2.0, 3.5, 5.0])
assert (list(FloatRange(0, 2, 1)) == [0.0, 1.0])
assert (list(FloatRange(1, 6)) == [1.0, 2.0, 3.0, 4.0, 5.0])
assert (list(FloatRange(0, 0)) == [])
assert (list(FloatRange(100, 0)) == [])
assert (list(FloatRange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(FloatRange(2, 5.5, 1.5)) == [2, 3.5, 5])
