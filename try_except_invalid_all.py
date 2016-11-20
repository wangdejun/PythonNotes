while True:
    try:
        x = input("the first number is:")
        y = input("the second number is :")
        value = x/y
        print "x/y is",value
    except:
        print "Invalid input,Please try again."
    else:
        break
