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

# def foo_1():
#     for i in range(10):
#         yield i
#
# print(foo_1())  # <generator object foo_1 at 0x7f6604e1e5f0>
#
# for x in foo_1():
#     print(x)


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


# path_from = '/home/yshost/Downloads/001.txt'
# path_to = '/home/yshost/Downloads/dest_01.txt'
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
# print(g)
#
# f = open(path_to, 'w')
# for chunk in read_file(path_from):
#     f.write(chunk)
# f.close()


import time


def cache(f):

    def inner(*args, **kwargs):
        x = args
        print(type(x))
        y = kwargs
        y1 = kwargs.items()
        print(y, type(y))
        print(y1, type(y1))
        key = (args, frozenset(kwargs.items()))
        print(key, type(key), len(key))
        print(key[1], type(key[1]))
        print(key[0], type(key[0]))
        if key not in inner.cache:
            inner.cache[key] = f(*args, **kwargs)
            print('!!!', inner.cache)
        return inner.cache[key]

    inner.cache = {}
    print(inner.cache)
    print('------')
    return inner


# @cache
# def foo_5(*args, **kwargs):
#     time.sleep(2)
#     return 44
#
#
# print(foo_5('ooo', a=1, b=2))


@cache
def fib_cache(n):
    result = 1 if n <= 2 else fib_cache(n-1) + fib_cache(n-2)
    return result


print(fib_cache(4))



import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(__file__, type(__file__))
print(os.path.abspath(__file__), type(os.path.abspath(__file__)))
print(ROOT_DIR)

print(__name__)



import csv

from flask import Flask

app = Flask(__name__)


@app.route('/get-data-from-csv')
def get_requirements():
    # with open('requirements.txt', 'r') as f:
    #     result = f.read()
    # print(result, type(result))
    # result = result.replace('\n', '<br>')
    # print(result)
    # return result
    with open('students.csv', 'r') as f:
        reader = csv.DictReader(f)
        print(reader, type(reader))  # <csv.DictReader object at 0x7f301b46fa30> <class 'csv.DictReader'>
        rows = [row for row in reader]
    # str_rows = '<br>'.join([
    #     str(record)
    #     for record in rows
    # ])
    # return str_rows
    print(rows[0], rows[1])  # [{'certifi==2022.9.24': 'charset-normalizer==2.1.1'}, {'certifi==2022.9.24': 'click==8.1.3'},...
    print(type(rows[0]))  # <class 'list'>

    average = 0
    Sum = 0
    column = len(rows)
    print(column)
    for row in rows:
        Sum += float(row['height'])
        print(Sum)
    average = Sum / column
    print(average)
    return str(rows[1])


app.run(host="localhost", port=5000, debug=True)
