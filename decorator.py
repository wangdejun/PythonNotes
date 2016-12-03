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

def logFunctionName(thename):
	def theNameWrapper(*args,**kw):
		print "call %s():" %thename.__name__
		print "I am going to print the name of the value! %s():" % thename.__name__
		return thename(*args,**kw)
	return theNameWrapper

@logFunctionName
def hello():
	print "Hello,World!"

hello()




