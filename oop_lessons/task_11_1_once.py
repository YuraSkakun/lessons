from functools import wraps


def once(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            wrapper.result = f(*args, **kwargs)
            return wrapper.result
        else:
            return wrapper.result
    wrapper.result = None
    wrapper.has_run = False
    print(f'id of function {id(wrapper())} name = {wrapper.__name__}')
    return wrapper


@once
def get_logger():
    return [1, 2, 3] * 2
'''
### this== ###    get_logger = once(get_logger)
print(get_logger.result, get_logger.has_run)
print('*' * 80)
'''

assert id(get_logger()) == id(get_logger()), "Not equal"
print('SUCCESS')

print(f'get_logger: {id(get_logger())}  {id(get_logger())}')
print(f'get_logger: {id(get_logger())}  {id(get_logger())}')
get_logger.has_run = False
print(f'get_logger: {id(get_logger())}  {id(get_logger())}')


assert id(get_logger()) == id(get_logger()), "Not equal"
print('SUCCESS')

result = get_logger()

result.append(42)

print(result)

help(get_logger)
