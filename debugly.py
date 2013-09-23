from functools import wraps

def debug(func):
    #func as input
    @wraps(func) #to copy meta data
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper
