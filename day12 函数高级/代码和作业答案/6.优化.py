"""
def outer(origin):
    def inner():
        print("before 110")
        res = origin()  # 调用原来的func函数
        print("after")
        return res

    return inner


@outer  # func1 = outer(func1)
def func1():
    print("我是func1函数")
    value = (11, 22, 33, 44)
    return value


@outer  # func2 = outer(func2)
def func2():
    print("我是func2函数")
    value = (11, 22, 33, 44)
    return value


@outer  # func3 = outer(func3)
def func3():
    print("我是func3函数")
    value = (11, 22, 33, 44)
    return value


func1()
func2()
func3()
"""


# ############ 函数有参数

def outer(origin):
    def inner(*args, **kwargs):
        print("before 110")
        res = origin(*args, **kwargs)  # 调用原来的func函数
        print("after")
        return res

    return inner


@outer  # func1 = outer(func1)
def func1(a1):
    print("我是func1函数")
    value = (11, 22, 33, 44)
    return value


@outer  # func2 = outer(func2)
def func2(a1, a2):
    print("我是func2函数")
    value = (11, 22, 33, 44)
    return value


@outer  # func3 = outer(func3)
def func3(a1):
    print("我是func3函数")
    value = (11, 22, 33, 44)
    return value


func1(1)
func2(11, a2=22)
func3(999)
