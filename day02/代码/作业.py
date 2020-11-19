score = input("请输入分数")
data = int(score)

if 90 <= data <= 100:
    print("A")
elif 80 <= data < 90:
    print("B")
elif 60 <= data < 80:
    print("C")
elif 40 <= data < 60:
    print("D")
elif 0 <= data < 40:
    print("E")
else:
    print("输入错误")
