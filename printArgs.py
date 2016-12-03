def printArgs(x,*args,**kwargs):
    print x
    for j in args:
        print args[j]
    for i in kwargs:
        print kwargs[i]

printArgs(1,2,3)
printArgs(1,2,{"z":3})
printArgs(1,2,3,4,5,6,z=1,w=1234,wang="name",name="wangpeng")
