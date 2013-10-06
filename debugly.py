from functools import wraps, partial

def debug(func=None,*, prefix=''):
    #making the decorator callable within itself unlike providing another function
    if func is None:
        return partial(debug, prefix=prefix)
    msg = prefix + func.__qualname__
    #func as input
    @wraps(func) #to copy meta data
    def wrapper(*args, **kwargs):
        print(msg)#for classes names qualname is user
        return func(*args, **kwargs)
    return wrapper

#use of args for a decorator through creation under a environment function debugarg where the variables get stored and can be accessible to the 
def debugarg(prefix = ''):
    def debug(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(func.__qualname__)#for classes names qualname is user
            return func(*args, **kwargs)
        return wrapper


def debugmethods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls,key, debug(val))
    return cls

