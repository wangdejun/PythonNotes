def printArgs(x,*args,**kwargs):
    print x
    print args
    print kwargs


printArgs(1,2,3)
printArgs(1,2,{"z":3})
printArgs(1,2,3,4,5,6,z=1,w=1234,wang="name")