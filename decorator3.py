import time

class Timeit(object):
    def __init__(self,func):
        self.func = func
    
    def __call__(self,*args,**kws):
        print('invoking Timer')
    
    def __get__(self,instance,owner):
        return lambda *args, **kwargs:self.func(instance)

@Timeit
def func():
    time.sleep(1)
    return "invoking function func"