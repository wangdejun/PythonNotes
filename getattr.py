B = {"name":"wang","age":"18","college":"Algriculture"}
for w in B:
    print "%s:%s" %(w, B[str(w)])
    # print B[str(w)]
    # print getattr(B,str(w))

arr = ["zh","en"]
arr_str = "zh;en"
print not "zh" in arr
print "en" in arr_str