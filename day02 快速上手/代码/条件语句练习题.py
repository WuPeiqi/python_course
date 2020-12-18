# 1. 提示用户输入用户名和密码，用户名等于"wupeiqi"且密码等于"uuu"就输出登录成功；否则输出登录失败。
"""
user = input("请输入用户名:")
pwd = input("请输入密码:")
if user == "wupeiqi" and pwd == "uuu":
    print("登陆成功")
else:
    print("登陆失败")
"""
# 2. 猜数字，提示用户输入一个数字，判断数字如果大于10，就输出猜错了；否则输出猜对了。
"""
num = input("请输入数字：") # "123"
if int(num) > 10:
    print("猜错了")
else:
    print("正确")
"""
# 3. 提示用户输入一个数字，判断是否为偶数，是偶数则输出 偶偶偶数，否则输出 奇奇奇数。
"""
num = input("请输入数字：")
new_num = int(num)
if new_num % 2 == 1:
    print("奇奇奇数")
else:
    print("偶偶偶数")
"""
