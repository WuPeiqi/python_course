class Base(object):

    def __data(self):
        print("base.__data")

    def num(self):
        print("base.num")
        self.__data()  # 不允许执行父类中的私有方法


class Foo(Base):

    def func(self):
        self.num()


obj = Foo()
obj.func()
