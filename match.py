import re
print re.match('Hello[\t]*(.*)world','Hello Wang world').group(1)
print re.match('/(.*)/(.*)/(.*)','/usr/home/lumberjack').groups()


List = ['wang','de','jun']
print List
List.append('shi')
print List
print List[1]
#List[99]=1
print List

ordList = [ord(x)**2 for x in 'spaam']
print ordList
ordSet = {ord(x) for x in 'spaam'}
print ordSet
ordDic = {x*2:ord(x) for x in "wangdejun"}
print ordDic
for m in ordDic:
    print ordDic[m]
    

Dic2={'a':1,'b':3,'c':332,'ab':2334}
print Dic2

for x in Dic2:
    print x.upper()
    print Dic2[x]



mm = 9
while mm >0:
    print (1*(9-mm))*" "+"WWW"*mm
    mm-=1
