def func():
    print(111)
    v1 = yield 1
    print(v1)

    print(222)
    v2 = yield 2
    print(v2)

    print(333)
    v3 = yield 3
    print(v3)

    print(444)


data = func()

n1 = data.send(None)
print(n1)

n2 = data.send(666)
print(n2)

n3 = data.send(777)
print(n3)

n4 = data.send(888)
print(n4)