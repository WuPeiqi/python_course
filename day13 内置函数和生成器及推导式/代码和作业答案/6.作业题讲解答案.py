# 第1题：参考视频的分析过程（也可以自己运行比较结果是否与你分析一致）

# 第2题：参考视频的分析过程（也可以自己运行比较结果是否与你分析一致）

# 第3题：参考视频的分析过程（也可以自己运行比较结果是否与你分析一致）

# 第4题
"""
data_list = [11, 22, 33, "alex", 455, 'eirc']

new_data_list = [item for item in data_list if type(item) == int]  # 请在[]中补充代码实现。
print(new_data_list)
"""
# 第5题
"""
data_list = [11, 22, 33, "alex", 455, 'eirc']

new_data_list = [len(item) if type(item) == str else item + 100 for item in data_list]
print(new_data_list)
"""

# 第6题
"""
data_list = [
    (1, 'alex', 19),
    (2, '老男', 84),
    (3, '老女', 73)
]

info_dict = {item[0]: item for item in data_list}
print(info_dict)
"""

# 第7题
"""
player = {
    "武沛齐": ["红桃", 10],
    "alex": ["红桃", 8],
    'eric': ["黑桃", 3],
    'killy': ["梅花", 12],
}

winner = sorted(player.items(), key=lambda x: x[1][-1], reverse=True)[0][0]
print(winner)

data = sorted(player.items(), key=lambda x: x[1][1])[-1][0]
print(data)
"""


# 第8题（自己写就好）

# 第9题
def fib(max_count):
    first = 1
    second = 0
    count = 0
    while count < max_count:
        next_value = first + second
        first = second
        second = next_value
        yield next_value
        count += 1


limit_count = input("请输入要生成斐波那契数列的个数：")
limit_count = int(limit_count)
fib_generator = fib(limit_count)
for num in fib_generator:
    print(num)
