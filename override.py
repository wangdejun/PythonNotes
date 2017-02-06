##调用类实例化对象，并且使用成员函数

class Car():
    def exclaim(self):
        print ("I'm a Car!")

class Yugo():
    def exclaim(self):
        print ("I'm Yugo,Much like a car,but more Yugo-ish!")


#use the class Car to create instance
give_me_a_car = Car()
#use the class Yugo() instance
give_me_a_yugo = Yugo()

#call the instance object member function
give_me_a_car.exclaim()
#call the instance object created by Yugo member function
give_me_a_yugo.exclaim()

