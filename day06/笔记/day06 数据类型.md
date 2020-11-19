# day06 数据类型（中）

常见的数据类型：

- <span style="color:gray">int，整数类型（整形）</span>
- <span style="color:gray">bool，布尔类型</span>
- <span style="color:gray">str，字符串类型</span>
- **list，列表类型**
- **tuple，元组类型**
- <span style="color:gray">dict，字典类型</span>
- <span style="color:gray">set，集合类型</span>
- <span style="color:gray">float，浮点类型（浮点型）</span>

目标：掌握列表和元组数据类型的各种操作（知识点应用案例）。

课程概要：

- list，列表类型，用于存储一些数据的容器（有序 & 可修改）。【80%】
- tuple，元组类型，用于存储一些数据的容器（有序 & 不可修改）。【20%】



## 1.列表（list）

列表（list），是一个**有序**且**可变**的容器，在里面可以存放**多个不同类型**的元素。

### 1.1 定义

```python
user_list =  ["苍老师","有坂深雪","大桥未久"]
number_list = [98,88,666,12,-1]
data_list = [1,True,"Alex","宝强","贾乃亮"]
```

```python
user_list = []
user_list.append("铁锤")
user_list.append(123)
user_list.append(True)
print(user_list) # ["铁锤",123,True]
```

不可变类型：字符串、布尔、整型（已最小，内部数据无法进行修改）

可变类型：列表（内部数据元素可以修改）



### 1.2 独有功能

Python中为所有的列表类型的数据提供了一批独有的功能。

在开始学习列表的独有功能之前，先来做一个字符串和列表的对比：

- 字符串，不可变，即：创建好之后内部就无法修改。【独有功能都是新创建一份数据】

  ```python
  name = "alex"
  data = name.upper()
  print(name)
  print(data)
  ```

- 列表，可变，即：创建好之后内部元素可以修改。【独有功能基本上都是直接操作列表内部，不会创建新的一份数据】

  ```python
  user_list = ["车子","妹子"]
  user_list.append("嫂子")
  
  print(user_list) # ["车子","妹子","嫂子"]
  ```

列表中的常见独有功能如下：

1. 追加，在原列表中尾部追加值。

   ```python
   data_list = []
   
   v1 = input("请输入姓名")
   data_list.append(v1)
   
   v2 = input("请输入姓名")
   data_list.append(v2)
   
   print(data_list) # ["alex","eric"]
   ```

   ```python
   # 案例1
   user_list = []
   
   while True:
       user = input("请输入用户名(Q退出)：")
       if user == "Q":
           break
       user_list.append(user)
       
   print(user_list) 
   ```

   ```python
   # 案例2
   welcome = "欢迎使用NB游戏".center(30, '*')
   print(welcome)
   
   user_count = 0
   while True:
       count = input("请输入游戏人数：")
       if count.isdecimal():
           user_count = int(count)
           break
       else:
           print("输入格式错误，人数必须是数字。")
   
   
   message = "{}人参加游戏NB游戏。".format(user_count)
   print(message)
   
   
   user_name_list = []
   
   for i in range(1, user_count + 1):
       tips = "请输入玩家姓名（{}/{}）：".format(i, user_count)
       name = input(tips)
       user_name_list.append(name)
   
   print(user_name_list)
   ```

2. 批量追加，将一个列表中的元素逐一添加另外一个列表。

   ```python
   tools = ["搬砖","菜刀","榔头"]
   tools.extend( [11,22,33] ) # weapon中的值逐一追加到tools中
   print(tools) # ["搬砖","菜刀","榔头",11,22,33]
   ```

   ```python
   tools = ["搬砖","菜刀","榔头"]
   weapon = ["AK47","M6"]
   #tools.extend(weapon) # weapon中的值逐一追加到tools中
   #print(tools) # ["搬砖","菜刀","榔头","AK47","M6"]
   
   weapon.extend(tools)
   print(tools) # ["搬砖","菜刀","榔头"]
   print(weapon) # ["AK47","M6","搬砖","菜刀","榔头"]
   ```

   ```python
   # 等价于(扩展)
   weapon = ["AK47","M6"]
   for item in weapon:
       print(item)
   
   # 输出：
   #  AK47
   #  M6
   tools = ["搬砖","菜刀","榔头"]
   weapon = ["AK47","M6"]
   for item in weapon:
       tools.append(item)  
   print(tools) # ["搬砖","菜刀","榔头","AK47","M6"]
   ```

3. 插入，在原列表的指定索引位置插入值

   ```python
   user_list = ["苍老师","有坂深雪","大桥未久"]
   user_list.insert(0,"马蓉")
   user_list.insert(2,"李小璐")
   print(user_list)
   ```

   ```python
   # 案例
   name_list = []
   while True:
       name = input("请输入购买火车票用户姓名（Q/q退出）：")
       if name.upper() == "Q":
           break
       if name.startswith("刁"):
           name_list.insert(0, name)
       else:
           name_list.append(name)
   print(name_list)
   ```

4. 在原列表中根据值删除（从左到右找到第一个删除）【慎用，里面没有会报错】

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   user_list.remove("Alex")
   print(user_list)
   
   
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   if "Alex" in user_list:
   	user_list.remove("Alex")
   print(user_list)
   
   
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   while True:
       if "Alex" in user_list:
           user_list.remove("Alex")
   	else:
           break
   print(user_list)
   ```

   ```python
   # 案例：自动抽奖程序
   import random
   
   data_list = ["iphone12", "二手充气女友", "大保健一次", "泰国5日游", "避孕套"]
   
   while data_list:
       name = input("自动抽奖程序，请输入自己的姓名：")
   
       # 随机从data_list抽取一个值出来
       value = random.choice(data_list) # "二手充气女友"
       print( "恭喜{}，抽中{}.".format(name, value) )
       
       data_list.remove(value) # "二手充气女友"
   ```

5. 在原列表中根据索引踢出某个元素（根据索引位置删除）

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   #               0       1      2      3       4
   user_list.pop(1)
   print(user_list) #  ["王宝强","Alex","贾乃亮","Alex"]
   
   user_list.pop()
   print(user_list) # ["王宝强","Alex","贾乃亮"]
   
   item = user_list.pop(1)
   print(item) # "Alex"
   print(user_list) # ["王宝强","贾乃亮"]
   ```

   ```python
   # 案例：排队买火车票
   
   # ["alex","李杰","eric","武沛齐","老妖","肝胆"]
   user_queue = []
   
   while True:
       name = input("北京~上海火车票，购买请输入姓名排队(Q退出)：")
       if name == "Q":
           break
       user_queue.append(name)
   
   ticket_count = 3
   for i in range(ticket_count):
       username = user_queue.pop(0)
       message = "恭喜{},购买火车票成功。".format(username)
       print(message)
   
   # user_queue = ["武沛齐","老妖","肝胆"]
   faild_user = "、".join(user_queue) # "武沛齐、老妖、肝胆"
   faild_message = "非常抱歉，票已售完，以下几位用户请选择其他出行方式，名单：{}。".format(faild_user)
   print(faild_message)
   ```

6. 清空原列表

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   user_list.clear()
   print(user_list) # []
   ```

7. 根据值获取索引（从左到右找到第一个删除）【慎用，找不到报错】

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   #               0       1      2       3      4
   if "Alex" in user_list:
   	index = user_list.index("Alex")
   	print(index) # 2
   else:
       print("不存在")
   ```

8. 列表元素排序

   ```python
   # 数字排序
   num_list = [11, 22, 4, 5, 11, 99, 88]
   print(num_list)
   num_list.sort()  # 让num_list从小到大排序
   num_list.sort(reverse=True)  # # 让num_list从大到小排序
   print(num_list)
   
   
   # 字符串排序
   user_list = ["王宝强", "Ab陈羽凡", "Alex", "贾乃亮", "贾乃", "1"]
   #       [29579, 23453, 24378]
   #       [65, 98, 38472, 32701, 20961]
   #       [65, 108, 101, 120]
   #       [49]
   print(user_list)
   """
   sort的排序原理
       [ "x x x" ," x x x x x " ]
   """
   user_list.sort()
   print(user_list)
   ```

   注意：排序时内部元素无法进行比较时，程序会报错（尽量数据类型统一）。

9. 反转原列表

   ```python
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   user_list.reverse()
   
   print(user_list)
   ```

### 1.3 公共功能

1. 相加，两个列表相加获取生成一个新的列表。

   ```python
   data = ["赵四","刘能"] + ["宋晓峰","范德彪"]
   print(data) # ["赵四","刘能","宋晓峰","范德彪"]
   
   v1 = ["赵四","刘能"]
   v2 = ["宋晓峰","范德彪"]
   v3 = v1 + v2
   print(v3) # ["赵四","刘能","宋晓峰","范德彪"]
   ```

2. 相乘，列表*整型 将列表中的元素再创建N份并生成一个新的列表。

   ```python
   data = ["赵四","刘能"] * 2
   print(data) # ["赵四","刘能","赵四","刘能"]
   
   v1 = ["赵四","刘能"]
   v2 = v1 * 2
   print(v1) # ["赵四","刘能"]
   print(v2) # ["赵四","刘能","赵四","刘能"]
   ```

3. 运算符in包含
   由于列表内部是由多个元素组成，可以通过in来判断元素是否在列表中。

   ```python
   user_list = ["狗子","二蛋","沙雕","alex"] 
   result = "alex" in user_list
   # result = "alex" not in user_list
   print(result) #  True
   
   if "alex" in user_list:
       print("在，把他删除")
       user_list.remove("alex")
   else:
       print("不在")
   ```

   ```python
   user_list = ["狗子","二蛋","沙雕","alex"] 
   if "alex" in user_list:
       print("在，把他删除")
       user_list.remove("alex")
   else:
       print("不在")
   
   text = "打倒小日本"
   data = "日" in text
   ```

   ```python
   # 案例
   user_list = ["狗子","二蛋","沙雕","alex"] 
   if "alex" in user_list:
       print("在，把他删除")
       user_list.remove("alex")
   else:
       print("不在")
   ```

   ```python
   # 案例
   user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
   if "Alex" in user_list:
   	index = user_list.index("Alex")
   	user_list.pop(index)
   ```

   ```python
   # 案例：敏感词替换
   text = input("请输入文本内容：") # 按时打发第三方科技爱普生豆腐啊；了深刻的房价破阿偶打飞机
   forbidden_list = ["草","欧美","日韩"]
   for item in forbidden_list:
       text = text.replace(item,"**")
   print(text)
   ```

   注意：**列表检查元素是否存在时，是采用逐一比较的方式，效率会比较低。**

4. 获取长度

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   print( len(user_list) )
   ```

5. 索引，一个元素的操作

   ```python
   # 读
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   print( user_list[0] )
   print( user_list[2] )
   print( user_list[3] ) # 报错
   ```

   ```python
   # 改
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   user_list[0] = "武沛齐"
   print(user_list) # ["武沛齐","刘华强",'尼古拉斯赵四']
   ```

   ```python
   # 删
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   del user_list[1]
   
   user_list.remove("刘华强")
   ele = user_list.pop(1)
   ```

   注意：超出索引范围会报错。
   提示：由于字符串是不可变类型，所以他只有索引读的功能，而列表可以进行 读、改、删

6. 切片，多个元素的操作（很少用）

   ```python
   # 读
   user_list = ["范德彪","刘华强",'尼古拉斯赵四']
   
   print( user_list[0:2] ) # ["范德彪","刘华强"]
   print( user_list[1:] )
   print( user_list[:-1] )
   ```

   ```python
   # 改
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[0:2] = [11, 22, 33, 44]
   print(user_list) # 输出 [11, 22, 33, 44, '尼古拉斯赵四']
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[2:] = [11, 22, 33, 44]
   print(user_list) # 输出 ['范德彪', '刘华强', 11, 22, 33, 44]
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[3:] = [11, 22, 33, 44]
   print(user_list) # 输出 ['范德彪', '刘华强', '尼古拉斯赵四', 11, 22, 33, 44]
   
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[10000:] = [11, 22, 33, 44]
   print(user_list) # 输出 ['范德彪', '刘华强', '尼古拉斯赵四', 11, 22, 33, 44]
   
   
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   user_list[-10000:1] = [11, 22, 33, 44]
   print(user_list) # 输出 [11, 22, 33, 44, '刘华强', '尼古拉斯赵四']
   ```

   ```python
   # 删
   user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
   del user_list[1:]
   print(user_list) # 输出 ['范德彪']
   ```

7. 步长

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   #              0        1        2          3       4
   print( user_list[1:4:2] )
   print( user_list[0::2] )
   print( user_list[1::2] )
   print( user_list[4:1:-1] )
   ```

   ```python
   # 案例：实现列表的翻转
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   new_data = user_list[::-1]
   print(new_data)
   
   
   data_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   data_list.reverse()
   print(data_list)
   
   # 给你一个字符串请实现字符串的翻转？
   name = "武沛齐"
   name[::-1]
   ```

8. for循环

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   for item in user_list:
   	print(item)
   ```

   ```python
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   
   for index in range( len(user_list) ):
       item = user_index[index]
       print(item)
   ```

   切记，循环的过程中对数据进行删除会踩坑【面试题】。

   ```python
   # 错误方式， 有坑，结果不是你想要的。
   
   user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
   for item in user_list:
       if item.startswith("刘"):
           user_list.remove(item)
           
   print(user_list)
   
   
   ```

   ```python
   # 正确方式，倒着删除。
   user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
   for index in range(len(user_list) - 1, -1, -1):
       item = user_list[index]
       if item.startswith("刘"):
           user_list.remove(item)
   print(user_list)
   ```

### 1.4 转换

- int、bool无法转换成列表

- str

  ```python
  name = "武沛齐"
  
  data = list(name)  # ["武","沛","齐"]
  print(data)
  ```

- 超前

  ```python
  v1 = (11,22,33,44) # 元组
  vv1 = list(v1)     # 列表 [11,22,33,44]
  
  v2 = {"alex","eric","dsb"} # 集合
  vv2 = list(v2) # 列表 ["alex","eric","dsb"]
  ```

  

### 1.5. 其他

#### 1.5.1 嵌套

列表属于容器，内部可以存放各种数据，所以他也支持列表的嵌套，如：

```python
data = [ "谢广坤",["海燕","赵本山"],True,[11,22,[999,123],33,44],"宋小宝" ]
```

对于嵌套的值，可以根据之前学习的索引知识点来进行学习，例如：

```python
data = [ "谢广坤",["海燕","赵本山"],True,[11,22,33,44],"宋小宝" ]

print( data[0] ) # "谢广坤"
print( data[1] ) # ["海燕","赵本山"]
print( data[0][2] ) # "坤"
print( data[1][-1] ) # "赵本山"

data.append(666)
print(data) # [ "谢广坤",["海燕","赵本山"],True,[11,22,33,44],"宋小宝",666]

data[1].append("谢大脚")
print(data) # [ "谢广坤",["海燕","赵本山","谢大脚"],True,[11,22,33,44],"宋小宝",666 ]


del data[-2]
print(data) # [ "谢广坤",["海燕","赵本山","谢大脚"],True,[11,22,33,44],666 ]


data[-2][1] = "alex"
print(data) # [ "谢广坤",["海燕","赵本山","谢大脚"],True,[11,"alex",33,44],666 ]


data[1][0:2] = [999,666]
print(data) # [ "谢广坤",[999,666,"谢大脚"],True,[11,"alex",33,44],666 ]
```

```python
# 创建用户列表
#    用户列表应该长： [ ["alex","123"],["eric","666"] ]

# user_list = [["alex","123"],["eric","666"],]
# user_list.append(["alex","123"])
# user_list.append(["eric","666"])


user_list = []
while True:
    user = input("请输入用户名：")
    pwd = input("请输入密码：")

    data = []
    data.append(user)
    data.append(pwd)
    
    user_list.append(data)
```

```python
user_list = []
while True:
    user = input("请输入用户名(Q退出)：")
    if user == "Q":
        break
    pwd = input("请输入密码：")
    data = [user,pwd]
    user_list.append(data)

print(user_list)
```



### 1.6 列表阶段作业

1. 写代码，有如下列表，按照要求实现每一个功能。

   ```python
   li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
   ```

   - 计算列表的长度并输出
   - 列表中追加元素"seven",并输出添加后的列表
   - 请在列表的第1个索引位置插入元素"Tony",并输出添加后的列表
   - 请修改列表第2个索引位置的元素为"Kelly",并输出修改后的列表
   - 请将列表的第3个位置的值改成 "妖怪"，并输出修改后的列表
   - 请将列表 `data=[1,"a",3,4,"heart"]` 的每一个元素追加到列表 `li` 中，并输出添加后的列表
   - 请将字符串 `s = "qwert"`的每一个元素到列表 `li` 中。
   - 请删除列表中的元素"barry",并输出添加后的列表
   - 请删除列表中的第2个元素，并输出删除元素后的列表
   - 请删除列表中的第2至第4个元素，并输出删除元素后的列表

2. 写代码，有如下列表，利用切片实现每一个功能

   ```python
   li = [1, 3, 2, "a", 4, "b", 5,"c"]
   ```

   - 通过对li列表的切片形成新的列表 [1,3,2]
   - 通过对li列表的切片形成新的列表 ["a",4,"b"] 
   - 通过对li列表的切片形成新的列表  [1,2,4,5]
   - 通过对li列表的切片形成新的列表 [3,"a","b"]
   - 通过对li列表的切片形成新的列表 [3,"a","b","c"]
   - 通过对li列表的切片形成新的列表  ["c"]
   - 通过对li列表的切片形成新的列表 ["b","a",3]

3. 写代码，有如下列表，按照要求实现每一个功能。

   ```python
   lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
   ```

   - 将列表lis中的第2个索引位置的值变成大写，并打印列表。
   - 将列表中的数字3变成字符串"100"
   - 将列表中的字符串"tt"变成数字 101
   - 在 "qwe"前面插入字符串："火车头"

4. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：

   ```python
   0 武沛齐
   1 景女神
   2 肖大侠
   ```

5. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：

   ```python
   1 武沛齐
   2 景女神
   3 肖大侠
   ```

6. 写代码实现以下功能

   - 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：

     ```python
     0,汽车
     1,飞机
     2,火箭
     ```

   - 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。

7. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。

8. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：

   ```python
   [48,45,42...]
   ```

9. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。

   ```python
   li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
   ```

10. 将以下车牌中所有 `京 `的车牌搞到一个列表中，并输出京牌车辆的数量。

    ```python
    data = ["京1231", "冀8899", "京166631", "晋989"]
    ```



## 2.元组

列表（list），是一个**有序**且**可变**的容器，在里面可以存放**多个不同类型**的元素。

元组（tuple），是一个**有序**且**不可变**的容器，在里面可以存放**多个不同类型**的元素。

> 如何体现不可变呢？
> 记住一句话：《"我儿子永远不能换成是别人，但我儿子可以长大"》

### 2.1 定义

```python
v1 = (11,22,33)
v2 = ("李杰","Alex")
v3 = (True,123,"Alex",[11,22,33,44])

# 建议：议在元组的最后多加一个逗v3 = ("李杰","Alex",)
```

```python
d1 = (1)  # 1
d2 = (1,) # (1,)

d3 = (1,2)
d4 = (1,2)
```

注意：建议在元组的最后多加一个逗号，用于标识他是一个元组。

```python
# 面试题
1. 比较值 v1 = (1) 和 v2 = 1 和 v3 = (1,) 有什么区别？
2. 比较值 v1 = ( (1),(2),(3) ) 和 v2 = ( (1,) , (2,) , (3,),) 有什么区别？
              (1,2,3)
```

### 2.2 独有功能

无

### 2.3 公共功能

1. 相加，两个列表相加获取生成一个新的列表。

   ```python
   data = ("赵四","刘能") + ("宋晓峰","范德彪")
   print(data) # ("赵四","刘能","宋晓峰","范德彪")
   
   v1 = ("赵四","刘能")
   v2 = ("宋晓峰","范德彪")
   v3 = v1 + v2
   print(v3) # ("赵四","刘能","宋晓峰","范德彪")
   ```

2. 相乘，列表*整型 将列表中的元素再创建N份并生成一个新的列表。

   ```python
   data = ("赵四","刘能") * 2
   print(data) # ("赵四","刘能","赵四","刘能")
   
   v1 = ("赵四","刘能")
   v2 = v1 * 2
   print(v1) # ("赵四","刘能")
   print(v2) # ("赵四","刘能","赵四","刘能")
   ```

3. 获取长度

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',)
   print( len(user_list) )
   ```

4. 索引

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',)
   print( user_list[0] )
   print( user_list[2] )
   print( user_list[3] )
   ```

5. 切片

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',)
   print( user_list[0:2] )
   print( user_list[1:] )
   print( user_list[:-1] )
   ```

6. 步长

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   print( user_list[1:4:2] )
   print( user_list[0::2] )
   print( user_list[1::2] )
   print( user_list[4:1:-1] )
   ```

   ```python
   # 字符串 & 元组。
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   data = user_list[::-1]
   
   # 列表
   user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
   data = user_list[::-1]
   
   user_list.reverse()
   print(user_list)
   ```

7. for循环

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   for item in user_list:
   	print(item)
   ```

   ```python
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   for item in user_list:
    if item == '刘华强':
   	 continue
    print(name)
   ```

   目前：只有 str、list、tuple 可以被for循环。 "xxx"  [11,22,33]  (111,22,33)

   ```python
   # len + range + for + 索引
   user_list = ("范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能")
   for index in range(len(user_list)):
       item = user_list[index]
       print(item)
   ```

   



### 2.4 转换

其他类型转换为元组，使用`tuple(其他类型)`，目前只有字符串和列表可以转换为元组。

```python
data = tuple(其他)

# str / list 
```

```python
name = "武沛齐"
data = tuple(name)
print(data) # 输出 ("武","沛","齐")
```

```python
name = ["武沛齐",18,"pythonav"]
data = tuple(name)
print(data) # 输出 ("武沛齐",18,"pythonav")
```



### 2.5 嵌套

由于元组和列表都可以充当`容器`，他们内部可以放很多元素，并且也支持元素内的各种嵌套。

```python
tu = ( '今天姐姐不在家', '姐夫和小姨子在客厅聊天', ('姐夫问小姨子税后多少钱','小姨子低声说道说和姐夫还提钱') )
tu1 = tu[0]
tu2 = tu[1]
tu3 = tu[2][0]
tu4 = tu[2][1]
tu5 = tu[2][1][3]

print(tu1) # 今天姐姐不在家
print(tu2) # 姐夫和小姨子在客厅聊天
print(tu3) # 姐夫问小姨子税后多少钱
print(tu4) # 小姨子低声说道说和姐夫还提钱
```

练习题1：判断是否可以实现，如果可以请写代码实现。

```python
li = ["alex", [11,22,(88,99,100,),33],  "WuSir",  ("ritian", "barry",),  "wenzhou"]
#        0               1                 2                3                4

# 1.请将 "WuSir" 修改成 "武沛齐"
li[2] = "武沛齐"
index = li.index("Wusir")
li[index] = "武沛齐"

# 2.请将 ("ritian", "barry",) 修改为 ['日天','日地']
li[3] = ['日天','日地']

# 3.请将 88 修改为 87
li[1][2][0] = 87 # (报错，)

# 4.请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "周周"
# li.remove("wenzhou")
# del li[-1]
li.insert(0,"周周")
```

练习题2：记住一句话：《"我儿子永远不能换成是别人，但我儿子可以长大"》

```python
data = ("123",666,[11,22,33], ("alex","李杰",[999,666,(5,6,7)]) )

# 1.将 “123” 替换成 9   报错

# 2.将 [11,22,33] 换成 "武沛齐"    报错

# 3.将 11 换成 99
data[2][0] = 99
print(data)  # ("123",666,[99,22,33], ("alex","李杰",[999,666,(5,6,7)]) )

# 4.在列表 [11,22,33] 追加一个44
data[2].append(44)
print(data) # ("123",666,[11,22,33,44], ("alex","李杰",[999,666,(5,6,7)]) )
```

练习题3：动态的创建用户并添加到用户列表中。

```python
# 创建用户 5个
# user_list = [] # 用户信息
user_list = [ ("alex","132"),("admin","123"),("eric","123") ]

while True:
    user = input("请输入用户名：")
    if user == "Q":
        brek
    pwd = input("请输入密码：")
    item = (user,pwd,)
    user_list.append(item)
    
# 实现：用户登录案例
print("登录程序")
username = input("请输入用户名：")
password = input("请输入密码：")

is_success = False

for item in user_list:
    # item = ("alex","132")   ("admin","123")    ("eric","123")
    if username == item[0] and password == item[1]:
        is_success = True
        break

if is_success:
    print("登录成功")
else:
    print("登录失败")
```



















































