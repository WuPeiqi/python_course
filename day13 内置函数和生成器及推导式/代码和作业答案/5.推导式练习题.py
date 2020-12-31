"""
def func():
    print(123)


data_list = [func for i in range(10)]

print(data_list)
"""

"""
data_list = [lambda: 100 for i in range(10)]
print(data_list)
"""

"""
def func(num):
    return num + 100


data_list = [func(i) for i in range(10)] # [100,101...109]

print(data_list)
"""

# 示例：执行会失败
"""
def func(x):
    return x + i


data_list = [func for i in range(10)]  # [函数,函数,函数...]  i=9

val = data_list[5](100)  # 100+9
print(val)
"""

data_list = [lambda x: x + i for i in range(10)]  # [函数,函数,函数]   i=9

v1 = data_list[0](100)
v2 = data_list[3](100)
print(v1, v2)  # 109 109
