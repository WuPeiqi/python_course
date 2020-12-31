def func():
    print(123)
    print(123)
    yield 1234  # 有点像return，执行到这个位置之后，就不再执行。
    print(456)
    yield 666  # 有点像return，执行到这个位置之后，就不再执行。
    print(789)
    # return None # 程序就会报错，生成器中的代码执行完毕了 StopIteration


data = func()
# 基于for循环执行生成器对象
for item in data:
    # next(data)
    print(item)

"""
# 执行生成器函数时，函数体默认不会被执行；返回的是一个生成器对象。
v1 = func()
print(v1) # <generator object func at 0x7fd0280f75f0>

# next里面放生成器对象，进入生成器函数并执行其中的代码
n1 = next(v1)
print(n1)

# next里面放生成器对象，进入生成器函数并执行其中的代码（从上次yield返回位置继续向下）
n2 = next(v1)
print(n2)

# next里面放生成器对象，进入生成器函数并执行其中的代码（从上次yield返回位置继续向下）
n3 = next(v1)
"""
