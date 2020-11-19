# 1. 猜数字，设定一个理想数字比如：66，一直提示让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有输入等于66，显示猜测结果正确，然后退出循环。
"""
data = True
while data:
    num = input("请输入数字：")
    num = int(num)
    if num > 66:
        print("大了")
    elif num < 66:
        print("小了")
    else:
        print("正确")
        data = False
"""

# 2. 使用循环输出1~100所有整数。
"""
num = 1
while num < 101:
    print(num)
    num = num + 1
"""
# 3. 使用循环输出 1 2 3 4 5 6   8 9 10，即：10以内除7以外的整数。
"""
num = 1
while num < 11:
    if num == 7:
        pass
    else:
        print(num)
    num = num + 1
"""
"""
num = 1
while num < 11:
    if num != 7:
        print(num)
    num = num + 1
"""
# 4. 输出 1~100 内的所有奇数。
"""
num = 1
while num < 101:
    if num % 2 == 1:
        print(num)
    num = num + 1
"""

# 5. 输出 1~100 内的所有偶数。
"""
num = 1
while num < 101:
    if num % 2 == 0:
        print(num)
    num = num + 1
"""
# 6. 求 1~100 的所有整数的和。
"""
total = 0 # 0 + 1 /  0 + 1 + 2 / 0 + 1 + 2 + 3 ...
num = 1
while num < 101:
    total = total + num
    num = num + 1
print(total)
"""
# 7. 输出 10 ~ 1 所有整数。
"""
num = 10
while num > 0:
    print(num)
    num = num - 1
"""

## 思考题：求 1~100 的所有整数这样的结果： 1 - 2 + 3 - 4 + 5 - 6 = ?

