#open a file and assign the handler to variable file,mode write
f = open('./file/data.txt','w')
#write the world Hello and changed to nextline
f.write('Hello\n')
f.write('World\n')
f.write('wangdejun\n')
f.write('continue write some messages')
f.close()
#close the handler
m = open('./file_0/data.txt','w')
m.write('World\n')
m.close()

w = open('./file/data.txt')
#assign the value to text
text = w.read()
print text
#close the file
w.close()