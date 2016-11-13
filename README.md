##Python Object Types
####intro
*    1.程序由模块组成
*    2.模块包含语句
*    3.语句包含表达式
*    4.表达式建立并处理对象
    强大的对象类型
    集合：list
    搜索表：字典
*    内置对象是扩展的组件
*    内置对象往往比定制的数据结构更有效率
*    内置对象是语言标准的一部分
#Python 的内置对象类型
##数字（Number）
    **表示乘方
    import math
    math.pi
    math.sqrt(8)#开方

    import random
    random.random()
    random.choice([1,2,3,4])
##字符串（String）
####基本操作
    len(S)
    S[0]
    S[1]
    S[-1]                                   #从后数倒数第一个
    S[-2]                                   #从后数倒数第二个
    S[-1]  --------> S[len(S)-1]  # 是等效的
####分片（slice）操作
    S[1:3]
    S[1:]
    S[:3]
    S[:-1]  -------> S[0:-1]         #除去最后一个的
    S[ : ]                                    #全量
注意负偏移量如何作分片的边界,在上面最后一个操作中如何有效地拷贝整个字符串，正像今后学到的那样，没有必要拷贝一个字符串，但是这种操作形式在列表这样的序列中很有用。
####concatenation连缀
    S+”String”
####Repetition复制
    S*8
####帮助函数
    help(S.replace)                  #查询replace方法是做什么的，你可以将其传递给help函数
####二进制ASCII码表
    ord(‘\n’)     #二进制ASCII码表值(参数只能是一个字符，而不能是一个字符串)
####模式匹配
    import re
    print re.match('Hello[\t]*(.*)world','Hello Wang world').group(1)
    print re.match('/(.*)/(.*)/(.*)','/usr/home/lumberjack').groups()

##列表(LIST)
    len(L)
    L[0]            #获取列表的第一个元素
    L[:3]           #切分一个列表并且返回一个新的列表
    L+[4,5,6]    #连缀concatenation两个列表
    L
    python的列表与其他语言中的数组有些类似，
    但是列表要强大得多，
*         其中一个方面是列表没有固定类型的约束。可以包括一个整数，一个字符串，以及一个浮点数
*         另一方面是列表没有固定大小，因此能够按照需要增大或减少列表大小，以响应其操作。
####常规操作
    L.append(“NI”)             #在结尾添加一个”NI”元素
    L.pop(2)                        #弹出index值为2的元素
    L.insert(“wangdejun”)   #在任意位置插入元素
    L.remove(“wang”)         #按照值移除元素
    L.sort()                           #进行排序
    L.reverse()                     #进行翻转
####边界检查
    L[99]
    IndexError: list index out of range
    L[99]==1
    IndexError: list assignment index out of range
    这也是比C语言之类的语言好的原因，自动进行边界检查，如果要对列表进行添值的操作的话，可以使用append方法，而不要直接使用由参取值再赋值的套路
####嵌套
python核心数据类型的一个优秀特性就是他们支持任意的嵌套，
    能够以任意的组合进行嵌套
    多个层级进行嵌套：一个列表包含一个字典，另一个字典中包含另一个列表，
        这种特性直接的应用==>能够实现矩阵
                                        ==>Python中的多维数组，
    这样的结构可以通过两种方法获取元素
    M[1]        :第二行数据
    M[1][2]    :第二行第三列元素数据
####注
    对于更加重要的数值运算而言，你可能会想要使用如NumPy这样的工具系统；
    NumPy包
    能以更高效的的方式存储并处理大型矩阵，胜过嵌套列表结构
    被看做是Matlab，功能更强大
    NASA, LosAlamos JPMorgan Chase使用这个工具从事科学和金融工作
    
####列表解析
    col2 = [row[1] for row in M]
    col3 = [row[1]+1 for row in M]
    col4 = [row[1] for row in M if row[1]%2==0]  //把偶数挑出来filter

    在python3.0中，列表，集合和字典都可以用解析来创建
    ordList = [ord(x)**2 for x in 'spaam']
    print ordList
    ordSet = {ord(x) for x in 'spaam'}
    print ordSet
    ordDic = {x*2:ord(x) for x in "wangdejun"}
    print ordDic
    for m in ordDic:
        print ordDic[m]
##字典

*     python字典是完全不同的东西，
*     不是序列，而是一种映射（Mapping）
*     映射是一个其他对象的集合，
*     通过key而不是相对位置来存储的。
*     核心对象集合
*     可变伸缩，像列表灵活
####两种新建字典的方式

    D = {'food':'bread','quantity':4}
    print D
    print D['food']
    print D["food"]

    Dic = {}
    Dic['name']="Apple"
    Dic['quantity']=2300
    Dic['food']="Apple Pie"
    print Dic

####字典的灵活性
    rec = {
        'name':{'first':'Bob','last':'Smith'},
        'job':['dev','mgr'],
        'age':40.5,
    }
    print rec

    rec['job'].append('janitor');
    rec['job'].append('writer');
    print rec
    for x in rec:
        print x+'\t’
*     最后一次引用对象后（将这个变量用其他的值进行赋值），这个对象占有的内存空间将会被清除
*     能自由地使用对象，不必创建空间，也不必手动释放内存

####键的排序
####优化迭代
*     列表解析工具和相关的函数编程工具如map和Filter通常运转得比for循环快，
*     这是对大数据集合的程序由重大影响的特性

##元祖
##文件 myfile = open(‘eggs’,’r’)
集合 set(‘abc’),{‘a’,’b’,’c’}
None
布尔型
    编程单元类型：函数，模块，类  ||def class import lambda这样的语句和表达式创建，并且可以在脚本间自由传递
    与实现相关的类型：编译的代码堆栈

    python没有类型，运行的表达式语法决定了创建和使用的对象的类型
    一旦创建了一个对象，它就和操作集合绑定了
    列表和字典就是强大的数据表现工具，省略了在使用底层语言过程中为了支持集合和搜索而引入的绝大部分工作
    列表提供了其他对象的有序集合
    字典是通过key-value来储存的。字典和列表都可以嵌套，可以随需求扩展和删减，并能够包含任意类型的对象。
