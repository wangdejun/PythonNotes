f = open('wangdata.txt','w')
f.write("Hello Nihao\n")
f.close()

f = open("wangdata.txt")
text = f.read()
print text
print text.split()
