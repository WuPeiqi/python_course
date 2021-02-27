# 1. 列举面向对象的成员并简述他们的特点。
"""
- 变量
    - 实例变量，属于对象。每个对象中中都封装各自的值。只能通过的对象来进行调用。
    - 类变量，属于类。每个类中各自保存的数据。可以通过对象和类来进行读取。
- 方法
    - 绑定方法，默认有一个self参数，由对象进行调用（此时self就等于调用方法的这个对象）【对象&类均可调用】
    - 类方法，默认有一个cls参数，用类或对象都可以调用（此时cls就等于调用方法的这个类）【对象&类均可调用】
    - 静态方法，无默认参数，用类和对象都可以调用。【对象&类均可调用】
- 属性
    基于方法+property装饰器实现可以实现，可以实现
        obj.属性名
        obj.属性名 = 123
        del obj.属性名
    语法和方法的对应关系。
"""

# 2. @staticmethod 和 @classmethod的作用是什么？
"""
@classmethod，将一个方法变换类方法；类和方法都可以调用，且cls默认是当前执行该方法的类。
@staticmethod，将一个方法变换为静态方法，静态方法的调用可以是类也可以对象，无默认参数。
"""

# 3. 面向对象中如何让成员变为私有。
"""
前面加上 __
"""

# 4.  `__new__`方法的作用？
"""
__new__是构造方法，用于创建对象（空对象），在__init__方法执行之前。
"""

# 5. 简述你理解的：迭代器、生成器、可迭代对象。
"""
迭代器，含有__iter__方法和__next__方法，__iter__返回自身，__next__可以获取数据（终止是抛出StopIteration异常。可以被for循环。
生成器，在定义时是函数中重要包含yield就是生成器函数，执行函数获得生成器对象（一种特殊的迭代器）；可以通过next取值 & 也可以通过for循环取值。
可迭代对象，含有 __iter__方法，且返回一个迭代器对象。可以被for循环。
"""

# 6. 看代码写结果
"""
666
1
18
99
1
999
999
1
99
"""

# 7. 看代码写结果，注意返回值。
"""
f3
f2
999
None
"""

# 8. 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""
class Foo(object):
    
    def f1(self):
        print('f1')

    @staticmethod
    def f2():
        print('f2')
        
obj = Foo()
obj.f1() # f1
obj.f2() # f2

Foo.f1() # 报错
Foo.f2() # f2
"""

# 9.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""
f1
f2
f3
"""

# 10.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""
f1
f2
f3
"""

# 11.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""
class Foo(object):
    a1 = 1
    __a2 = 2

    def __init__(self, num):
        self.num = num
        self.__salary = 1000

    def show_data(self):
        print(self.num + self.a1)


obj = Foo(666)

print(obj.num)  # 666
print(obj.a1)  # 1
print(obj.__salary)  # 报错
print(obj.__a2)  # 报错
print(Foo.a1)  # 1
print(Foo.__a2)  # 报错
obj.show_data()  # 667
"""

# 12.看代码写结果
"""
8
8 None
9
9 None
"""

# 13.看代码写结果
"""
1 1
666
666
"""

# 14.看代码写结果
"""
class Foo(object):
    def __init__(self, num):
        self.num = num


v1 = [Foo for i in range(10)]
v2 = [Foo(5) for i in range(10)]
v3 = [Foo(i) for i in range(10)]

print(v1)  # [类,类,类...]
print(v2)  # [对象(num=5),对象(num=5),对象(num=5)..]
print(v3)  # [对象(num=0),对象(num=1),对象(num=2)..]
"""

# 15.看代码写结果
"""
1
2
3
"""

# 16.看代码写结果
"""
1 666
2 666
3 666
"""

# 17. 看代码写结果
"""
3
19 5
20 5
666 33
"""

# 18. 看代码写结果
"""
class StarkConfig(object):
    def __init__(self, num):
        self.num = num

    def run(self):
        self()

    def __call__(self, *args, **kwargs):
        print(self.num)


class RoleConfig(StarkConfig):
    def __call__(self, *args, **kwargs):
        print(345)

    def __getitem__(self, item):
        return self.num[item]


v1 = RoleConfig('alex')
v2 = StarkConfig("wupeiqi")

print(v1[1]) # l
print(v2[2]) # 报错
"""

# 19.补全代码
"""
class Context:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def do_something(self):
        pass


with Context() as ctx:
    ctx.do_something()
"""

# 20.看代码写结果
"""
我是武沛齐,年龄18,属于人事部
我是alex,年龄18,属于人事部
"""

# 21.分析代码关系，并写出正确的输出结果。
"""
中国
Node对象（title=河南省）
河南省
Node对象（title=河北省）
河北省
"""

# 22. 分析代码关系，并写出正确的输出结果。
"""
中国
河南省
河北省
石家庄
廊坊
雄安
"""
