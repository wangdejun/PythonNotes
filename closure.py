# in python ,everythig is a object

# def line_conf():
#     def line(x):
#         return 2*x + 1
# line_conf()
# print(line(5))


#closure

def line_conf_2():
    b = 15
    def line(x):
        return 2*x + b
    return line

b = 5
my_line = line_conf_2()
print(my_line(5))

#fanhan
def line_conf_3(a,b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf_3(1,1)
line2 = line_conf_3(4,5)
print(line1(5),line2(5))