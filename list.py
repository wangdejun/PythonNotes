name = "wang de jun"
print name
# split在此地的方法与js是一样的，将一个字符串按某个字符拆分成为一个数组
name_arr = name.split(" ")
print name_arr


#注意extend和append的区别，extent有拍平的功能
#append会把数组作为一个独立的元素添加到数组尾部
name_arr2 = ["dejun","wang"]
name_arr.extend(name_arr2)
print name_arr

# name_arr.append(name_arr2)
print name_arr

print name_arr.index("dejun")

print name_arr.count("wang")