class Account(object):

    def login(self):
        pass

    def register(self):
        pass

    def index(self):
        pass

    def run(self):
        name = input("请输入要执行的方法名称：")
        method = getattr(self, name)
        if not method:
            print("输入错误")
        method()


from importlib import import_module

from requests.exceptions import InvalidURL

from openpyxl.utils.exceptions import InvalidFileException