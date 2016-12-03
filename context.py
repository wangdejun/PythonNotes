f = open("data.txt","w")
print(f.closed)

f.write("Hello,World!")
f.close()
print(f.closed);


with open("data.txt","w") as f:
    print(f.closed)
    f.write("Hello,World ,This is the second time")
print(f.closed)

class VOW(object):
    def __init__(self,text):
        self.text = text
    def __enter__(self):
        self.text = "I say "+self.text
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        self.text = self.text +"!"

with VOW("I'm fine") as myvow:
    print (myvow.text)

print(myvow.text)


class bird(object):
    feather = True
class chicken(bird):
    fly = False
    def __init__(self,age):
        self.age = age
    def __getattr__(self,name):
        if name == 'adult':
            if self.age > 1.0:
                return True
            else:
                return False
        else:
            raise AttributeError(name)

summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)