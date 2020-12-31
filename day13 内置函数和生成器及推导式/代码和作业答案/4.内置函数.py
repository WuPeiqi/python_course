data_list = [
    '1-5 编译器和解释器.mp4',
    '1-17 今日作业.mp4',
    '1-9 Python解释器种类.mp4',
    '1-16 今日总结.mp4',
    '1-2 课堂笔记的创建.mp4',
    '1-15 Pycharm使用和破解（win系统）.mp4',
    '1-12 python解释器的安装（mac系统）.mp4',
    '1-13 python解释器的安装（win系统）.mp4',
    '1-8 Python介绍.mp4', '1-7 编程语言的分类.mp4',
    '1-3 常见计算机基本概念.mp4',
    '1-14 Pycharm使用和破解（mac系统）.mp4',
    '1-10 CPython解释器版本.mp4',
    '1-1 今日概要.mp4',
    '1-6 学习编程本质上的三件事.mp4',
    '1-18 作业答案和讲解.mp4',
    '1-4 编程语言.mp4',
    '1-11 环境搭建说明.mp4'
]
result = sorted(data_list, key=lambda x: int(x.split(' ')[0].split("-")[-1]) )
print(result)
