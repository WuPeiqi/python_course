import time

v1 = time.time()
print(v1)  # 1609750346.687055

v2 = time.timezone
print(v2, v2 / 60 / 60)

print("开始")
time.sleep(1.5)
print("结束")

# while True:
#     time.sleep(1)
#     print(123123)
