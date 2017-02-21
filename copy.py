a = ["wang","de","jun"]
b = a

##list()方法和[:]是复制赋值的
c = list(a)
d = a[:]
print a
print b
print c
print d
a[0]="li"
print a
print b
print c
print d
# 运行结果：
# ['wang', 'de', 'jun']
# ['wang', 'de', 'jun']
# ['wang', 'de', 'jun']
# ['wang', 'de', 'jun']
# ['li', 'de', 'jun']
# ['li', 'de', 'jun']
# ['wang', 'de', 'jun']
# ['wang', 'de', 'jun']
