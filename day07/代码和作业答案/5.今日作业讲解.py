# 1.根据需求写代码
"""
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

dic['k4'] = "v4"
print(dic)

dic['k1'] = "alex"
print(dic)

dic['k3'].append(44)
print(dic)

dic['k3'].insert(1,18)
print(dic)

# 注意：int/float/bool/str/list/tuple/set/dict
"""

# 2.根据需求写代码
"""
dic1 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python1', 'python2', 100] }
}


dic1['name'].append("wusir")

new_name = dic1['name'][0].upper()
dic1['name'][0] = new_name

new_name = dic1['name'][0].capitalize()
dic1['name'][0] = new_name

dic1['oldboy']['老男孩'] = "linux"

dic1['oldboy']['alex'].remove("python2")

del dic1['oldboy']['alex'][1]

"""

# 3.循环提示用户输入，并将输入内容添加到字典中（如果输入N或n则停止循环）
"""
info = {}

while True:
    text = input("请输入内容（n/N退出)：")  # x1|wupeiqi
    if text.upper() == "N":
        break
    data_list = text.split("|")  # ["x1","wupeiqi"]
    info[data_list[0]] = data_list[1]

print(info)
"""

# 4.判断以下值那个能做字典的key ？那个能做集合的元素？
"""
[1,2]
{11,22,33,4}
{'name':'wupeiq','age':18}
"""

# 5.将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
"""
key_list = []
value_list = []
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for key, value in info.items():
    key_list.append(key)
    value_list.append(value)
print(key_list)
print(value_list)
"""
"""
key_list = []
value_list = []
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
key_list = list(info.keys())
value_list = list(info.values())
print(key_list)
print(value_list)
"""

# 6.字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
"""
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
for key in dic.keys():
    print(key)

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
for v in dic.values():
    print(v)

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
for k, v in dic.items():
    print(k, v)
"""

# 7.请循环打印k2对应的值中的每个元素。
"""
info = {
    'k1':'v1',
    'k2':[ ('alex'),('wupeiqi'),('oldboy')],
}

for item in info['k2']:
    print(item)

"""

# 8.有字符串"k: 1|k1:2|k2:3  |k3 :4" 处理成字典 {'k':1,'k1':2....}
"""
result = {}
text = "k: 1|k1:2|k2:3  |k3 :4"
data_list = text.split('|')  # ["k: 1","k1:2","k2:3  ","k3 :4"]
for item in data_list:
    # item # "k: 1"
    small_list = item.split(":")  # ["k"," 1"]
    result[small_list[0]] = int(small_list[1].strip())
print(result)
"""

"""
v = "k1:3"
v1, v2 = v.split(":")  # ["k1","3"]
print(v1, v2)
"""
"""
result = {}
text = "k: 1|k1:2|k2:3  |k3 :4"
data_list = text.split('|')  # ["k: 1","k1:2","k2:3  ","k3 :4"]
for item in data_list:
    key, value = item.split(":")  # ["k"," 1"]
    result[key] = int(value.strip())
print(result)
"""

# 9.写代码
"""
result = {'k1': [], 'k2': []}
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

for item in li:
    if item > 66:
        result['k1'].append(item)
    elif item == 66:
        pass
    else:
        result['k2'].append(item)
print(result)
"""

"""
# result = {"k1":[77,88]}
result = {}
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

for item in li:
    if item > 66:
        if "k1" in result:
            result['k1'].append(item)
        else:
            result['k1'] = [item]
    elif item == 66:
        pass
    else:
        if "k2" in result:
            result['k2'].append(item)
        else:
            result['k2'] = [item]
print(result)

"""

# 11.输出商品列表，用户输入序号，显示用户选中的商品
"""
商品列表：
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998}
    ]
要求:
1：页面显示 序号 + 商品名称 + 商品价格，如：
      1 电脑 1999 
      2 鼠标 10
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
"""

"""
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
for index in range(len(goods)):
    item = goods[index]
    print(index + 1, item['name'], item['price'])

while True:
    num = input("请输入要选择的商品序号(Q/q)：")  # "1"
    if num.upper() == "Q":
        break
    if num.isdecimal():
        num = int(num)
        if 0 < num < 5:
            target_index = num - 1
            choice_item = goods[target_index]
            print(choice_item["name"], choice_item['price'])
        else:
            print("序号范围选择错误")
    else:
        print("用户输入的序号格式错误")

# 注意：此示例是初级程序员会写的程序。
"""


"""
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
for index in range(len(goods)):
    item = goods[index]
    print(index + 1, item['name'], item['price'])

while True:
    num = input("请输入要选择的商品序号(Q/q)：")  # "1"
    if num.upper() == "Q":
        break
    if not num.isdecimal():
        print("用输入的格式错误")
        break
    num = int(num)

    if num > 4 or num < 0:
        print("范围选择错误")
        break
    target_index = num - 1
    choice_item = goods[target_index]
    print(choice_item["name"], choice_item['price'])
"""

"""
准则：
    - 尽可能少if嵌套
    - 简单的逻辑先处理
"""