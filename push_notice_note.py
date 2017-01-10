**需求描述

1.server按照时区发送notice

2.分别发送中英文版本

3.筛选发送国家

**解决办法是：

1.每条notice是一个任务，一个task。server定期来run这个job,用crontab文件,每过一小时执行一次。

2.把符合要求的task按照时区筛选出来，把符合要求的用户筛选出来，执行发送行为

3.每次发送都要存库，一遍轮到下一个时区的时候先查表，如果表中已经记录了，则skip掉，不筛选已经被skip掉的用户

4.服务器定期run 这个job，轮播发送，每小时定期run job,发送给符合要求的用户合适他们的Notice

**任务完结思考：

1.一开始设置的Q(query)条件变量覆盖范围非常大，query条件变量根据条件不断在缩减

2.如果有国家，筛选，没有国家，不筛选，即，query条件不变，懒变化的一个概念

3.如果语言中有中文版本，筛选复合条件的用户，发送中文任务；如果语言中有英文版本，筛选复合条件的英文用户，则发送英文消息，非常条理，丝毫不乱。

4.一种漂亮的python写法,用函数返回的元组直接赋值给目标元组,如下
    #noticehelper.py
    def sendNotice:
        pass
        return (a,b)
    import noticehelper
    #exec.py
    (a,b)=noticehelper.sendNotice(arguments)

