try:
    fh = open("_wangdata1.txt","w")
    fh.write("this is a test file ,fo exception")
except IOError:
    print "Error:not found"
else:
    print "file write successfully"
    fh.close()