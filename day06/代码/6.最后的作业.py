# 1.以下哪些数据类型转换为布尔值为False
"""
0          False
1
""         False
-19
[]         False
[11,22]
(1)
(1,2,3)
()         False
"""

# 2.运算符操作
"""
v1 = [] or "alex"  # alex
v2 = [11, 22] and (1, 2,)  # (1, 2,)
"""

# 3.比较：` a = [1,2,3] `和 `b = [(1),(2),(3) ]` 以及 `c = [(1,),(2,),(3,) ]` 的区别？
"""
a = [1, 2, 3]
b = [(1), (2), (3)]
c = [(1,), (2,), (3,)]
"""

# 4.将字符串`text = "wupeiqi|alex|eric"`根据 `|` 分割为列表，然后列表转换为元组类型。
"""
text = "wupeiqi|alex|eric"
data_list = text.split("|")
result = tuple(data_list)
print(result)  # ('wupeiqi', 'alex', 'eric')
"""

# 5.补充代码，根据如下规则创建一副扑克牌（排除大小王）。
"""
# 花色列表
color_list = ["红桃", "黑桃", "方片", "梅花"]

# 牌值
num_list = []  # 1 2 3 4 5...11、12、13
for num in range(1, 14):
    num_list.append(num)

result = []
# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]
for color in color_list:
    # print(color) # 红桃
    for num in num_list:
        item = (color, num,)
        result.append(item)
print(result)
"""
