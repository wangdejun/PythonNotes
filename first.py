#declare a class and definate a function in the class
class SampleMore(object):
    #transport the value self and a:
    def __call__(self,a):
        # return the sum: return a tuple
        return (a+5,a+6)


add = SampleMore()

print(add(2))
print map(add,[2,4,5])

new_values = SampleMore()
value1,value2 = new_values(100)
print value1,value2