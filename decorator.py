#decorator args参数装饰器


def log(f):
    def wrapper(*args,**kw):
        # 包装函数
        # 打印传进来的函数name
        print "call %s():" % f.__name__
        print "i am going to print the name of the value! %s():" % f.__name__
        #返回传进来的函数，可以发现装饰器在返回函数之前做了很多『装饰性』工作
        return f(*args,**kw)
        # 返回包装函数
    return wrapper


@log#使用装饰器
def now():
    print "2016-12-1"

#执行函数
now()

#定义一个新的装饰器，
# 功能是在调用某函数之前打印函数名字，并且告知即将调用函数的名字

def logFunctionName(thename):
	def theNameWrapper(*args,**kw):
		print "call %s():" % thename.__name__
		print "I am going to print the name of the value! %s():" % thename.__name__
		return thename(*args, **kw)
	return theNameWrapper


@logFunctionName
def hello():
	print "Hello,World!"

hello()




