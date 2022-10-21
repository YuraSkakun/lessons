def frange(start, stop=None, step=None):

    """ float range function """

    start = float(start)
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if step is None:
        step = 1.0

    print("start= ", start, "stop= ", stop, "step= ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1


for i in frange(5):
    print(i)  # output 1.0, 2.0, 3.0, 4.0

for i in frange(1, 10, 3.5):
    print(i)  # output 1.0, 4.5, 8.0

for i in frange(10, 1, -3.5):
    print(i)  # output 10.0, 6.5, 3.0

for i in frange(1, 3.5):
    print(i)  # output 1.0, 2.0, 3.0, default step == 1

for i in frange(-1, -5, -1.2):
    print(i)  # output -1.0, -2.2, -3.4, -4.6
