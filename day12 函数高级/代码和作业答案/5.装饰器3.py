# ############################# 大家的思路
"""
def func1():
    print('before 100')

    print("我是func1函数")
    value = (11, 22, 33, 44)

    print("after")
    return value


def func2():
    print('before 100')

    print("我是func2函数")
    value = (11, 22, 33, 44)

    print("after")
    return value


def func3():
    print('before 100')

    print("我是func3函数")
    value = (11, 22, 33, 44)

    print("after")
    return value


func1()
func2()
func3()
"""

# ############################# 我的思路
"""
def outer(origin):
    def inner():
        print("before 110")
        res = origin()  # 调用原来的func函数
        print("after")
        return res

    return inner


@outer
def func1():
    print("我是func1函数")
    value = (11, 22, 33, 44)
    return value


@outer
def func2():
    print("我是func2函数")
    value = (11, 22, 33, 44)
    return value


@outer
def func3():
    print("我是func3函数")
    value = (11, 22, 33, 44)
    return value


func1()
func2()
func3()
"""

# 应用场景
# - 少，你的思路。
# - 多，我的思路。
