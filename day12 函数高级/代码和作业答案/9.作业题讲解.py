# ################### 第1题 ###################
"""
import functools


def outer(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        # print("before")
        res = function(*args, **kwargs)  # 执行原函数
        print("after")
        return res

    return inner


@outer
def func(a1):
    return a1 + "傻叉"


@outer
def base(a1, a2):
    return a1 + a2 + '傻缺'


@outer
def foo(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4 + '傻蛋'
"""

# ################### 第2题 ###################
"""
import random
import functools


def five_times(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        data_list = []
        for i in range(5):
            res = function(*args, **kwargs)  # 执行原函数
            data_list.append(res)
        return data_list

    return inner


@five_times
def func():
    return random.randint(1, 4)


result = func()  # 内部自动执行5次，并将每次执行的结果追加到列表最终返回给result
print(result)
"""

# ################### 第3题 ###################
"""
import os
import functools


def gard(function):
    @functools.wraps(function)
    def inner(path):

        # 获取路径的上级目录
        # folder_path = path.rsplit('/', 1)[0]
        folder_path = os.path.dirname(path)

        # 不存在，就创建
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        res = function(path)
        return res

    return inner


@gard
def write_user_info(path):
    file_obj = open(path, mode='w', encoding='utf-8')
    file_obj.write("武沛齐")
    file_obj.close()


write_user_info('/Users/wupeiqi/PycharmProjects/luffyCourse/day12/xxx.txt')
"""


# ################### 第4~8题 ###################
# 分析过程，请参见视频讲解
def func(val):
    def inner(a1, a2):
        return a1 + a2 + val

    return inner


data_list = []

for i in range(10):
    data_list.append(func(i))
# data_list 是inner函数列表
v1 = data_list[0](11, 22)  # 11+22+0
v2 = data_list[2](33, 11)  # 33+11+2

print(v1)
print(v2)
