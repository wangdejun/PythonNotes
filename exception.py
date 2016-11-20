try:
    x=input("first number:")
    y=input("second number:")
    print x/y
except ZeroDivisionError:
    print "the second number can't be zerow"
