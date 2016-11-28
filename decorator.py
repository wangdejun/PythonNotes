def log(f):
    def wrapper(*args,**kw):
        print "call %s():" % f.__name__
        print "i am going to print the name of the value! %s():" % f.__name__
        return f(*args,**kw)
    return wrapper

@log
def now():
    print "2016-12-1"


now()
