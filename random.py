import random
name = [{0},"wang",1,{"hello":"name"},{1},{2},{3}]
print random.choice(name)

obj = "wangdejun"
print obj.isalpha()


strname = "{0},wang,de,jun,{1},{2},{3}"
strname = strname.format('space1','space2','space3','space4')
print strname

help(strname.format)

S='A\nB\tC'
S2='\t'
S3='\n'
print len(S)
print len(S2)
print len(S3)

print ord("n")
print ord("m")
print ord('\n')


msg = """
aaaaaa
     bbbbb
          ccccc
    dddd
fff
"""
print msg

