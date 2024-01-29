import time


class FRange:

    def __init__(self, top_limit, bottom_limit=None, step=1):
        if bottom_limit is not None:
            self.bottom_limit, self.top_limit = top_limit, bottom_limit
        else:
            self.bottom_limit, self.top_limit = 0, top_limit

        self.step = step
        self._increment = 0
        self._value = self.bottom_limit

    def __next__(self):
        if self.step > 0:
            self._value += self._increment
            if self._value >= self.top_limit:
                raise StopIteration()
            self._increment = self.step
            return self._value
        else:
            self._value += self._increment
            if self._value <= self.top_limit:
                raise StopIteration()
            self._increment = self.step
            return self._value

    def __iter__(self):
        return self


for i in FRange(10, 2, -2):
  time.sleep(1)
  print(i)

assert(list(FRange(5)) == [0, 1, 2, 3, 4])
assert(list(FRange(10, 2, -2)) == [10, 8, 6, 4])
