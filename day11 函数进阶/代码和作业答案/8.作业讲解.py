# 1.如何查看一个值得内存地址？
"""
基于内置函数id来获取，例如：
    addr1 = id("武沛齐")
    addr2 = id([11,22,33,44])
"""

# 2.函数的参数传递的是引用（内存地址）还是值（拷贝一份）？
"""
参数参数默认传递的是引用（内存地址）
"""

# 3.看代码写结果
"""
v1 = {}
v2 = v1
v1["k1"] = 123

print(v1, v2)  # {'k1': 123} {'k1': 123}
"""

# 4.看代码写结果
"""
def func(k, v, info={}):
    info[k] = v
    return info


v1 = func(1, 2)
print(v1)  # {1: 2}

v2 = func(4, 5, {})
print(v2)  # {4: 5}

v3 = func(5, 6)
print(v3)  # {1: 2, 5: 6}
"""

# 5.看代码写结果
"""
def func(k, v, info={}):
    info[k] = v
    return info


v1 = func(1, 2)
v2 = func(4, 5, {})
v3 = func(5, 6)

print(v1, v2, v3)  # {1: 2, 5: 6}   {4: 5}   {1: 2, 5: 6}
"""

# 6. 简述第5题、第6题的结果为何结果不同。
"""
第5题中的 v1和v3变量指向的都是函数内部维护的那个列表的内存地址。
    先print(v1)时，函数内部维护的列表的值当时是{1: 2}
    最后print(v3)时，函数内部维护的列表的值已被修改为{1: 2, 5: 6}

第5题中的 v1和v3变量也是指向的都是函数内部维护的那个列表的内存地址。
    最后再print v1和v3 时，结果就是最终函数内部维护的列表的值，即： {1: 2, 5: 6}
"""

# 7.看代码写结果
"""
def func(*args, **kwargs):
    print(args, kwargs)
    return "完毕"


v1 = func(11, 22, 33)  # (11, 22, 33) {}
print(v1)  # 完毕

v2 = func([11, 22, 33])  # ([11, 22, 33],) {}
print(v2)  # 完毕

v3 = func(*[11, 22, 33])  # (11, 22, 33) {}
print(v3)  # 完毕

v4 = func(k1=123, k2=456)  # () {'k1': 123, 'k2': 456}
print(v4)  # 完毕

v5 = func({"k1": 123, "k2": 456})  # ({'k1': 123, 'k2': 456},) {}
print(v5)  # 完毕

v6 = func(**{"k1": 123, "k2": 456})  # () {'k1': 123, 'k2': 456}
print(v6)  # 完毕

v7 = func([11, 22, 33], **{"k1": 123, "k2": 456})  # ([11, 22, 33],) {'k1': 123, 'k2': 456}
print(v7)  # 完毕

v8 = func(*[11, 22, 33], **{"k1": 123, "k2": 456})  # (11, 22, 33) {'k1': 123, 'k2': 456}
print(v8)  # 完毕
"""

# 8.看代码写结果
"""
def func(*args, **kwargs):
    prev = "-".join(args)
    data_list = []
    for k, v in kwargs.items():
        item = "{}-{}".format(k, v)
        data_list.append(item)
        content = "*".join(data_list)
    return prev, content


v1 = func("北京", "上海", city="深圳", count=99)
print(v1)  # ('北京-上海', 'city-深圳*count-99')

v2 = func(*["北京", "上海"], **{"city": "深圳", "count": 99})
print(v2)  # ('北京-上海', 'city-深圳*count-99')
"""

# 9.补充代码，实现获取天气信息并按照指定格式写入到文件中。【重点讲】
"""
import requests


def write_file(**kwargs):
    data_list = []

    row_dict = kwargs["weatherinfo"]
    for k, v in row_dict.items():
        group = "{}-{}".format(k, v)
        data_list.append(group)
    row_string = ",".join(data_list)

    with open('xxxx.txt', mode='a', encoding="utf-8") as file_object:
        file_object.write("{}\n".format(row_string))


def get_weather(code):
    url = "http://www.weather.com.cn/data/ks/{}.html".format(code)
    res = requests.get(url=url)
    res.encoding = "utf-8"
    weather_dict = res.json()
    return weather_dict


city_list = [
    {'code': "101020100", 'title': "上海"},
    {'code': "101010100", 'title': "北京"},
]

for item in city_list:
    # 101020100
    result_dict = get_weather(item["code"])
    write_file(**result_dict)
"""

# 10.看代码写结果
"""
def func():
    return 1, 2, 3


val = func()
print( type(val) == tuple) # True
print( type(val) == list) # False
print( type(val) == dict) # False
"""
"""
info = {
    "1": [11, 22, 33],
    "2": {'k1': 123, "k2": 456, "k3": "999"}
}
index = input("请输入序号：")
value = info[index]
if type(value) == list:
    print(value[0], value[1], value[2])
elif type(value) == dict:
    print(value['k1'], value['k2'], value['k3'])
"""
# 11.看代码写结果
"""
def func(users, name):
    users.append(name)
    print(users)


result = func(['武沛齐', '李杰'], 'alex')  # # ['武沛齐', '李杰', 'alex']
print(result)  # None
"""

# 12.看代码写结果
"""
def func(v1):
    return v1 * 2


def bar(arg):
    return "%s 是什么玩意？" % (arg,)


val = func('你')
data = bar(val)
print(data) # 你你 是什么玩意？
"""

# 13.看代码写结果
"""
def func(v1):
    return v1 * 2


def bar(arg):
    msg = "%s 是什么玩意？" % (arg,)
    print(msg)


val = func('你')
data = bar(val) # 你你 是什么玩意？
print(data) # None
"""

# 14.看代码写结果
"""
def func():
    data = 2 * 2
    return data

data_list = [func,func,func]

for item in data_list:
    v = item()
    print(v)

# 输出：
# 4  
# 4  
# 4
"""

# 15.分析代码，写结果
"""
def func(handler, **kwargs):
    # handler() -> killer()
    # kwargs = {"name": "武沛齐", "age": 18}
    extra = {
        "code": 123,
        "name": "武沛齐"
    }
    kwargs.update(extra)
    # kwargs = {"name": "武沛齐", "age": 18,"code": 123,}
    return handler(**kwargs)


def something(**kwargs):
    return len(kwargs)


def killer(**kwargs):
    # {"name": "武沛齐", "age": 18,"code": 123,}
    key_list = []
    for key in kwargs.keys():
        key_list.append(key)
    return key_list # ["name","age","code"]


v1 = func(something, k1=123, k2=456)
print(v1)  # 4

v2 = func(killer, **{"name": "武沛齐", "age": 18})
print(v2)  # ["name","age","code"]
"""

# 16.两个结果输出的分别是什么？并简述其原因。
"""
def func():
    return 123


v1 = [func, func, func, func, ]
print(v1)  # 列表，内部元素都是函数（将函数名放在列表的索引位置，函数名代指函数）

v2 = [func(), func(), func(), func()]
print(v2)  # 列表，内部元素都是123（执行函数之后，将函数的返回值放在列表的索引位置）
"""

# 17.看代码结果
"""
v1 = '武沛齐'


def func():
    print(v1)


func()  # 武沛齐
func()  # 武沛齐
"""

# 18.看代码结果
"""
v1 = '武沛齐'


def func():
    print(v1)


func()  # 武沛齐

v1 = '老男人'

func()  # 老男人
"""

# 19.看代码写结果
"""
NUM_LIST = []
SIZE = 18


def f1():
    NUM_LIST.append(8)
    SIZE = 19


def f2():
    print(NUM_LIST)
    print(SIZE)


f2()  # []   18
f1()  # 无任何输出
f2()  # [8]   18
"""

# 20.看代码写结果
"""
NUM_LIST = [11, 22, 33]
SIZE = 18


def f1():
    global NUM_LIST
    global SIZE
    NUM_LIST = "武沛齐"
    SIZE = 19


def f2():
    print(NUM_LIST)
    print(SIZE)


f2()  # [11,22,33] 18
f1()  # 无输出
f2()  # 武沛齐  19
"""

# 21.资源下载器 v1版本【重点讲】
"""
import requests

SELECTED_IMAGE_SET = set()  # 已下载图片ID（序号）
SELECTED_VIDEO_SET = set()
SELECTED_NBA_SET = set()


def download(file_path, url):
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )
    with open(file_path, mode='wb') as f:
        f.write(res.content)


def download_image():
    total_image_dict = {
        "1": ("吉他男神", "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V"),
        "2": ("漫画美女", "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO"),
        "3": ("游戏地图", "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd"),
        "4": ("alex媳妇", "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz"),
    }
    while True:
        # 构造 1.吉他男神;2.漫画美女;
        text_list = []
        for num, item in total_image_dict.items():
            if num in SELECTED_IMAGE_SET:
                continue
            data = "{}.{}".format(num, item[0])
            text_list.append(data)
        if text_list:
            text = ";".join(text_list)
        else:
            text = "无可下载选项"
        # 输出：1.吉他男神;2.漫画美女;3.游戏地图;4.alex媳妇
        print(text)

        # 返回上一步
        index = input("请输入要选择的序号(Q/q退出）：")
        if index.upper() == "Q":
            return

        # 选择序号 3
        if index in SELECTED_IMAGE_SET:
            print("已下载，无法再继续下载，请重新选择！")
            continue

        group = total_image_dict.get(index)
        if not group:
            print("序号不存在，请重新选择")
            continue

        # 下载图片
        file_path = "{}.png".format(group[0])
        download(file_path, group[1])

        # 已下载集合中
        SELECTED_IMAGE_SET.add(index)


def download_video():
    total_video_dict = {
        "1": {"title": "东北F4模仿秀",
              'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"},
        "2": {"title": "卡特扣篮",
              'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"},
        "3": {"title": "罗斯mvp",
              'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"},
    }

    while True:
        text_list = []
        for num, item in total_video_dict.items():
            if num in SELECTED_VIDEO_SET:
                continue
            data = "{}.{}".format(num, item["title"])
            text_list.append(data)
        if text_list:
            text = ";".join(text_list)
        else:
            text = "无可下载选项"
        print(text)
        index = input("请输入要选择的序号(Q/q退出）：")
        if index.upper() == "Q":
            return

        if index in SELECTED_VIDEO_SET:
            print("已下载，无法再继续下载，请重新选择！")
            continue

        group = total_video_dict.get(index)
        if not group:
            print("序号不存在，请重新选择")
            continue

        file_path = "{}.mp4".format(group["title"])
        download(file_path, group["url"])

        SELECTED_VIDEO_SET.add(index)


def download_nba():
    total_nba_dict = {
        "1": {"title": "威少奇才首秀三双",
              "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"},
        "2": {"title": "塔图姆三分准绝杀",
              "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"}

    }
    while True:
        text_list = []
        for num, item in total_nba_dict.items():
            if num in SELECTED_NBA_SET:
                continue
            data = "{}.{}".format(num, item["title"])
            text_list.append(data)
        if text_list:
            text = ";".join(text_list)
        else:
            text = "无可下载选项"
        print(text)
        index = input("请输入要选择的序号(Q/q退出）：")
        if index.upper() == "Q":
            return

        if index in SELECTED_NBA_SET:
            print("已下载，无法再继续下载，请重新选择！")
            continue

        group = total_nba_dict.get(index)
        if not group:
            print("序号不存在，请重新选择")
            continue

        file_path = "{}.mp4".format(group["title"])
        download(file_path, group["url"])

        SELECTED_NBA_SET.add(index)


print("欢迎使用xxx系统")
func_dict = {
    "1": download_image,
    "2": download_video,
    "3": download_nba
}
while True:
    print("1.花瓣网图片专区;2.抖音短视频专区;3.NBA锦集专区 ")
    choice = input("请选择序号：")
    if choice.upper() == "Q":
        break
    func = func_dict.get(choice)
    if not func:
        print("输入错误，请重新选择！")
        continue
    # 进入专区
    func()
"""

# 21.资源下载器 v2版本
"""
import requests

DB = {
    "1": {
        "area": "花瓣网图片专区",
        "total_dict": {
            "1": ("吉他男神", "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V"),
            "2": ("漫画美女", "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO"),
            "3": ("游戏地图", "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd"),
            "4": ("alex媳妇", "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz"),
        },
        "ext": "png",
        "selected": set()
    },
    "2": {
        "area": "抖音短视频专区",
        "total_dict": {
            "1": {"title": "东北F4模仿秀",
                  'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"},
            "2": {"title": "卡特扣篮",
                  'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"},
            "3": {"title": "罗斯mvp",
                  'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"},
        },
        "ext": "mp4",
        "selected": set()
    },
    "3": {
        "area": "NBA锦集专区",
        "total_dict": {
            "1": {"title": "威少奇才首秀三双",
                  "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"},
            "2": {"title": "塔图姆三分准绝杀",
                  "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"}
        },
        "ext": "mp4",
        "selected": set()
    },
}


def download(file_path, url):
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )
    with open(file_path, mode='wb') as f:
        f.write(res.content)


def handler(area_info):
    # 进入专区提醒
    summary = "欢迎进入{}".format(area_info['area'])
    print(summary)

    # 专区中选择下载
    while True:
        text_list = []
        for num, item in area_info['total_dict'].items():
            if num in area_info['selected']:
                continue
            if type(item) == tuple:
                data = "{}.{}".format(num, item[0])
            else:
                data = "{}.{}".format(num, item["title"])
            text_list.append(data)
        if text_list:
            text = ";".join(text_list)
        else:
            text = "无可下载选项"

        print(text)
        index = input("请输入要选择的序号(Q/q退出）：")
        if index.upper() == "Q":
            return

        if index in area_info['selected']:
            print("已下载，无法再继续下载，请重新选择！")
            continue

        group = area_info['total_dict'].get(index)
        if not group:
            print("序号不存在，请重新选择")
            continue

        if type(group) == tuple:
            title, url = group
        else:
            title, url = group['title'], group['url']

        file_path = "{}.{}".format(title, area_info['ext'])
        download(file_path, url)

        area_info['selected'].add(index)


print("欢迎使用xxx系统")
while True:
    print("1.花瓣网图片专区;2.抖音短视频专区;3.NBA锦集 专区 ")
    choice = input("请选择序号（Q/q退出）：")
    if choice.upper() == "Q":
        break

    # 选择序号： 去db中找对应的字典信息
    area_dict = DB.get(choice)

    if not area_dict:
        print("输入错误，请重新选择！")
        continue

    # 进入专区（area_dict选择的专区信息）
    handler(area_dict)

"""