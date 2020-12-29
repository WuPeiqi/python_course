# ########## 大家的思路【胜出】
"""
def func():
    print("before")

    print("我是func函数")
    value = (11, 22, 33, 44)

    print('after')
    return value


result = func()
print(result)
"""

# ########## 我的思路
"""
python中支持特殊语法，在某个函数上方使用： 

@函数名
def xxx():
    pass

Python内部会自动执行 函数名(xxx) ，执行完之后，再讲结果赋值给 xxx。
xxx = 函数名(xxx)

"""

"""
def outer(origin):
    def inner():
        print("before")
        res = origin()  # 调用原来的func函数
        print("after")
        return res

    return inner


@outer  # func = outer(func)
def func():
    print("我是func函数")
    value = (11, 22, 33, 44)
    return value


result = func()
print(result)
"""