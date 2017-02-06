def foo(*args, **kwargs):
    print 'args=', args
    print 'kwargs=', kwargs
    print '**********************'

if __name__=='__main__':
    foo(1, 2, 3)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, a=1, b=2, c=3)
    foo(1, 'b', 'c', a=1, b='b', c='c',d={'name':'wangdejun','age':28})


def printArgs(x,*args,**kwargs):
    print x
    for j in args:
        print args[j]
    for i in kwargs:
        print kwargs[i]

printArgs(1,2,3)
printArgs(1,2,{"z":3})
printArgs(1,2,3,4,5,6,z=1,w=1234,wang="name",name="wangpeng")