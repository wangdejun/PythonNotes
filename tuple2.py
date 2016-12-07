#cmp(tuple1,tuple2)
tuple1, tuple2 = (123,'xyz'),(456,'abc')
print bool(cmp(tuple1,tuple2))
print cmp(tuple2,tuple1)
print cmp(tuple2,tuple2)
print cmp(tuple1,tuple2)

#len(tuple)

print(tuple1+tuple2)
print(len(tuple1+tuple2))
print(tuple1[0:2])
print(max(tuple1+tuple2),min(tuple1+tuple2))

name = [1,2,3,4,5,6]
name1 = tuple(name)
print name1