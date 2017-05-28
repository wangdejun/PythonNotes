
##这一个函数所能达到的抽象能力让人吃惊，关键点在于list和list也可以判断是否相同
##给定一个list和一个item(这个item可能是int 可能是float, 也可能是另外一个list)
def count(sequence,item):
    result_count = 0

    for x in sequence:
        if x == item:
            result_count = result_count + 1
        else:
            pass

    return result_count