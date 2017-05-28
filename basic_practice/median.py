def median(li):
    new_li = sorted(li)
    if(len(li)%2==0):
        return (new_li[len(li)/2-1]+new_li[len(li)/2])/2.0
    else:
        return new_li[len(li)/2]
