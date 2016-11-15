print "wangdejun"

T = (1,2,3,4,5)
print T
print T+(6,7)
print T[0]


print T.index(5)
print T.count(5)

T = T+ (6,7,8,9,10,"wangdejun",[11,12,13,15],{"name":"wangdejun","address":"Beijing"})
print T

for x in T:
    print x
