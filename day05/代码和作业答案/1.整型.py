v1 = 5
print(bin(v1))  # 0b101
# 调用v1（int）的独有功能，获取v1的二进制有多少个位组成。
result1 = v1.bit_length()
print(result1)  # 3

v2 = 10
print(bin(10))  # 0b1010
# 调用v2（int）的独有功能，获取v2的二进制有多少个位组成。
result2 = v2.bit_length()
print(result2)  # 4


