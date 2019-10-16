def log(f):
    def wrapper(*args, **kwargs):
        print (f.__name__, args, kwargs)
        res = f(*args, **kwargs)
        print (f.__name__, res)
        return res
    return wrapper
@log 
def add(x,y):
    return x + y
print (add (2, 3))