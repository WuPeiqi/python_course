# v1 = int(1)
# v2 = int(5)
# v3 = v1 + v2
# print(v3)


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return "{}-{}".format(self.name, other.name)


v1 = Foo("alex")
v2 = Foo("sb")

# 对象+值，内部会去执行 对象.__add__方法，并将+后面的值当做参数传递过去。
v3 = v1 + v2
print(v3)
