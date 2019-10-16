def f():
    y = a
    def g(x):
        return y*x 
    return get

def get_area(x):
    return x*x
def scale(f):
    def wrapper(x):
        x = x*100
        res = f(x)
        return res
    return wrapper
get_area = scale (get_area)
print (get_area(5))
#ss
@scale
def get_area(x):
    return x*x
get_area (5)