学习笔记

Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）



Number（数字）：
        Python3 支持 int、float、bool、complex（复数）
        在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long
        像大多数语言一样，数值类型的赋值和计算都是很直观的。

        赋值实例： 
            counter = 100          # 整型变量 int
            counter = 1000.0       # 浮点型变量 float
            counter = 9.322e-36j   # 复数型变量 complex
            counter = True         # 布尔型变量 bool 代表数字 1
            counter = False        # 布尔型变量 bool 代表数字 0

String（字符串）：
        Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

        赋值实例：
            str = 'Runoob'

        字符串的截取的语法格式如下：
        变量[头下标:尾下标]

        赋值实例：
            print (str[2:5])     # 输出从第三个开始到第五个的字符

        加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数

        赋值实例：
            print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str) 
            print (str + "TEST") # 连接字符串

        Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：    

        赋值实例：
            >>> print('Ru\noob')
            Ru
            oob
            >>> print(r'Ru\noob')
            Ru\noob
            
List（列表）：
        List（列表） 是 Python 中使用最频繁的数据类型。
        列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
        列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
        和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

        赋值实例：
            list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]

        列表截取的语法格式如下：
        变量[头下标:尾下标]
        索引值以 0 为开始值，-1 为从末尾的开始位置

        赋值实例：
            print (list[1:3])       # 从第二个开始输出到第三个元素

        加号 + 是列表连接运算符，星号 * 是重复操作

        赋值实例：
            tinylist = [123, 'runoob']  
            print (tinylist * 2)        # 输出两次列表  [123, 'runoob', 123, 'runoob']
            print (list + tinylist)     # 连接列表      ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']

        与Python字符串不一样的是，列表中的元素是可以改变的：

        赋值实例：
            >>> a = [1, 2, 3, 4, 5, 6]
            >>> a[0] = 9
            >>> a[2:5] = [13, 14, 15]

Tuple（元组）：
        元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
        元组中的元素类型也可以不相同：         

        赋值实例：
            tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )   

        元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）
        其实，可以把字符串看作一种特殊的元组

        赋值实例：
        >>> tup = (1, 2, 3, 4, 5, 6)
        >>> print(tup[0])
        1
        >>> print(tup[1:5])
        (2, 3, 4, 5)
        >>> tup[0] = 11  # 修改元组元素的操作是非法的


Set（集合）：
        集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
        基本功能是进行成员关系测试和删除重复元素。
        可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

        赋值实例：
        sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
        # set可以进行集合运算
        a = set('abracadabra')
        b = set('alacazam')
        print(sites)   # 输出集合，重复的元素被自动去掉 

        # 成员测试
        if 'Runoob' in sites :
            print('Runoob 在集合中')
        else :
            print('Runoob 不在集合中')
        print(a)
        print(a - b)     # a 和 b 的差集
        print(a | b)     # a 和 b 的并集
        print(a & b)     # a 和 b 的交集
        print(a ^ b)     # a 和 b 中不同时存在的元素

        输出：
        {'Zhihu', 'Baidu', 'Taobao', 'Runoob', 'Google', 'Facebook'}
        Runoob 在集合中
        {'b', 'c', 'a', 'r', 'd'}
        {'r', 'b', 'd'}
        {'b', 'c', 'a', 'z', 'm', 'r', 'l', 'd'}
        {'c', 'a'}
        {'z', 'b', 'm', 'r', 'l', 'd'}

Dictionary（字典）：
        字典（dictionary）是Python中另一个非常有用的内置数据类型。
        列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
        字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
        键(key)必须使用不可变类型。
        在同一个字典中，键(key)必须是唯一的。

        赋值实例：
        dict = {}
        dict['one'] = "1 - 教程"
        dict[2]     = "2 - 工具"
        tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
        print (dict['one'])       # 输出键为 'one' 的值
        print (dict[2])           # 输出键为 2 的值
        print (tinydict)          # 输出完整的字典
        print (tinydict.keys())   # 输出所有键
        print (tinydict.values()) # 输出所有值

        输出：
        1 - 教程
        2 - 工具
        {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
        dict_keys(['name', 'code', 'site'])
        dict_values(['runoob', 1, 'www.runoob.com'])

        构造函数 dict() 可以直接从键值对序列中构建字典如下：

        赋值实例：
            >>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
            {'Runoob': 1, 'Google': 2, 'Taobao': 3}
            >>> {x: x**2 for x in (2, 4, 6)}
            {2: 4, 4: 16, 6: 36}
            >>> dict(Runoob=1, Google=2, Taobao=3)
            {'Runoob': 1, 'Google': 2, 'Taobao': 3}