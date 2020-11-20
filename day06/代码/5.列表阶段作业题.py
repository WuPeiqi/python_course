# ####################### 第1题 #######################
"""
li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]

# print(len(li))

# li.append("seven")
# print(li)

# li.insert(1,"Tony")
# print(li)

# li.insert(2,"Kelly")
# print(li)

# li[3] = "妖怪"
# print(li)

# data = [1, "a", 3, 4, "heart"]
# li.extend(data)
# print(li)

# s = "qwert"
# for item in s:
#     li.append(item)
# print(li)
# li.extend("qwert")
# print(li)

# li.remove("barry")

# del li[1]
# ele = li.pop(1)
# print(li)

# del li[2:4]

"""

# ####################### 第2题 #######################
"""
li = [1, 3, 2, "a", 4, "b", 5,"c"]

# print(li[0:3])

# print(li[3:6])

# print(li[:-1:2])
# print(li[::2])

# print(li[1:-1:2])

# print(li[1::2])

# print(li[7:])

# print(li[5:0:-2])
"""
# ####################### 第3题 #######################
"""
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

# data = lis[2].upper()
# lis[2] = data
# lis[2] = lis[2].upper()

# lis[1] = "100"
# lis[3][2][1][1] = "100"
# print(lis)

# lis[3][2][1][0] = 101

# lis[3].insert(0,"火车头")
# print(lis)

"""
# ####################### 第4题 #######################
"""
users = ["武沛齐", "景女神", "肖大侠"]
count = 0
for item in users:
    print(count, item)
    count += 1
"""
"""
users = ["武沛齐", "景女神", "肖大侠"]
for index in range(len(users)):
    print(index, users[index])
"""

# ####################### 第5题 #######################
"""
users = ["武沛齐", "景女神", "肖大侠"]
for index in range(len(users)):
    print(index + 1, users[index])
"""

# ####################### 第6题 #######################
"""
goods = ['汽车', '飞机', '火箭']
for index in range(len(goods)):
    print(index, goods[index])
index = input("请输入序号：")  # "1"
index = int(index)
text = goods[index]
message = "您选择的商品是{}".format(text)
print(message)
"""

# ####################### 第7题 #######################
"""
data_list = []
for num in range(0,51):
    if num == 0:
        continue
    # 是否能被3整除呢？
    data = num % 3
    if data == 0:
        data_list.append(num)
print(data_list)
"""

# ####################### 第8题 #######################
"""
data_list = []
for num in range(0,51):
    if num == 0:
        continue
    # 是否能被3整除呢？
    data = num % 3
    if data == 0:
        data_list.insert(0,num)
print(data_list)
"""

# ####################### 第9题 #######################
"""
data_list = []
li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
for item in li:
    data = item.strip()
    if data.startswith("a"):
        data_list.append(data)
print(data_list)
"""

"""
data_list = []
li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
for item in li:
    data = item.strip()
    if not data.startswith("a"):
        continue
    data_list.append(data)
print(data_list)
"""

# ####################### 第10题 #######################
"""
# 将以下车牌中所有 `京 `的车牌搞到一个列表中，并输出京牌车辆的数量。
result = []
data = ["京1231", "冀8899", "京166631", "晋989"]
for item in data:
    if not item.startswith("京"):
        continue
    result.append(item)

count = len(result)
print( "京牌的数据为：{}".format(count) )
"""