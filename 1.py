f = open('./file/data.txt','w')
f.write('Hello\n')
f.write('World\n')
f.write('wangdejun\n')
f.write('continue write some messages')
f.close()
m = open('./file_0/data.txt','w')
m.write('World\n')
m.close()

w = open('./file/data.txt')
text = w.read()
print text
