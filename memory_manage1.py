a = 1
b = 1
c = 1
print(id(a))
print(id(b))
print(id(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print(a is b)
print(b is c)

w = "wangdejun is a good programmer"
m = "wangdejun is a good programmer"

print(a is b)

#getrefcount()
from sys import getrefcount
# a=0
# print("1,after the defination:",getrefcount(a))
a = [1,2,3]
print("2,after the =: ",getrefcount(a))
b = a
print("3,after another = ",getrefcount(b))

class from_obj(object):
    def __init__(self,to_obj):
        self.to_obj = to_obj

b = [1,2,3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))

a = [1,2,3]
print(getrefcount(a))
b = [a,a]
print("b=",b)
print(getrefcount(a))


#getrefcount()
from sys import getrefcount


# a=0
print("1,after the defination:",getrefcount(a))
a = [1,2,3]
print("2,after the =: ",getrefcount(a))
b = a
print("3,after another = ",getrefcount(b))

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

import objgraph
objgraph.show_refs([z], filename='ref_topo.png')