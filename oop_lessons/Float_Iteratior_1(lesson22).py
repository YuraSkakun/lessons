class RangeFloatIterator:
    counter = 0

    def _step_check(self, condition):
        if self.counter < self.end if condition else self.counter > self.end:
            self.counter += self.step
            return self.counter - self.step
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __init__(self, start, end=None, step=1.0):
        self.step = step
        self.start = start
        self.end = end
        if self.end is not None:
            self.start, self.end = start, end
        else:
            self.start, self.end = 0.0, start

        self.counter = self.start

    def __next__(self):
        if self.step > 0:
            return self._step_check(True)
        else:
            return self._step_check(False)


frange = RangeFloatIterator(10, 2, -2)

for i in frange:
    print(i)

assert (list(RangeFloatIterator(5)) == [0.0, 1.0, 2.0, 3.0, 4.0])
assert (list(RangeFloatIterator(5)) == [0, 1, 2, 3, 4])
assert (list(RangeFloatIterator(2, 5.5, 1.5)) == [2.0, 3.5, 5.0])
assert (list(RangeFloatIterator(0, 2, 1)) == [0.0, 1.0])
assert (list(RangeFloatIterator(1, 6)) == [1.0, 2.0, 3.0, 4.0, 5.0])
assert (list(RangeFloatIterator(0, 0)) == [])
assert (list(RangeFloatIterator(100, 0)) == [])
assert (list(RangeFloatIterator(10, 2, -2)) == [10, 8, 6, 4])
assert (list(RangeFloatIterator(2, 5.5, 1.5)) == [2, 3.5, 5])
