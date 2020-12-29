"""
需求：请实现在函数执行前输入before，执行后输出after

"""

# def func():
#     print("我是func函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# result = func()
# print(result)

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
def func():
    print("我是func函数")
    value = (11, 22, 33, 44)
    return value


def outer(origin):
    def inner():
        print("before")
        res = origin()  # 调用原来的func函数
        print("after")
        return res

    return inner


func = outer(func)

result = func()
print(result)
"""
