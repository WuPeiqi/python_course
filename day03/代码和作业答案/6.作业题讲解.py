# 4. 实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）。
"""
count = 0
while count < 3:
    count += 1
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    if user == "wupeiqi" and pwd == "123":
        print("成功")
        break
    else:
        message = "用户名或者密码错误，剩余错误次数为{}次".format(3 - count)
        print(message)
"""

"""
count = 3
while count > 0:
    count -= 1
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    if user == "wupeiqi" and pwd == "123":
        print("成功")
        break
    else:
        message = "用户名或者密码错误，剩余错误次数为{}次".format(count)
        print(message)
"""

# 5.猜年龄游戏
"""
count = 0
while count < 3:
    count += 1
    age = input("请输入年龄：")
    age = int(age)
    if age == 73:
        print("恭喜你猜对了")
        break
    else:
        print("猜错了")

print("程序结束")
"""

# 6. 升级版猜年龄
# 允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
count = 0
while count < 3:
    count += 1
    age = input("请输入年龄：")
    age = int(age)
    if age == 73:
        print("恭喜你猜对了")
        break
    else:
        print("猜错了")

    if count == 3:
        choice = input("是否想继续玩(Y/N)？")
        if choice == "N":
            break
        elif choice == "Y":
            count = 0
            continue
        else:
            print("内容输入错误")
            break

print("程序结束")

