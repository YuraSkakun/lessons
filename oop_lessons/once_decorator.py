from functools import wraps

def once(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@once
def get_logger():
    return [1, 2, 3] * 2


print('#' * 80)
print(get_logger, type(get_logger), id(get_logger))
print('#' * 80)
print(get_logger())
print(get_logger())
print(id(get_logger()), id(get_logger()))
assert id(get_logger()) == id(get_logger()), "Not equal"
print("SUCCESS!")
print('#' * 80)

def get_logger_1():
    return [1, 2, 3] * 2
a1 = get_logger_1()
a2 = get_logger_1()

print(get_logger_1, id(get_logger_1))
print(id(a1), id(a2))
print(a1 == a2)
assert id(a1) != id(a2), "equal"
print("SUCCESS!")
print(a1)
