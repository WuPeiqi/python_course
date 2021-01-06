import time

print("开始下载")
for i in range(1, 101):
    data = "\r{}%".format(i)
    print(data, end="")
    time.sleep(0.02)

print("\n下载完成")
