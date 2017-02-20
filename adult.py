class Bird(object):
    feather = True
class Chicken(Bird): 
    fly = False
    def __init__(self, age):
        self.age = age
    def getAdult(self):
        if self.age > 1.0:
            return True
        else:
            return False
    adult = property(getAdult)


summer = Chicken(2)
print(summer.adult)
summer.age = 0.5
print(summer.adult)

class num(object):
    def __init__(self,value):
        self.value = value
    def getNeg(self):
        return -self.value
    def setNeg(self,value):
        self.value = -value
    def delNeg(self):
        print("value also deleted")
        del self.value
    neg = property(getNeg,setNeg,delNeg,"I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg