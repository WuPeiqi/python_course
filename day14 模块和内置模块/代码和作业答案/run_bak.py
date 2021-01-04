"""
import应用场景：项目根目录的包模块级别的导入。
from应用场景：成员、嵌套的包模块时。
两种都是as别名，处理重名情况（更短）
"""

"""
# 导入一个模块
import many
v1 = many.show()

import commons.page as pg
v2 = pg.pagination()

# 导入一个包
import commons
print(commons.VERSION)
"""

# 导入成员
# from many import show, f1
# from commons.utils import encrypt
# v1 = encrypt("武沛齐")
# print(v1)


# 导入一个模块（至少一个嵌套）
# from commons import utils
# utils.encrypt("xxx")
# utils.f1()


# 导入一个包（至少一个嵌套）
# from commons import tencent
# import many
# from many import show


from commons.page import f1 as f11
from commons.utils import f1 as f122




















