#装饰类

def decorator(aClass):
    class newClass:
        #类初始化
        def __init__(self,age):
            self.total_display = 0
            self.wrapped = aClass(age)
        #成员函数
        def display(self):
            self.total_display += 1
            print ("total display" ,self.total_display)
            self.wrapped.display()
    #返回这个新的类
    return newClass

#使用装饰器
@decorator
#定义类：
class Bird:
    def __init__(self,age):
        self.age = age
    def display(self):
        print("My age is ",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()