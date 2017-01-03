# a = ["wang","de","jun"]
# b = a
# print a
# print b
# a[0]="li"
# print a
# print b

# # output:
# # ['wang', 'de', 'jun']
# # ['wang', 'de', 'jun']
# # ['li', 'de', 'jun']
# # ['li', 'de', 'jun']


a = ["wang","de","jun"]
b = a
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
