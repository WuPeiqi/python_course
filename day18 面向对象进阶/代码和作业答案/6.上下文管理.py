# # 文件操作
# """
# f = open('xxxx.log')
#
# f.read()
#
# f.close()
# """
#
# """
# with open("xxxx.log") as f:
#     f.read()
# """
#
#
# class Foo(object):
#
#     def __enter__(self):
#         print("进来了")
#         return 666
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("出去了")
#
#
# """
# obj = Foo()
#
# # with 对象 as f         在内部会执行__enter__方法
# # 当with缩进中的代码执行完毕，自动会执行__exit__
# with obj as f:
#     print(123)
#     print(f)
# """
# with Foo() as f:
#     print(123)
#     print(f)


class Context:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def do_something(self):
        print('内部执行')


with Context() as ctx:
    print('内部执行')
    ctx.do_something()
